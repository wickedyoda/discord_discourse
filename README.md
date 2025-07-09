# 🔍 Search Bot for GL.iNet Forum

**Search Bot** is a lightweight Discord bot that allows users to search the [GL.iNet Forum](https://forum.glinet.net) directly from Discord using a simple slash command or a traditional `!search` command. It responds with the top 5 discussion threads matching your search query.

---

## ✨ Features

- `/search [keywords]`: Publicly returns top 5 search results from the GL.iNet forum.
- `!search [keywords]`: Legacy command prefix support.
- Built with Python and Discord API.
- Docker-ready for simple deployment.

---

## 📂 Project Structure

.
├── bot.py               # Main bot logic
├── Dockerfile           # Docker build file
├── requirements.txt     # Python dependencies
├── docker-compose.yml   # Compose config (pulls built image)
└── .env                 # Environment variables (not committed)

---

## ⚙️ Environment Variables

Create a `.env` file in the root of the project with the following content:

```env
DISCORD_TOKEN=your_discord_bot_token
GUILD_ID=your_discord_server_id

🐳 Docker Deployment

This bot is designed to run inside a container using a prebuilt image hosted at:
ghcr.io/wickedyoda/discord_discourse:latest

To deploy using Docker Compose:
docker compose up -d

Ensure your .env file is in the same directory as docker-compose.yml.

✅ Discord Bot Setup
	1.	Go to the Discord Developer Portal.
	2.	Create a new application or select your existing bot.
	3.	Enable the following OAuth2 Scopes:
	•	bot
	•	applications.commands
	4.	Set permissions to include:
	•	Send Messages
	•	Read Message History
	•	Use Slash Commands
	5.	Use the OAuth2 URL to invite the bot to your server:
      https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=2416004096&scope=bot+applications.commands


🔎 Example Commands
	•	/search vpn
	•	!search firmware upgrade

⸻

📦 Image Repository

This bot is built and pushed automatically via GitHub Actions to:
	•	GHCR: ghcr.io/wickedyoda/discord_discourse

⸻

📬 Support

Need help? Join the Wicked Discord Link community here:

🔗 https://discord.gg/m6UjX6UhKe