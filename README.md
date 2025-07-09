# 🔗 Link – Discord Search Bot for GL.iNet Forum

**Link** is a simple, containerized Discord bot that allows users to search the [GL.iNet Community Forum](https://forum.gl-inet.com/) using either slash commands (`/search`) or the traditional `!search` prefix.

---

## 💡 Features

- 🔍 Search GL.iNet’s official forum from Discord.
- 💬 Supports both `/search` slash command and `!search` prefix command.
- 🔗 Returns top 5 relevant results with clickable links.
- 🐳 Docker-ready with GitHub container image.
- 🔧 Easy deployment via `.env` file or Docker Compose.
- 🎯 Designed for use in GL.iNet-related Discord servers.

---

## 🛠 Setup & Configuration

### 1. Create a `.env` file
Place this in the project root:

```env
DISCORD_TOKEN=your_discord_bot_token
GUILD_ID=your_discord_server_id
```

### 2. Docker Compose (Optional)
You can deploy using Docker Compose:

```yaml
version: "3.8"

services:
  discord_discourse:
    image: ghcr.io/wickedyoda/discord_discourse:latest
    restart: unless-stopped
    env_file:
      - .env
```

Run it with:

```bash
docker compose up -d
```

---

## 🤖 Bot Commands

### `/search [query]`
Search the GL.iNet forum using a slash command.

- Example: `/search wireguard`

### `!search [query]`
Classic text-based command (works in any channel where the bot has permissions).

- Example: `!search repeater mode`

---

## 🚀 Discord Bot Invite

Use this link to invite the bot to your server:

👉 [Invite Link](https://discord.com/oauth2/authorize?client_id=1392251842343206963&permissions=2416004096&scope=bot+applications.commands)

---

## 🧠 How It Works

- Uses the Discourse JSON API (`/search.json`) from [forum.gl-inet.com](https://forum.gl-inet.com/).
- Parses search results and formats clickable topic links.
- Supports ephemeral (private) or public responses.

---

## 🔒 Permissions Needed

To function properly, ensure the bot has the following Discord permissions:
- `Read Messages/View Channels`
- `Send Messages`
- `Use Slash Commands`
- `Embed Links`
- (Optional) `Manage Messages` (for future features)

---

## 🐳 Docker Notes

If you're building the container manually:

```bash
docker build -t discord_discourse .
docker run --env-file .env discord_discourse
```

To run it cross-platform (including ARM64), ensure your image is built using multi-arch in GitHub Actions or locally using `buildx`.

---

## 📝 Credits

- Built by [WickedYoda](https://wickedyoda.com)
- Uses: [`discord.py`](https://discordpy.readthedocs.io/), [`requests`](https://docs.python-requests.org/), [`bs4`](https://www.crummy.com/software/BeautifulSoup/)

---

## 🔗 Related

- [GL.iNet Forum](https://forum.gl-inet.com/)
- [Bot Repository](https://github.com/wickedyoda/discord_discourse)
- [WickedYoda Discord](https://discord.gg/m6UjX6UhKe)

---

Let us know if you need help! Join the community and open an issue or feature request. 👾