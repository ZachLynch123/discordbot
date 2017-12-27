import discord
import asyncio
import os
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
from imgurpython import ImgurClient
import pdb

# Constant
client_token = os.environ.get('DISCORD_TOKEN')
imgur_id = os.environ.get('IMGUR_ID')
imgur_secret = os.environ.get('IMGUR_SECRET')
imgur = ImgurClient(imgur_id, imgur_secret)
# Set's the bot's description and prexix to any command
client = Bot(description='Hello!', command_prefix='$', pm_help=False)
# main function that handles commands

# if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
 #    discord.opus.load_opus('opus')
#     print('opus')


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-------')

# @client.command(pass_context=True)
# async def ping(ctx): 
#	await client.say(":ping_pong: pong!")

@client.event
async def on_message(message): 
	if message.content.startswith('random'): 
		url_list = []
		items = imgur.gallery()
		i = 0
		for item in items:
			url_list.append(item.link) 
			i = i + 1
		print(url_list)
		await client.send_message(random.choice(url_list))

#async def random(): 
#	url_list = []
#	i = 0
#	items = imgur.gallery()
#	for item in items: 
#		url_list.append(item.link)
#		i = i + 1
#
#	imglink = random.choice(url_list)
#	await client.say((random.choice(url_list)))

client.run(client_token)

