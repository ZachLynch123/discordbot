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
client = Bot(description='Hello!', command_prefix='-', pm_help=False)
# main function that handles commands
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('')
	print('--------')
	print('')
	print('')
	print('--------')
	print('')

@client.event
async def on_message(message): 
	if message.content.startswith('-random'): 
		url_list = []
		i = 0
		items = imgur.gallery()
		for item in items: 
			url_list.append(item.link)
			i = i +1
		await client.send_message(message.channel, random.choice(url_list))

@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")


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

