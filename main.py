import asyncio
import discord
import time
import random
import datetime
import os

app = discord.Client()
##test token
token = "NTYyODkzNDA3MDIyODc0NjU0.XKRZXQ.TbDAucqRpmN36RqVkny8WLOS3ZE"

@app.event
async def on_ready():
    print("MercuryBot by Team Hermes!")
    print("=============")

    await app.change_presence(game=discord.Game(name="MercuryBot", type=0))

@app.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "!도움":
        await app.send_message(message.channel, "!도움\n어찌구\n저찌구\n쏼라\n쏼라")
    
    elif message.content == "!정보":
        await app.send_message(message.channel, "MercuryBot Server Version :\nv0.1\n\nMercury Bot은 Team Hermes(팀 헤르메스)가 개발한\ndiscord.py 봇입니다.")

    elif message.content == "!며칠":
        now = datetime.datetime.now()
        await app.send_message(message.channel, random.choice(["귀찮아", "저리가", str(now.day)+"일임."]))

app.run(token)
