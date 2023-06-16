import discord

# TODO: put token
TOKEN = ""

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)


@client.event
async def on_ready():
	print("Logged in")


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("!run"):
		# TODO: file name with chats
		with open("!!!FILE PATH", "r", encoding='utf-8') as f:
			for line in f:
				await message.channel.send(line.strip())


client.run(TOKEN)