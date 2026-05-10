# Discord/Owl Black Box

Purpose: keep an append-only operational record for the Discord server, Owl/OpenRouter bot behavior, deployment changes, incidents, and continuity notes.

Use this file as the first place to check when resuming work on:

- Discord bot configuration
- server/channel setup state
- OpenRouter/Owl model behavior
- webhook/integration status
- moderation or access changes
- deployment and runtime failures

Rules:

1. Append new entries at the top or bottom consistently. Do not rewrite history.
2. Record facts, not guesses.
3. Do not store tokens, webhook URLs, passwords, or secret keys here.
4. Reference files, commits, channels, and commands when useful.
5. End each entry with the next concrete action if follow-up is needed.

Recommended entry format:

```text
Date:
Operator:
Area:
Change / event:
Observed result:
Impact:
Next step:
Files / channels:
```

---

## 2026-05-09

Date: 2026-05-09
Operator: Codex + user
Area: Discord bot / repo integration
Change / event:
- built and stabilized the Discord research bot with Owl/OpenRouter support
- added slash commands for `ask`, `ping`, `about`, `github`, `publications`, and admin preset posting
- configured language-aware replies with Polish/English/Chinese handling
- placed the bot project in `shared/discord-server-bot-owl/`
- added Codex continuity ops files in `MHLM/ai-workflows/ops/`
Observed result:
- bot logs in successfully as `LuciferSun Grant Bot`
- slash commands register on the research server guild
- `/ask` works with OpenRouter and Owl primary routing
Impact:
- server now has a working AI research assistant and a tracked repo location for the Discord/Owl tooling
Next step:
- document server setup and GitHub-to-Discord update flow in a dedicated setup doc
Files / channels:
- `shared/discord-server-bot-owl/`
- Discord guild: `Akasha Chroniclles Open Research Lab`
- channel planned for updates: `#github-updates`
