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
    if text is not None:
        await ctx.send(text)
    else:
        leagueCodeEmbed = bot_commands.getLeagueCodes('Invalid League Code Entered!')
        await ctx.send(embed=leagueCodeEmbed)

@bot.command(name='standings', help='Display Standings with only Matches played & points')
async def standings(ctx, arg=''):
    text = bot_commands.getStandings(arg, mode='long')
    if text is not None:
        await ctx.send(text)
    else:
        leagueCodeEmbed = bot_commands.getLeagueCodes('Invalid League Code Entered!')
        await ctx.send(embed=leagueCodeEmbed)


@bot.group(name='fixtures')
async def fixtures(ctx):
    if ctx.invoked_subcommand is None:
        helpEmbed = bot_commands.getHelpEmbed(ctx)
        await ctx.send('Invalid Usage!\nLook at usage here:', embed=helpEmbed)

@fixtures.command(name='league')
async def league(ctx, code='', limit=5):
    fixturesEmbed = bot_commands.getFixtures(code, limit,mode='league')
    path = fetchImage(code)
    if path is not None:
        fixturesEmbed.set_thumbnail(url='attachment://image.jpg')
        fixturesEmbed.set_footer(text='Requested By: ' + str(ctx.author))
        await ctx.send(embed=fixturesEmbed, file=discord.File(path, 'image.jpg'))
    else:
        await ctx.send(embed=fixturesEmbed)

@fixtures.command(name='team')
async def team(ctx, code='', limit=5):
    fixturesEmbed = bot_commands.getFixtures(code, limit, mode='team')
    await ctx.send(embed=fixturesEmbed)


@bot.command(name='league-codes')
async def leagueCodes(ctx):
    leagueCodesEmbed = bot_commands.getLeagueCodes()
    await ctx.send(embed=leagueCodesEmbed)


@bot.command(name='team-codes')
async def teamCodes(ctx):
    teamCodesEmbed = bot_commands.getTeamCodes()
    await ctx.send(embed=teamCodesEmbed)

@bot.command(name='help')
async def help(ctx):
    helpEmbed = bot_commands.getHelpEmbed(ctx)
    await ctx.send(embed=helpEmbed)

bot.run(TOKEN)