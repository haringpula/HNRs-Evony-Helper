import os
import discord
import requests
from datetime import datetime
from discord.ext import commands
from keep_alive import keep_alive

my_secret = os.environ['token']

#client = commands.Bot(command_prefix='$')

client = discord.Client()

version = 1.1

now = datetime.now()
time = now.strftime("%H:%M:%S")
#print(time)

#Food, Wood, Stone, Iron, Gold, Power
M = [[80, 80, 0, 0, 0, 2], [130, 130, 0, 0, 0, 2.7], [200, 200, 0, 0, 0, 3.65],
     [220, 220, 0, 120, 0, 4.92], [240, 240, 0, 260, 0, 6.64],
     [260, 260, 0, 580, 0, 8.97], [300, 300, 0, 900, 0, 12.11],
     [420, 420, 0, 1300, 0, 16.34], [600, 600, 0, 1800, 0, 22.06],
     [850, 850, 0, 2500, 0, 29.79], [1300, 1300, 0, 3900, 0, 35.75],
     [2000, 2000, 0, 6000, 0, 53.63], [3000, 3000, 0, 9000, 0, 81],
     [4500, 4500, 0, 13500, 200, 122], [7500, 7500, 0, 22500, 800, 163]]
G = [[160, 0, 0, 0, 0, 2], [220, 0, 40, 0, 0, 2.7], [320, 0, 80, 0, 0, 3.65],
     [380, 0, 120, 60, 0, 4.92], [460, 0, 160, 120, 0, 6.64],
     [660, 0, 220, 220, 0, 8.97], [900, 0, 300, 300, 0, 12.11],
     [1300, 0, 420, 420, 0, 16.34], [1800, 0, 600, 600, 0, 22.06],
     [2500, 0, 850, 850, 0, 29.79], [3900, 0, 1300, 1300, 0, 35.75],
     [6000, 0, 2000, 2000, 0, 53.63], [9000, 0, 3000, 3000, 0, 81],
     [13500, 0, 4500, 4500, 200, 122], [22500, 0, 7500, 7500, 800, 163]]
R = [[40, 120, 0, 0, 0, 2], [60, 160, 40, 0, 0, 2.7],
     [80, 240, 80, 0, 0, 3.65], [120, 320, 120, 0, 0, 4.92],
     [160, 420, 160, 0, 0, 6.64], [220, 660, 220, 0, 0, 8.97],
     [300, 900, 300, 0, 0, 12.11], [420, 1300, 420, 0, 0, 16.34],
     [600, 1800, 600, 0, 0, 22.06], [850, 2500, 850, 0, 0, 29.79],
     [1300, 3900, 1300, 0, 0, 35.75], [2000, 6000, 2000, 0, 0, 53.63],
     [3000, 9000, 3000, 0, 0, 81], [4500, 13500, 4500, 0, 200, 122],
     [7500, 22500, 7500, 0, 800, 163]]
S = [[0, 100, 60, 0, 0, 2], [0, 120, 140, 0, 0, 2.7],
     [0, 120, 280, 0, 0, 3.65], [0, 120, 320, 120, 0, 4.92],
     [0, 160, 420, 160, 0, 6.64], [0, 220, 660, 220, 0, 8.97],
     [0, 300, 900, 300, 0, 12.11], [0, 420, 1300, 420, 0, 16.34],
     [0, 600, 1800, 600, 0, 22.06], [0, 850, 2500, 850, 0, 29.79],
     [0, 1300, 3900, 1300, 0, 35.75], [0, 2000, 6000, 2000, 0, 53.63],
     [0, 3000, 9000, 3000, 0, 81], [0, 4500, 13500, 4500, 200, 122],
     [0, 7500, 22500, 7500, 800, 163]]


@client.event
async def on_ready():
    print(f'{client.user} is now live!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('pong Dev cmd do not use')
        print(
            f'{message.author} is talking to {client.user} on {message.channel}!'
        )

    if message.content.startswith('$calc'):
        query = message.content
        det = query.split()
        if len(det) != 4:
            await message.channel.send(
                'Usage: `$calc TroopType TroopTier TroopNum`')
            await message.channel.send(
                'Troop Type: (M=Mounted, G=Ground, R=Ranged, S=Siege)\nTroop Tier: (1-15)\nTroop Number: How Many Troops you want'
            )
        else:
            type = det[1].upper()
            tier = int(det[2])
            num = int(det[3])
            if (type not in ['M', 'G', 'R', 'S']):
                await message.channel.send('Invalid Troop Type')
            elif (tier < 1) or (tier > 15):
                await message.channel.send('Invalid Troop Tier')
            elif (num < 1):
                await message.channel.send('Invalid Troop Amount')
            else:
                if type == 'M':
                    food = num * M[tier - 1][0]
                    wood = num * M[tier - 1][1]
                    stone = num * M[tier - 1][2]
                    iron = num * M[tier - 1][3]
                    gold = num * M[tier - 1][4]
                    power = num * M[tier - 1][5]
                    await message.channel.send(
                        f'Hey <@{message.author.id}>, here is Troop Calculation!'
                    )
                    await message.channel.send(
                        f'Food = {food}\nWood = {wood}\nStone = {stone}\nIron = {iron}\nGold = {gold}\nPower Increase: {power}'
                    )
                elif type == 'G':
                    food = num * G[tier - 1][0]
                    wood = num * G[tier - 1][1]
                    stone = num * G[tier - 1][2]
                    iron = num * G[tier - 1][3]
                    gold = num * G[tier - 1][4]
                    power = num * G[tier - 1][5]
                    await message.channel.send(
                        f'Hey <@{message.author.id}>, here is Troop Calculation!'
                    )
                    await message.channel.send(
                        f'Food = {food}\nWood = {wood}\nStone = {stone}\nIron = {iron}\nGold = {gold}\nPower Increase: {power}'
                    )
                elif type == 'R':
                    food = num * R[tier - 1][0]
                    wood = num * R[tier - 1][1]
                    stone = num * R[tier - 1][2]
                    iron = num * R[tier - 1][3]
                    gold = num * R[tier - 1][4]
                    power = num * R[tier - 1][5]
                    await message.channel.send(
                        f'Hey <@{message.author.id}>, here is Troop Calculation!'
                    )
                    await message.channel.send(
                        f'Food = {food}\nWood = {wood}\nStone = {stone}\nIron = {iron}\nGold = {gold}\nPower Increase: {power}'
                    )
                elif type == 'S':
                    food = num * S[tier - 1][0]
                    wood = num * S[tier - 1][1]
                    stone = num * S[tier - 1][2]
                    iron = num * S[tier - 1][3]
                    gold = num * S[tier - 1][4]
                    power = num * S[tier - 1][5]
                    await message.channel.send(
                        f'Hey <@{message.author.id}>, here is Troop Calculation!'
                    )
                    await message.channel.send(
                        f'Food = {food}\nWood = {wood}\nStone = {stone}\nIron = {iron}\nGold = {gold}\nPower Increase: {power}'
                    )
                else:
                    await message.channel.send(
                        'Internal Error. Contact creator on <@645255797340766218> or on haringpula#1414'
                    )

    if message.content.startswith('$help'):
        await message.channel.send(
            f"Hi <@{message.author.id}>! I'm [HNR]Honor Alliance's Evony TKR Helper Bot v{version}!"
        )
        await message.channel.send(
            "Commands!\n`$help` - Show help\n`$commands` - Show commands list\n`$calc` - Calculate Troop Cost\n`$mean` - Give Evony abbreviation meaning (**In Development**)\n`$new` - See what's new in this version\n`$about` - Learn more about me!"
        )
        await message.channel.send(
            'For more information, contact my creator on <@645255797340766218> or on haringpula#1414'
        )

    if message.content.startswith('$commands'):
        await message.channel.send(
            "Commands!\n`$help` - Show help\n`$commands` - Show commands list\n`$calc` - Calculate Troop Cost\n`$mean` - Give Evony abbreviation meaning (**In Development**)\n`$new` - See what's new in this version\n`$about` - Learn more about me!"
        )

    if message.content.startswith('$mean'):
        await message.channel.send('**This command is still in development**')

    if message.content.startswith('$about'):
        await message.channel.send(
            'For more information, contact my creator on <@645255797340766218> or on haringpula#1414'
        )

    if message.content.startswith('$new'):
        await message.channel.send('**This command is still in development**')


# Commands test
@client.command()
async def test(ctx):
    await ctx.send('hello')


# Add commands
#client.add_command(test)

# Web Server to keep bot online
#keep_alive()

try:

    client.run(my_secret)
except discord.errors.HTTPException:
    r = requests.head(url="https://discord.com/api/v1")
    try:
        print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
    except:
        print("Rate limit error")
    print("\nBlocked by Rate Limits\nRestarting now...\n")
    os.system("python restarter.py")
    os.system('kill 1')
