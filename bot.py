import os
import discord
import requests
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

SEARCH_URL = 'https://forum.gl-inet.com/search.json'

@bot.command(name='search')
async def search(ctx, *, query: str):
    """Search the GL.iNet forum and return top 5 results."""
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
        url = f'https://forum.gl-inet.com/t/{slug}/{id_}'
        results.append(f'{title} - {url}')

    if results:
        await ctx.send('\n'.join(results))
    else:
        await ctx.send('No results found.')

bot.run(TOKEN)
