import discord
import asyncio
from config import *

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    id = client.get_guild(CHANNEL_ID)
    channels = [""]

    if message.content.find("!hello") != -1:
        await message.channel.send("Hi, " + message.author.id)
    elif message.content == "!users":
        await message.channel.send(f"""In {id.name} - {id.member_count} Members\nOwner is {id.owner_id}""")

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
