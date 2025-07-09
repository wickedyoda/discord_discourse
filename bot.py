import discord
from discord.ext import commands
from discord import app_commands
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# Forum search function
def search_forum(query):
    url = f"https://forum.glinet.net/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.select('.topic-title')
    top_links = []
    for result in results[:5]:
        link = result.get('href')
        if link:
            top_links.append(f"https://forum.glinet.net{link}")
    return top_links if top_links else ["No results found."]

# Slash command
@tree.command(name="search", description="Search GL.iNet Forum")
@app_commands.describe(query="Enter search keywords")
async def search_slash(interaction: discord.Interaction, query: str):
    await interaction.response.defer()
    results = search_forum(query)
    await interaction.followup.send("\n".join(results), ephemeral=False)  # public reply

# Prefix-based command
@bot.command(name="search")
async def search_prefix(ctx, *, query: str):
    await ctx.send("🔍 Searching forum...")
    results = search_forum(query)
    await ctx.send("\n".join(results))

# Sync and launch
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await tree.sync(guild=guild)
        print(f"Synced {len(synced)} command(s) to the guild.")
    except Exception as e:
        print("Failed to sync slash commands:", e)

@bot.event
async def on_ready():
    try:
        synced = await tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"✅ Synced {len(synced)} command(s) to guild ID {GUILD_ID}")
    except Exception as e:
        print("❌ Failed to sync slash commands:", e)

bot.run(TOKEN)