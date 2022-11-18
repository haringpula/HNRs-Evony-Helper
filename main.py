#
# main.py created on Sat Jul 30 2022 by King Red Sanchez
# Copyright (c) 2022
# ~~~~~~~~~~~██████████████████████████REMOVE██████████████████████████~~~~~~~~~~~
# Author Naming Conventions: █ Package names are in lowercase
# Class/Interfaces names are in PascalCase █ Method/Instances names are in camelCase
# Variable names are in camelCase (typeName) █ Constants are in SNAKE_CASE
# Temporary variables names: i,j,k,m,n for int; c,d,e for char (else follow var names)
# Author Code Conventions: █ TODO: pending completion █ NOTE: notes on implementation
# BUG: valid / broken code █ XXX: bogus / working code █ FIXME: bogus / broken code
# SEE: valid / working / spaghetti code █ HACK: valid / working / temporary
# ~~~~~~~~~~███████████REMOVE IN FINAL VERSION ██ SAPERE AUDE███████████~~~~~~~~~~
#

# NOTE: Clear unused import
import os
import discord
import requests
import logging
import datetime
from discord.ext import commands, tasks
from keep_alive import keep_alive
from discord import app_commands
import discord.ext.commands.bot

# SEE: static vars to separate access file
my_secret = os.environ['token']
prefix = '/'
version = 1.8
logo = 'https://cdn.discordapp.com/attachments/968595427228286976/972125616730144778/honor2_031019-1.jpg'
github = 'https://github.com/haringpula/HNRs-Evony-Helper'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix,  intents=intents)
# Test for new slash commands
#tree = app_commands.CommandTree(bot)
activity = discord.Activity(
    name="for $help",
    type=discord.ActivityType.watching)
bot.remove_command('help')

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# XXX: fffffkin nuclear level refactoring required
# Food, Wood, Stone, Iron, Gold, Power stored in 2d lists
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


#@tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=12417128931)) 
# Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, 
# but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@bot.event
async def on_ready():
    print(f'{bot.user} is now live!')
    await bot.change_presence(activity=activity)
    #await tree.sync(guild=discord.Object(id=835899395219652671))
    if not event.is_running():
        event.start()
        print("Announcement Started")

@bot.command()
async def syncing(ctx):
    guild = ctx.guild #or discord.Object(id=835899395219652671)  
    # you can use a full discord.Guild as the method accepts a Snowflake
    bot.tree.copy_global_to(guild=guild)
    await ctx.send('Synced')


@tasks.loop(minutes=1)
async def event():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    # Create the time on which the task should always run
    midnight = datetime.time(hour=00, minute=00).strftime("%H:%M")

    if time != midnight:
        return
    channel = bot.get_channel(967433695495598150)
    # await channel.send("Event succesful")
    print("Announce Working")

# Commands test
@bot.tree.command(name='mycommand')
async def ping(ctx):
    await ctx.send('pong')
    print(f"{ctx.author} is talking to {bot.user} on {ctx.guild}")


@bot.tree.command()
async def commands(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        url='https://github.com/haringpula/HNRs-Evony-Helper',
        description='Here are the commands!',
        color=discord.Color.dark_gray())
    embed.set_thumbnail(url=logo)
    embed.add_field(name='$help', value='Show help', inline=False)
    embed.add_field(name='$commands', value='Show commands list', inline=False)
    embed.add_field(name='$time',
                    value='Show current server time/day',
                    inline=False)
    embed.add_field(name='$calc', value='Calculate Troop Costs', inline=False)
    embed.add_field(name='$mean',
                    value='Give Evony abbreviation meaning *In development*',
                    inline=False)
    embed.set_footer(
        text="Information requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)


@bot.command()
async def time(ctx):
    now = datetime.datetime.now()
    day_name = now.strftime("%A")
    time = now.strftime("%H:%M:%S")
    day_full = now.strftime("%b-%d-%Y")
    embed = discord.Embed(
        title='Current Server Day/Time',
        url='https://github.com/haringpula/HNRs-Evony-Helper',
        description="The server is on {}, {} at {}".format(
            day_name, day_full, time),
        color=discord.Color.dark_gray())
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=logo)
    embed.set_footer(
        text="Information requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
    del now
    del day_full
    del day_name
    del time


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='[HNR] Evony Bot',
        url='https://github.com/haringpula/HNRs-Evony-Helper',
        description='**Evony TKR Discord Helper Bot!**',
        color=discord.Color.dark_gray())
    embed.set_author(name="**For Evony The Kings Return**",
                     icon_url=bot.user.avatar_url)
    embed.set_thumbnail(url=logo)
    embed.add_field(name='`$commands`',
                    value='To show commands list',
                    inline=False)
    embed.add_field(name='Server Time',
                    value='Get the current server time/day in Evony',
                    inline=True)
    embed.add_field(name='Troop Calculator',
                    value='Calculate rasources needed for troops',
                    inline=True)
    embed.set_footer(
        text="Made by:\nharingpula <@645255797340766218>\nLordickenstein <@756084838154633237>"
    )
    await ctx.send(embed=embed)


@bot.command()
async def calc(ctx, *args):
    if len(args) != 3:
        await ctx.send('Usage: `$calc TroopType TroopTier TroopNum`')
        await ctx.send(
            'Troop Type: (M=Mounted, G=Ground, R=Ranged, S=Siege)\nTroop Tier: (1-15)\nTroop Number: How Many Troops you want'
        )
        return
    type = args[0].upper()
    tier = int(args[1])
    num = int(args[2])
    if (type not in ['M', 'G', 'R', 'S']):
        await ctx.send('**Invalid Troop Type**')
        return
    if (tier < 1) or (tier > 15):
        await ctx.send('**Invalid Troop Tier**')
        return
    if (num < 1):
        await ctx.send('**Invalid Troop Amount**')
        return
    if type == 'M':
        food = num * M[tier - 1][0]
        wood = num * M[tier - 1][1]
        stone = num * M[tier - 1][2]
        iron = num * M[tier - 1][3]
        gold = num * M[tier - 1][4]
        power = num * M[tier - 1][5]
    if type == 'G':
        food = num * G[tier - 1][0]
        wood = num * G[tier - 1][1]
        stone = num * G[tier - 1][2]
        iron = num * G[tier - 1][3]
        gold = num * G[tier - 1][4]
        power = num * G[tier - 1][5]
    if type == 'R':
        food = num * R[tier - 1][0]
        wood = num * R[tier - 1][1]
        stone = num * R[tier - 1][2]
        iron = num * R[tier - 1][3]
        gold = num * R[tier - 1][4]
        power = num * R[tier - 1][5]
    if type == 'S':
        food = num * S[tier - 1][0]
        wood = num * S[tier - 1][1]
        stone = num * S[tier - 1][2]
        iron = num * S[tier - 1][3]
        gold = num * S[tier - 1][4]
        power = num * S[tier - 1][5]
    embed = discord.Embed(
        title='Troop Calculator',
        url='https://github.com/haringpula/HNRs-Evony-Helper',
        description='Hey <@{}>, here is your Troop Calculation!'.
        format(ctx.author.id),
        color=discord.Color.dark_gray())
    embed.set_thumbnail(url=logo)
    embed.add_field(
        name='Input',
        value='Troop Type = {}\nTroop Tier = {}\nTroop Amount = {}'.
        format(type, tier, num),
        inline=True)
    embed.add_field(
        name='Output',
        value='Food = {}\nWood = {}\nStone = {}\nIron = {}\nGold = {}\nPower Increase: {}'
        .format(food, wood, stone, iron, gold, power),
        inline=True)
    embed.set_footer(text="Information requested by: {}".format(
        ctx.author.display_name))
    await ctx.send(embed=embed)
    del type
    del tier
    del num
    del food
    del wood
    del stone
    del iron
    del gold
    del power


# TODO dictionary
@bot.command()
async def mean(ctx):
    await ctx.send('**This command is still in development**')


# Catching Discord Rate Limits
try:
    bot.run(my_secret)
    # Web Server to keep bot online
    keep_alive()
except discord.errors.HTTPException:
    r = requests.head(url="https://discord.com/api/v1")
    try:
        print(
            f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left. Global: {r.headers['Global']}")
    except:
        print("Rate limit error")
    print("\nBlocked by Rate Limits\nRestart now...\n")
