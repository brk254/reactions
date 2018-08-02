import discord, random

# Secret token corresponding to brobot
token = "NDU2MTAzODIwOTMwMzE4MzM5.DkSzow.m8CV2UflqLEs1jHHDaxZ_O2UBHg"

client = discord.Client()


@client.event
async def on_message(message):
	# we d on ot want the bot to reply to itself
	if message.author == client.user:
		return
	if message.content.startswith('?hello'):
		msg = "Hello {0.author.mention}".format(message)
		await client.send_message(message.channel, msg)

# add some disapprovals
	if message.content.startswith("?face"):
		face_file = open("face_pics")
		facelist = face_file.readlines()
		msg = random.choice(facelist).format(message)
		await client.send_message(message.channel, msg)
		face_file.close()
	if message.content.startswith("?addface"):
		new_image_url = message.content[9:]
		face_append = open("face_pics", "a")
		face_append.write("\n" + new_image_url)
		face_append.close()
		msg = "Thank you {0.author.mention}. Your reaction has been added.".format(message)
		await client.send_message(message.channel, msg)

# Add some angry faces
	if message.content.startswith("?angry"):
		face_file = open("angry_faces")
		facelist = face_file.readlines()
		msg = random.choice(facelist).format(message)
		await client.send_message(message.channel, msg)
		face_file.close()
	if message.content.startswith("?addangry"):
		new_image_url = message.content[10:]
		face_append = open("angry_faces", "a")
		face_append.write("\n" + new_image_ur)
		face_append.close()
		msg = "Thank you {0.author.mention}. Your reaction has been added.".format(message)
		await client.send_message(message.channel, msg)

# Add some shocked faces
	if message.content.startswith("?shocked"):
		face_file = open("shocked_faces")
		facelist = face_file.readlines()
		msg = random.choice(facelist).format(message)
		await client.send_message(message.channel, msg)
		face_file.close()
	if message.content.startswith("?addshocked"):
		new_image_url = message.content[12:]
		face_append = open("shocked_faces", "a")
		face_append.write("\n" + new_image_url)
		face_append.close()
		msg = "Thank you {0.author.mention}. Your reaction has been added.".format(message)
		await client.send_message(message.channel, msg)

# Add some disgusted faces
	if message.content.startswith("?disgust"):
		face_file = open("disgusted_faces")
		facelist = face_file.readlines()
		msg = random.choice(facelist).format(message)
		await client.send_message(message.channel, msg)
		face_file.close()
	if message.content.startswith("?adddisgusted"):
		new_image_url = message.content[14:]
		face_append = open("disgusted_faces", "a")
		face_append.write("\n" + new_image_url)
		face_append.close()
		msg = "Thank you {0.author.mention}. Your reaction has been added.".format(message)
		await client.send_message(message.channel, msg)

# Add some laughter faces
	if message.content.startswith("?laughter"):
		face_file = open("laughter_faces")
		facelist = face_file.readlines()
		msg = random.choice(facelist).format(message)
		await client.send_message(message.channel, msg)
		face_file.close()
	if message.content.startswith("?addlaughter"):
		new_image_url = message.content[13:]
		face_append = open("laughter_faces", "a")
		face_append.write("\n" + new_image_url)
		face_append.close()
		msg = "Thank you {0.author.mention}. Your reaction has been added.".format(message)
		await client.send_message(message.channel, msg)

	if message.content.startswith("Okay, bot's going down for now."):
		msg = "NO, WAIT!".format(message)
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("------")

client.run(token)
