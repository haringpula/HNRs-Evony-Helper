import os
import discord
import requests
from datetime import datetime
from discord.ext import commands
from keep_alive import keep_alive

my_secret = os.environ['token']
prefix = '$'
version = 1.1
logo = 'https://cdn.discordapp.com/attachments/968595427228286976/972125616730144778/honor2_031019-1.jpg'
github='https://github.com/haringpula/HNRs-Evony-Helper'
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

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


# Commands test
@client.command()
async def ping(ctx):
    await ctx.send('pong')
    print(f"{ctx.author} is talking to {client.user} on {ctx.guild}")


# View commands list
@client.command()
async def commands(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        url='https://github.com/haringpula/HNRs-Evony-Helper',
        description='Here are the commands!',
        color=discord.Color.dark_gray()
    )
    embed.set_author(
        name=ctx.author.display_name,                    
        icon_url=ctx.author.avatar_url
    )
    embed.set_thumbnail(url=logo)
    embed.add_field(
        name='$help',
        value='Show help',
        inline=False
    )
    embed.add_field(
        name='$commands',
        value='Show commands list',
        inline=False
    )
    embed.add_field(
        name='$calc',
        value='Calculate Troop Costs',
        inline=False
    )
    embed.add_field(
        name='$mean',
        value='Give Evony abbreviation meaning',
        inline=False
    )
    embed.add_field(
        name='$new',
        value="See what's in the new version",
        inline=False
    )
    embed.add_field(
        name='$about',
        value='Learn more about me!',
        inline=False
    )
    embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

# Commands test
@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        description='Welcome to help section. Here are the commands'

    )
    embed.set_thumbnail(url=logo)
    embed.add_field(
        name='$help',
        value='List this help',
        inline=True
    )
    await ctx.send(embed=embed)
    await ctx.send(f"Hi <@{ctx.author.id}>! I'm [HNR]Honor Alliance's Evony TKR Helper Bot v{version}!")
    await ctx.send("Commands!\n`$help` - Show help\n`$commands` - Show commands list\n`$calc` - Calculate Troop Cost\n`$mean` - Give Evony abbreviation meaning (**In Development**)\n`$new` - See what's new in this version\n`$about` - Learn more about me!")
    await ctx.send('For more information, contact my creator on <@645255797340766218> or on haringpula#1414')

  
@client.command()
async def calc(ctx, *args):
    '''
        Calculates Troop Cost
    '''
    if len(args) != 3:
        await ctx.send('Usage: `$calc TroopType TroopTier TroopNum`')
        await ctx.send('Troop Type: (M=Mounted, G=Ground, R=Ranged, S=Siege)\nTroop Tier: (1-15)\nTroop Number: How Many Troops you want')
    else:
        type = args[0].upper()
        tier = int(args[1])
        num = int(args[2])
        if (type not in ['M', 'G', 'R', 'S']):
            await ctx.send('Invalid Troop Type')
        elif (tier < 1) or (tier > 15):
            await ctx.send('Invalid Troop Tier')
        elif (num < 1):
            await ctx.send('Invalid Troop Amount')
        else:
            if type == 'M':
                food = num * M[tier - 1][0]
                wood = num * M[tier - 1][1]
                stone = num * M[tier - 1][2]
                iron = num * M[tier - 1][3]
                gold = num * M[tier - 1][4]
                power = num * M[tier - 1][5]
            elif type == 'G':
                food = num * G[tier - 1][0]
                wood = num * G[tier - 1][1]
                stone = num * G[tier - 1][2]
                iron = num * G[tier - 1][3]
                gold = num * G[tier - 1][4]
                power = num * G[tier - 1][5]
            elif type == 'R':
                food = num * R[tier - 1][0]
                wood = num * R[tier - 1][1]
                stone = num * R[tier - 1][2]
                iron = num * R[tier - 1][3]
                gold = num * R[tier - 1][4]
                power = num * R[tier - 1][5]
            elif type == 'S':
                food = num * S[tier - 1][0]
                wood = num * S[tier - 1][1]
                stone = num * S[tier - 1][2]
                iron = num * S[tier - 1][3]
                gold = num * S[tier - 1][4]
                power = num * S[tier - 1][5]
            await ctx.send(f'Hey <@{ctx.author.id}>, here is your Troop Calculation!')
            await ctx.send(f'Food = {food}\nWood = {wood}\nStone = {stone}\nIron = {iron}\nGold = {gold}\nPower Increase: {power}')

# TODO
@client.command()
async def mean(ctx):
    await ctx.send('**This command is still in development**')

# TODO
@client.command()
async def new(ctx):
    await ctx.send('**This command is still in development**')
  
# TODO Link self and github repo, about
@client.command()
async def about(ctx):
    await ctx.send('For more information, contact my creator on <@645255797340766218> or on haringpula#1414')


try:
    # Web Server to keep bot online
    #keep_alive()
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
