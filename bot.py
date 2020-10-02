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

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Bot Running!")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=".help on " + str(len(bot.guilds)) + " server(s)")
    )


@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            helpEmbed = bot_commands.getHelpEmbed()
            await channel.send('Hey There! Just got added to this channel!\
                \nBasic commands are listed below :)', embed=helpEmbed)
            break


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Cool. Cool cool cool cool cool cool cool,\
        \nno doubt no doubt no doubt no doubt.',
        'If I die, turn my tweets into a book',
        'Captain Wuntch. Good to see you. But if you’re here, who’s guarding Hades?',
        'Anyone over the age of six celebrating a birthday should go to hell.'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

# Requires admin
@bot.command(name='update')
async def update(ctx, message = None):
    if ctx.message.author.id == 694128831291981844:
        for guild in bot.guilds:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    helpEmbed = bot_commands.getHelpEmbed()
                    await channel.send(message, embed=helpEmbed)
                    break
            

@bot.command(name='standings-all', help='Displays standings with all details')
async def standingsAll(ctx, arg=''):
    text = bot_commands.getStandings(arg.upper(), mode='all')
    if text is not None:
        await ctx.send(text)
    else:
        leagueCodeEmbed = bot_commands.getLeagueCodes(
            'Invalid League Code Entered!')
        await ctx.send(embed=leagueCodeEmbed)


@bot.command(name='standings', help='Display Standings with only Matches played & points')
async def standings(ctx, arg=''):
    text = bot_commands.getStandings(arg.upper(), mode='long')
    if text is not None:
        await ctx.send(text)
    else:
        leagueCodeEmbed = bot_commands.getLeagueCodes(
            'Invalid League Code Entered!')
        await ctx.send(embed=leagueCodeEmbed)


@bot.command(name='fixtures', alias=['matches', 'm', 'f'])
async def fixtures(ctx, code = '', limit=5):
    fixturesEmbed = bot_commands.getFixtures(code.upper(), limit)
    fixturesEmbed.set_footer(text='Requested By: ' + str(ctx.author))

    path = fetchImage(code.upper())
    if path is not None:
        fixturesEmbed.set_thumbnail(url='attachment://image.jpg')
        await ctx.send(embed=fixturesEmbed, file=discord.File(path, 'image.jpg'))
    else:
        await ctx.send(embed=fixturesEmbed)

@bot.command(name='live', aliases=['l'])
async def matches(ctx, code='', limit=5):
    liveMatchesEmbed = bot_commands.getMatches(code.upper(), limit)
    liveMatchesEmbed.set_footer(text='Requested By: ' + str(ctx.author))
  
    path = fetchImage(code.upper())
    if path is not None:
        liveMatchesEmbed.set_thumbnail(url='attachment://image.jpg')
        await ctx.send(embed=liveMatchesEmbed, file=discord.File(path, 'image.jpg'))
    else:
        await ctx.send(embed=liveMatchesEmbed)

@bot.command(name='league-codes')
async def leagueCodes(ctx):
    leagueCodesEmbed = bot_commands.getLeagueCodes()
    leagueCodesEmbed.set_footer(text='Requested By: ' + str(ctx.author))
    await ctx.send(embed=leagueCodesEmbed)

@bot.command(name='team-codes')
async def teamCodes(ctx):
    teamCodesEmbed = bot_commands.getTeamCodes()
    teamCodesEmbed.set_footer(text='Requested By: ' + str(ctx.author))
    await ctx.send(embed=teamCodesEmbed)

@bot.command(name='invite')
async def invite(ctx):
    inviteEmbed = bot_commands.getInviteEmbed(ctx)
    await ctx.author.send(embed=inviteEmbed)
    await ctx.send(f'The invite link has been sent to your DM {ctx.author.mention} :D')

@bot.command(name='help')
async def help(ctx):
    helpEmbed = bot_commands.getHelpEmbed(ctx)
    await ctx.send(embed=helpEmbed)


bot.run(TOKEN)
