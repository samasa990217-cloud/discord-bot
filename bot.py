import discord
from discord.ext import commands
from discord import app_commands
import os
import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

VERIFIED_ROLE_ID = 1442916731927396403
BUYERS_ROLE_ID = 1442915193704157235
TRADE_CATEGORY_ID = 123456789012345678
WAIT_TIME = 60
LOG_FOLDER = "trade_logs"

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        await bot.tree.sync()
        print("Slash commands synced.")
    except Exception as e:
        print(e)

# 這裡可貼前面完整 bot.py 內容
bot.run("你的TOKEN")
