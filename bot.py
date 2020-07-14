# bot.py
import os
import random

import source.bot_commands as bot_commands

import discord
from discord.ext import commands
from dotenv import load_dotenv
from source.utils import fetchImage

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot Running!")

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='standings-all', help='Displays standings with all details')
async def standingsAll(ctx, arg=''):
    text = bot_commands.getStandings(arg, mode='all')
    await ctx.send(text)

@bot.command(name='standings', help='Display Standings with only Matches played & points')
async def standings(ctx, arg=''):
    text = bot_commands.getStandings(arg, mode='long')
    await ctx.send(text)

@bot.command(name='fixtures')
async def fixtures(ctx, code='', limit=5):
    embed = bot_commands.getFixtures(code, limit)
    path = fetchImage(code)
    if path is not None:
        embed.set_thumbnail(url='attachment://image.jpg')
        embed.set_footer(text='Requested By: ' + str(ctx.author))
        await ctx.send(embed=embed, file=discord.File(path, 'image.jpg'))
    else:
        await ctx.send(embed=embed)

@bot.command(name='help')
async def help(ctx):
    helpEmbed = bot_commands.getHelpEmbed(ctx)
    await ctx.send(embed=helpEmbed)

bot.run(TOKEN)