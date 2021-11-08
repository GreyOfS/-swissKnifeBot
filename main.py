import discord
import os

from replyHello import isSayHello

sk = discord.Client()

@sk.event
async def on_ready():
	print(f"We have logged in {sk.user}")

@sk.event
async def on_message(message):
	
	if message.author == sk.user:
		return

	if isSayHello(message.content):
		print(f"{message.author.name}\n╰─➤\t{message.content}")
		await message.channel.send(f"Hello {message.author.mention}!")

sk.run(os.environ['D_TOKEN'])