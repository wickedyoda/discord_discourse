# discord_discourse

A simple Discord bot that searches the [GL.iNet forum](https://forum.gl-inet.com/) (powered by Discourse) and returns the top five matching topics.

## Usage

1. Create a Discord bot token and invite the bot to your server.
2. Set the `DISCORD_TOKEN` environment variable to your bot token. The bot
   requires the Message Content intent to be enabled in the Discord developer
   portal.
3. Optionally set `DISCOURSE_BASE_URL` to the base URL of the Discourse
   forum you want to search (defaults to `https://forum.gl-inet.com`).
4. Start the bot using Docker:

```bash
docker build -t discord-discourse .
docker run -e DISCORD_TOKEN=YOUR_TOKEN \
           -e DISCOURSE_BASE_URL=https://forum.gl-inet.com \
           discord-discourse
```

In Discord, use:

```
!search your query here
```

The bot will reply with up to five matching links from the forum.
