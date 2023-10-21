# 導入Discord.py模組
import discord

import os
import logging.config
import yaml
from dotenv import load_dotenv
from clinet import Client

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not os.path.exists('log'):
    os.mkdir('log')

with open(file="logconfig.yaml", mode='r', encoding="utf-8") as file:
    logging_yaml = yaml.load(stream=file, Loader=yaml.FullLoader)
    logging.config.dictConfig(config=logging_yaml)

# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
client = Client(intents=intents)
client.run(TOKEN)