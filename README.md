# discord_discourse

A simple Discord bot that searches the [GL.iNet forum](https://forum.gl-inet.com/) (powered by Discourse) and returns the top five matching topics.

## Usage

1. Create a Discord bot token and invite the bot to your server.
2. Set the `DISCORD_TOKEN` environment variable to your bot token.
3. Start the bot using Docker:

```bash
docker build -t discord-discourse .
docker run -e DISCORD_TOKEN=YOUR_TOKEN discord-discourse
```

In Discord, use:

```
!search your query here
```

The bot will reply with up to five matching links from the forum.
