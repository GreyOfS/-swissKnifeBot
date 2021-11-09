import discord
import os

from replyHello import hello

sk = discord.Client()

@sk.event
async def on_ready():
	print(f"We have logged in {sk.user}\n────────────────────")

@sk.event
async def on_message(message):
	
	if message.author == sk.user:
		return

	if hello.isSay(message.content):
		print(f"👤╭─{message.author.name}\n📥╰─➤ \t{message.content}\n────────────────────")
		await message.channel.send(f"Hello {message.author.mention}!")

sk.run(os.environ['D_TOKEN'])