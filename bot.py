import discord
from discord.ext import commands

import random

TOKEN = 'PUT YOUR BOT_TOKEN HERE'

description = '''Python Discord Bot'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, welcome!")

@bot.command()
async def rollthedice(ctx):
    await ctx.send(random.randint(1, 6))

bot.run(TOKEN)


