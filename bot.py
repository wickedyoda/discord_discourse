import os
import discord
import requests
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN environment variable not set")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

BASE_URL = os.getenv("DISCOURSE_BASE_URL", "https://forum.gl-inet.com").rstrip("/")
SEARCH_URL = f"{BASE_URL}/search.json"

@bot.command(name='search')
async def search(ctx, *, query: str):
    """Search the configured Discourse forum and return top 5 results."""
    params = {'q': query}
    try:
        r = requests.get(SEARCH_URL, params=params)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        await ctx.send('Error fetching results: %s' % e)
        return

    topics = data.get('topics', [])
    results = []
    for topic in topics[:5]:
        title = topic.get('title')
        slug = topic.get('slug')
        id_ = topic.get('id')
        url = f"{BASE_URL}/t/{slug}/{id_}"
        results.append(f'{title} - {url}')

    if results:
        await ctx.send('\n'.join(results))
    else:
        await ctx.send('No results found.')

bot.run(TOKEN)
