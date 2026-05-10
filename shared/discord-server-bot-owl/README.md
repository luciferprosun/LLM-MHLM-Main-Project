# Discord Grant Bot

Discord bot for finding public grant and funding opportunities.

## What It Does

- Searches Grants.gov open/forecasted opportunities through the official public API.
- Watches configured foundation/RFA pages for funding wording.
- Stores results locally in `data/grants.json`.
- Posts scheduled alerts to a configured Discord channel.
- Supports manual Discord commands.

It does not send emails or spam funders. It only collects public opportunities for review.

## Setup

1. Create a Discord application:
   https://discord.com/developers/applications

2. Add a bot user and copy the bot token.

3. Copy config:

```bash
cp .env.example .env
```

4. Edit `.env`:

```bash
DISCORD_BOT_TOKEN=your_token
DISCORD_APPLICATION_ID=your_application_id
DISCORD_GUILD_ID=your_server_id
DISCORD_ENABLE_MESSAGE_CONTENT_INTENT=false
BOT_DISPLAY_NAME=LuciferSun Research Bot
AI_SYSTEM_PROMPT=You are a professional Discord assistant for an open computational research server and should answer in the same language as the user.
DISCORD_ADMIN_IDS=your_discord_user_id
DISCORD_ALERT_CHANNEL_ID=optional_channel_id
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5-mini
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=openrouter/free
OPENROUTER_FALLBACK_MODEL=openrouter/free
```

5. Install dependencies:

```bash
npm install
```

6. Run:

```bash
npm start
```

## Bot Invite

In the Discord Developer Portal, enable these bot permissions:

- Send Messages
- Read Message History
- View Channels

For message-prefix commands, enable `MESSAGE CONTENT INTENT` under Bot settings.

For fast slash command registration during setup, set `DISCORD_GUILD_ID` to your server ID.

If `OPENROUTER_API_KEY` is set, `/ask` will use OpenRouter. If the chosen OpenRouter model is rate-limited and `OPENROUTER_FALLBACK_MODEL` is set, it retries with the fallback model. Otherwise it falls back to OpenAI only when OpenRouter is not configured.

## Commands

- `/ping`
- `/about`
- `/github`
- `/publications scope:best|all`
- `!grant help`
- `!grant whoami`
- `!grant scan`
- `!grant list`
- `!grant search AI open source`
- `!grant sources`
- `!grant setchannel` admin only
- `/ask prompt:<question>`

The bot also answers when mentioned in a server channel.

For mention-based replies, enable `MESSAGE CONTENT INTENT` in the Discord Developer Portal and set `DISCORD_ENABLE_MESSAGE_CONTENT_INTENT=true`.

## Sources

Edit `sources.json` to add or remove monitored pages.

## Operations

Use the black-box log for continuity and incident tracking:

- `ops/BLACK_BOX.md`
- `ops/BLACK_BOX_TEMPLATE.md`

Do not store secrets in the black-box log.
