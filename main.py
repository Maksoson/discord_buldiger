import discord
import asyncio
from config import *

client = discord.Client()


async def task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id=CHANNEL_ID)
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, counter)
        await asyncio.sleep(60)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.loop.create_task(task())
client.run(TOKEN)

# from discord.ext import commands
#
# bot = commands.Bot(command_prefix='>')
#
#
# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')
#
#
# @bot.command()
# async def ping(ctx: commands.Context):
#     await ctx.send('Pong!')
#
#
# bot.run(TOKEN)
