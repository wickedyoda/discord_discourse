# Discord Discourse Bot

This repository outlines a simple Discord bot that searches the [GL.iNet forum](https://forum.gl-inet.com/) and returns the top five results for a query. The GL.iNet community uses [Discourse](https://www.discourse.org/) software, so the bot interacts with its public API to fetch links.

> **Note**: You are responsible for ensuring your usage complies with the GL.iNet forum terms of service and API guidelines. Use this bot responsibly and avoid excessive requests.

## Features

- Responds to commands in Discord and returns up to five links that match the search query.
- Uses the Discourse API (`/search.json`) to retrieve results.
- Dockerized deployment for easier hosting.
- Designed for use by all members of your Discord server.

## Setup

### Requirements

- Python 3.11+
- A Discord bot token ([create one here](https://discord.com/developers/applications)).
- `discord.py` and `requests` Python packages.
- A running Docker environment (for containerized deployment).

### Environment Variables

The bot reads the following environment variables:

- `DISCORD_TOKEN` – your Discord bot token.
- `DISCOURSE_URL` – base URL of the forum (`https://forum.gl-inet.com`).
- `SEARCH_LIMIT` – number of links to return (defaults to `5`).

Create a `.env` file (or supply these variables through your hosting platform) with the values:

```
DISCORD_TOKEN=your_bot_token_here
DISCOURSE_URL=https://forum.gl-inet.com
SEARCH_LIMIT=5
```

### Local Development

1. Clone this repository and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the bot using Python:

   ```bash
   python bot.py
   ```

### Docker

A sample `Dockerfile` is provided for containerized deployments. Build the image and run it with your environment variables:

```bash
# Build
docker build -t discord-discourse .

# Run (replace values as needed)
docker run -e DISCORD_TOKEN=your_bot_token \
           -e DISCOURSE_URL=https://forum.gl-inet.com \
           -e SEARCH_LIMIT=5 discord-discourse
```

## Usage

Once the bot is running in your Discord server, use the command below to search the forum:

```
!search <keywords>
```

The bot replies with up to five links that best match your query.

## Additional Notes

- The search functionality relies on the `search.json` endpoint of the forum's Discourse instance. Rate limiting and access rules are determined by the forum's administrators.
- For production deployments, consider implementing caching to reduce requests to the forum.
- The code is intentionally simple and can be extended with additional features such as link previews or automatic trending topics.

## License

This project is released under the [MIT License](LICENSE).

=======
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
