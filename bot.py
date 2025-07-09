import discord
from discord.ext import commands
from discord import app_commands
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

# Set intents and bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree
guild = discord.Object(id=GUILD_ID)

# Search the GL.iNet forum
def search_forum(query):
    url = f"https://forum.gl-inet.com/search.json?q={query}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        results = data.get("topics", [])
        top_links = []
        for topic in results[:5]:
            topic_id = topic.get("id")
            slug = topic.get("slug")
            if topic_id and slug:
                top_links.append(f"https://forum.gl-inet.com/t/{slug}/{topic_id}")
        return top_links if top_links else ["No results found."]
    except Exception as e:
        print(f"Error searching forum: {e}")
        return ["❌ Failed to fetch results."]

# Slash command (must be defined before on_ready)
@tree.command(name="search", description="Search GL.iNet Forum", guild=guild)
@app_commands.describe(query="Enter search keywords")
async def search_slash(interaction: discord.Interaction, query: str):
    await interaction.response.defer()
    results = search_forum(query)
    await interaction.followup.send("\n".join(results), ephemeral=False)

# Optional: Classic prefix-based command
@bot.command(name="search")
async def search_prefix(ctx, *, query: str):
    await ctx.send("🔍 Searching forum...")
    results = search_forum(query)
    await ctx.send("\n".join(results))

# Ready event: sync commands
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await tree.sync(guild=guild)
        print(f"✅ Synced {len(synced)} command(s) to guild ID {GUILD_ID}")
    except Exception as e:
        print("❌ Failed to sync slash commands:", e)

# Run the bot
bot.run(TOKEN)