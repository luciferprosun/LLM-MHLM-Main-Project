import { Client, GatewayIntentBits, Partials, REST, Routes, SlashCommandBuilder } from "discord.js";
import { config, isAdmin } from "./config.js";
import { loadSources } from "./foundationPages.js";
import { askOpenAI } from "./openai.js";
import {
  formatGitHubLinks,
  formatPapersPost,
  formatPublicationLinks,
  formatServerDescription,
  formatWelcomePost
} from "./researchCatalog.js";
import { filterGrants, formatGrant, runGrantScan } from "./scanner.js";
import { readGrants, readState, writeState } from "./storage.js";

if (!config.discordToken) {
  throw new Error("Missing DISCORD_BOT_TOKEN. Copy .env.example to .env and fill it.");
}

const client = new Client({
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages].concat(
    config.enableMessageContentIntent ? [GatewayIntentBits.MessageContent] : []
  ),
  partials: [Partials.Channel]
});
const mentionCooldown = new Map();

function chunk(text, limit = 1900) {
  if (text.length <= limit) return [text];
  const out = [];
  let rest = text;
  while (rest.length > limit) {
    const cut = rest.lastIndexOf("\n", limit);
    const at = cut > 500 ? cut : limit;
    out.push(rest.slice(0, at));
    rest = rest.slice(at).trim();
  }
  if (rest) out.push(rest);
  return out;
}

async function sendLong(channel, text) {
  for (const part of chunk(text)) {
    await channel.send(part);
  }
}

async function replyLong(interaction, text) {
  const parts = chunk(text);
  for (const [index, part] of parts.entries()) {
    if (index === 0) await interaction.reply(part);
    else await interaction.followUp(part);
  }
}

function ensureAdminInteraction(interaction) {
  if (isAdmin(interaction.user.id)) {
    return true;
  }

  interaction.reply({ content: "Admin only.", ephemeral: true }).catch(() => {});
  return false;
}

function buildResearchPrompt(rawPrompt) {
  return [
    "Server context:",
    "- Open computational research laboratory",
    "- Topics: neutrino anomaly research, AI-assisted theory work, simulation, reproducibility, coding",
    "- Style: rigorous, concise, technically serious",
    "",
    rawPrompt
  ].join("\n");
}

function detectPromptLanguage(text) {
  const value = String(text || "").trim();
  if (!value) return "en";

  if (/[\u4e00-\u9fff]/.test(value)) return "zh";
  if (/[ąćęłńóśźż]/i.test(value)) return "pl";

  const lower = value.toLowerCase();
  const polishHints = [" czy ", " jest ", " się ", " serwer ", " opisz ", " wyjaśnij ", " po polsku ", " czym "];
  const englishHints = [" the ", " and ", " what ", " explain ", " describe ", " server ", " how "];

  const score = (hints) => hints.reduce((sum, hint) => sum + (lower.includes(hint) ? 1 : 0), 0);
  const plScore = score(polishHints);
  const enScore = score(englishHints);

  if (plScore > enScore) return "pl";
  if (enScore > plScore) return "en";
  return "en";
}

function systemPromptForText(text) {
  const language = detectPromptLanguage(text);
  if (language === "pl") {
    return `${config.aiSystemPrompt} Respond in Polish.`;
  }
  if (language === "zh") {
    return `${config.aiSystemPrompt} Respond in Chinese.`;
  }
  return `${config.aiSystemPrompt} Respond in English unless the user explicitly asks for another language.`;
}

function canUseMentionReply(message) {
  const key = `${message.author.id}:${message.channelId}`;
  const now = Date.now();
  const last = mentionCooldown.get(key) || 0;
  if (now - last < 10000) {
    return false;
  }

  mentionCooldown.set(key, now);
  return true;
}

async function registerSlashCommands() {
  if (!config.discordClientId) {
    console.warn("Missing DISCORD_CLIENT_ID. Skipping slash command registration.");
    return;
  }

  const commands = [
    new SlashCommandBuilder().setName("ping").setDescription("Check if the bot is online").toJSON(),
    new SlashCommandBuilder().setName("about").setDescription("Show what this bot does").toJSON(),
    new SlashCommandBuilder().setName("github").setDescription("Show GitHub and website links for this project").toJSON(),
    new SlashCommandBuilder()
      .setName("publications")
      .setDescription("Show Zenodo publications for this project")
      .addStringOption((option) =>
        option
          .setName("scope")
          .setDescription("Show selected best records or a broader list")
          .setRequired(false)
          .addChoices({ name: "best", value: "best" }, { name: "all", value: "all" })
      )
      .toJSON(),
    new SlashCommandBuilder()
      .setName("postpreset")
      .setDescription("Admin: post prepared server content into this channel")
      .addStringOption((option) =>
        option
          .setName("section")
          .setDescription("Which prepared content to post")
          .setRequired(true)
          .addChoices(
            { name: "welcome", value: "welcome" },
            { name: "github", value: "github" },
            { name: "publications", value: "publications" },
            { name: "description", value: "description" },
            { name: "all", value: "all" }
          )
      )
      .toJSON(),
    new SlashCommandBuilder()
      .setName("ask")
      .setDescription("Ask the AI assistant a research/coding question")
      .addStringOption((option) =>
        option.setName("prompt").setDescription("Your question").setRequired(true).setMaxLength(1800)
      )
      .toJSON()
  ];

  const rest = new REST({ version: "10" }).setToken(config.discordToken);
  if (config.discordGuildId) {
    await rest.put(Routes.applicationGuildCommands(config.discordClientId, config.discordGuildId), { body: commands });
    console.log(`Registered slash commands for guild ${config.discordGuildId}`);
    return;
  }

  await rest.put(Routes.applicationCommands(config.discordClientId), { body: commands });
  console.log("Registered global slash commands.");
}

async function handleGrantCommand(message) {
  const args = message.content.trim().split(/\s+/).slice(1);
  const sub = (args.shift() || "help").toLowerCase();

  if (sub === "help") {
    return sendLong(
      message.channel,
      [
        "Grant bot commands:",
        "`!grant whoami`",
        "`!grant scan`",
        "`!grant list`",
        "`!grant search AI open source`",
        "`!grant sources`",
        "`!grant setchannel` admin only"
      ].join("\n")
    );
  }

  if (sub === "whoami") {
    return message.reply(`Your Discord user ID: ${message.author.id}\nAdmin: ${isAdmin(message.author.id)}`);
  }

  if (sub === "setchannel") {
    if (!isAdmin(message.author.id)) return message.reply("Admin only.");
    const state = await readState();
    state.alertChannelId = message.channel.id;
    await writeState(state);
    return message.reply(`Alert channel set to <#${message.channel.id}>.`);
  }

  if (sub === "sources") {
    const sources = await loadSources();
    return sendLong(
      message.channel,
      sources.map((source) => `- ${source.name}: ${source.url}`).join("\n")
    );
  }

  if (sub === "scan") {
    if (!isAdmin(message.author.id)) return message.reply("Admin only.");
    const note = await message.reply("Scanning public grant sources...");
    const { grants, newlyFound } = await runGrantScan(args);
    return note.edit(`Scan complete. Total stored: ${grants.length}. New this scan: ${newlyFound.length}.`);
  }

  if (sub === "list") {
    const grants = (await readGrants()).slice(0, 8);
    if (!grants.length) return message.reply("No grants stored yet. Run `!grant scan` first.");
    return sendLong(message.channel, grants.map((grant, i) => formatGrant(grant, i + 1)).join("\n\n"));
  }

  if (sub === "search") {
    const query = args.join(" ").trim();
    if (!query) return message.reply("Usage: `!grant search AI open source`");
    const results = filterGrants(await readGrants(), query).slice(0, 8);
    if (!results.length) return message.reply("No stored results matched. Try `!grant scan` with your keywords.");
    return sendLong(message.channel, results.map((grant, i) => formatGrant(grant, i + 1)).join("\n\n"));
  }

  return message.reply("Unknown command. Use `!grant help`.");
}

async function scheduledScan() {
  try {
    const state = await readState();
    const channelId = state.alertChannelId || config.alertChannelId;
    const { newlyFound } = await runGrantScan();
    if (!channelId || !newlyFound.length) return;
    const channel = await client.channels.fetch(channelId);
    if (!channel) return;
    await sendLong(
      channel,
      ["New grant/funding opportunities found:", ...newlyFound.slice(0, 5).map((grant, i) => formatGrant(grant, i + 1))].join(
        "\n\n"
      )
    );
  } catch (error) {
    console.error("Scheduled scan failed:", error);
  }
}

client.once("clientReady", async () => {
  console.log(`Logged in as ${client.user.tag}`);
  await registerSlashCommands();
  setInterval(scheduledScan, Math.max(15, config.scanIntervalMinutes) * 60 * 1000);
});

client.on("messageCreate", async (message) => {
  if (message.author.bot) return;
  const content = message.content.trim();

  if (content.startsWith("!grant")) {
    try {
      await handleGrantCommand(message);
    } catch (error) {
      console.error(error);
      await message.reply(`Grant bot error: ${error.message || error}`);
    }
    return;
  }

  if (!message.mentions.has(client.user) || !content) return;
  if (!canUseMentionReply(message)) {
    await message.reply("Rate limit: wait a few seconds before asking again in this channel.");
    return;
  }

  const prompt = content.replaceAll(`<@${client.user.id}>`, "").replaceAll(`<@!${client.user.id}>`, "").trim();

  try {
    await message.channel.sendTyping();
    const effectivePrompt = buildResearchPrompt(prompt || "Introduce yourself and explain how you can help here.");
    const answer = await askOpenAI(effectivePrompt, { systemPrompt: systemPromptForText(prompt) });
    await sendLong(message.channel, answer);
  } catch (error) {
    console.error(error);
    await message.reply(`AI error: ${error.message || error}`);
  }
});

client.on("interactionCreate", async (interaction) => {
  if (!interaction.isChatInputCommand()) return;
  if (interaction.commandName === "ping") {
    await interaction.reply("Online.");
    return;
  }

  if (interaction.commandName === "about") {
    await interaction.reply(
      `${config.botDisplayName} helps with research discussion, coding questions, grant tracking, GitHub links, and Zenodo publications. Use \`/ask\`, \`/github\`, \`/publications\`, or mention the bot in a channel.`
    );
    return;
  }

  if (interaction.commandName === "github") {
    await replyLong(interaction, formatGitHubLinks());
    return;
  }

  if (interaction.commandName === "publications") {
    const scope = interaction.options.getString("scope") || "best";
    await replyLong(interaction, formatPublicationLinks(scope));
    return;
  }

  if (interaction.commandName === "postpreset") {
    if (!ensureAdminInteraction(interaction)) return;

    const section = interaction.options.getString("section", true);
    await interaction.reply({ content: `Posting preset content: ${section}`, ephemeral: true });

    if (section === "welcome" || section === "all") {
      await sendLong(interaction.channel, formatWelcomePost());
    }
    if (section === "github" || section === "all") {
      await sendLong(interaction.channel, formatGitHubLinks());
    }
    if (section === "publications" || section === "all") {
      await sendLong(interaction.channel, formatPapersPost());
    }
    if (section === "description" || section === "all") {
      await sendLong(interaction.channel, ["Server description draft:", formatServerDescription()].join("\n\n"));
    }
    return;
  }

  if (interaction.commandName !== "ask") return;

  const prompt = interaction.options.getString("prompt", true).trim();
  await interaction.deferReply();

  try {
    const answer = await askOpenAI(buildResearchPrompt(prompt), { systemPrompt: systemPromptForText(prompt) });
    for (const [i, part] of chunk(answer).entries()) {
      if (i === 0) await interaction.editReply(part);
      else await interaction.followUp(part);
    }
  } catch (error) {
    console.error(error);
    await interaction.editReply(`AI error: ${error.message || error}`);
  }
});

client.login(config.discordToken);
