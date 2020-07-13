# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
from source.bot_commands import *

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
    text = getStandings(arg, mode='all')
    await ctx.send(text)

@bot.command(name='standizngs', help='Display Standings with only Matches played & points')
async def standings(ctx, arg=''):
    text = getStandings(arg, mode='long')
    await ctx.send(text)


@bot.command(name='help')
async def help(ctx):
    helpEmbed = getHelpEmbed(ctx)
    await ctx.send(embed=helpEmbed)

bot.run(TOKEN)