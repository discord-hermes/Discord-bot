import asyncio
import discord
import time
import random
import datetime
import os

app = discord.Client()
##test token
token = "NjfsdiIfdsldafjiLidfvjleir20gfisvcfaskdfldf94fjlkxjapok"

@app.event
async def on_ready():
    print("MercuryBot by Team Hermes!")
    print("=============")

    await app.change_presence(game=discord.Game(name="MercuryBot", type=0))

@app.event
async def on_message(message):
    if message.author.bot:
        return None


app.run(token)
