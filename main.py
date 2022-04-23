import os
import discord
from datetime import datetime
from replit import db
from keep_alive import keep_alive

my_secret = os.environ['token']

client = discord.Client()

now = datetime.now()
time = now.strftime("%H:%M:%S")
print(time)

@client.event
async def on_ready():
  print(f'{client.user} is now live!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$ping'):
    await message.channel.send('pong')
    print(f'{message.author} is talking to {client.user}!')


# Web Server to keep bot online
#keep_alive()
client.run(my_secret)