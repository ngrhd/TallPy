import discord
from discord.ext import commands
import logging
import bottesting as bt

logging.basicConfig(level=logging.INFO)

Client = discord.Client() #Initialise Client
client = commands.Bot(command_prefix = ".") #Initialise client bot


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Tally.ERP 9'))
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

#@client.event
#async def on_message(message):
#    if message.content == "cookie":
#        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"


@client.event
async def on_message(message):
    if message.content.startswith('.cr'):
        await client.send_message(message.channel, 'Type Party Name')
        msg = await client.wait_for_message(author=message.author)
        i_got = bt.lmao(msg.content)
        await client.send_message(message.channel, i_got)


#use the following with bottesting.py
''''@client.event
async def on_message(message):
    if message.content.startswith('.cr'):
        await client.send_message(message.channel, 'Enter anything...')
        msg = await client.wait_for_message(author=message.author)
        i_got = bt.lmao(msg.content)
        await client.send_message(message.channel, i_got)
'''


client.run("NDIxNTQ4MzgxNjE0MjQzODUw.DYO2Qw.Ld8GxHePs6WhOa0Z6MeIb3qFJYs") #Replace token with your bots token