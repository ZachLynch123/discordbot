import discord
import asyncio
import os
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Constant
client_token = os.environ.get('DISCORD_TOKEN')

client = Bot(description='Hello!', command_prefix='?', pm_help=True)
def main(): 

	client = Bot(description='Hey all! Im the best!', command_prefix='?', pm_help=True)

	@client.event

	async def on_ready(): 
		print('Github link: https://github.com/ZachLynch123/discordbot')





if __name__ == '__main__':
	client.run(client_token)

