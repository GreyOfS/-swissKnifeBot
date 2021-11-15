import discord
from replyHello import hello
import re
import os

sk = discord.Client()

@sk.event
async def on_ready():
	print(f"We have logged in {sk.user}\n────────────────────")

@sk.event
async def on_message(message):
	
	if message.author == sk.user:
		return

	if hello.isSay(hello, message.content):
		print(f"👤╭─{message.author.name}\n📥╰─➤ \t{message.content}\n────────────────────")
		await message.channel.send(f"Hello {message.author.mention}!")
	
	if re.compile(r'\b({0})\b'.format("never gonna give you up"), flags=re.IGNORECASE).search(message.content) != None:
			await message.channel.send(
				content = "~~https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=cameronbarnett~~",
				delete_after = 60.0
			)

sk.run(os.environ['D_TOKEN'])