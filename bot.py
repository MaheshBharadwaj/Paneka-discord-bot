# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
from test import getStandings

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

@bot.command(name='standings', help='Display Standings with only Matches played & points')
async def standings(ctx, arg=''):
    text = getStandings(arg, mode='long')
    await ctx.send(text)


@bot.command(name='help')
async def help(ctx):
    embed=discord.Embed(title="Paneka-Help!", description="Shows available commands and their functions", color=0xf58300)
    embed.set_thumbnail(url="https://img.icons8.com/fluent/144/000000/get-help.png")
    embed.add_field(name=":exclamation: standings-all [PL or SPA or SA]", value="   Detailed Standings, with team codes", inline=False)
    embed.add_field(name=":exclamation: standings [PL or SPA or SA]", value="   Display Standings", inline=False)
    embed.set_footer(text='Requested by ' + str(ctx.author))
    await ctx.send(embed=embed)

bot.run(TOKEN)