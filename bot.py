import discord
import asyncio
import os
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Constant
client_token = os.environ.get('DISCORD_TOKEN')
# Set's the bot's description and prexix to any command
client = Bot(description='Hello!', command_prefix='?', pm_help=True)

# main function that handles commands
def main(): 
	@client.event

	async def on_ready(): 
		print('Github link: https://github.com/ZachLynch123/discordbot')





if __name__ == '__main__':
	client.run(client_token)

