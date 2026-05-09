import dotenv from "dotenv";

dotenv.config();

export function csv(value) {
  return String(value || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function isTrue(value) {
  return /^(1|true|yes|on)$/i.test(String(value || "").trim());
}

export const config = {
  discordToken: process.env.DISCORD_BOT_TOKEN || "",
  discordClientId: process.env.DISCORD_CLIENT_ID || process.env.DISCORD_APPLICATION_ID || "",
  discordGuildId: process.env.DISCORD_GUILD_ID || "",
  enableMessageContentIntent: isTrue(process.env.DISCORD_ENABLE_MESSAGE_CONTENT_INTENT),
  alertChannelId: process.env.DISCORD_ALERT_CHANNEL_ID || "",
  adminIds: new Set(csv(process.env.DISCORD_ADMIN_IDS)),
  botDisplayName: process.env.BOT_DISPLAY_NAME || "LuciferSun Research Bot",
  aiSystemPrompt:
    process.env.AI_SYSTEM_PROMPT ||
    "You are a professional Discord assistant for an open computational research server. Be concise, technically serious, helpful, and skeptical in a scientific way. Avoid hype, conspiracy framing, and cult-like language. When uncertain, say what is uncertain. Prefer practical next steps, reproducibility, and clear reasoning. Respond in the same language as the user's message unless the user explicitly asks for another language. If the message mixes languages, answer in the dominant language of the user's prompt.",
  openaiApiKey: process.env.OPENAI_API_KEY || "",
  openaiModel: process.env.OPENAI_MODEL || "gpt-5-mini",
  openrouterApiKey: process.env.OPENROUTER_API_KEY || "",
  openrouterModel: process.env.OPENROUTER_MODEL || "openrouter/free",
  openrouterFallbackModel: process.env.OPENROUTER_FALLBACK_MODEL || "openrouter/free",
  keywords: csv(
    process.env.GRANT_KEYWORDS ||
      "AI,open source,research software,scientific computing,compute,physics,data infrastructure,reproducibility"
  ),
  scanIntervalMinutes: Number(process.env.GRANT_SCAN_INTERVAL_MINUTES || 360),
  grantsGovRows: Number(process.env.GRANTS_GOV_ROWS || 10)
};

export function isAdmin(userId) {
  return config.adminIds.has(String(userId));
}
