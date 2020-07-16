import discord
import requests
import json
import os

from dotenv import load_dotenv
from source.utils import putTableAll, putTableLong,putFixtures,fetchJSON
from source.league_code import LEAGUE_CODE
from source.team_id import TEAM_ID
from source.exceptions import *


def getStandings(code, mode='long'):
    """
    Function that delivers standings in text format.
    Queries the cache for the requested data, if not found,
    Loads the data from API and caches it

    Parameters:
    -----------
    code: str
        The ID of the league for which standings are required
    mode: 'long' or 'all', optional
        * defaults to 'long'
        * 'long' -> SNO, Team name, Matches Played, Points Obtained
        * 'all'  -> SNO, Team Code, Matches Played, Won, Drawn, Lost, Pts, Goal Difference

    Returns:
    --------
    str
        standings if code is valid, or an error message

    """

    try:
        if code not in LEAGUE_CODE:
            raise InvalidLeagueCodeException

        obj = fetchJSON(code, 'standings')
        if mode == 'all':
            return putTableAll(obj)
        return putTableLong(obj)
                
    except InvalidLeagueCodeException:
        return None


def getFixtures(code, limit: int, mode):
    """
    Displays the fixtures in the requested league / team as an embed
    Fetches fixtures from JSON file and renders embed for it,
    Displays 'limit' matches
    
    Parameters:
    -----------
    code: str
        The ID of the league or team for which fixtures are required
    limit: int, optional
        Number of fixtures to display (default value of 5)
    mode: str ['league' or 'team']
        Whether the fixtures of a league or a team are to be rendered

    Returns:
    --------
    discord.Embed 
        Shows the fixtures as many as requested,
        Incase of invalid code, relevant help embed is returned

    """
    try:
        if limit < 0:
            raise InvalidLimitException

        if (mode == 'league' and code not in LEAGUE_CODE):
            raise InvalidLeagueCodeException
        
        if (mode == 'team' and code not in TEAM_ID):
            raise InvalidTeamCodeException

        obj = fetchJSON(code, 'fixtures')
        return putFixtures(obj, code, limit, mode)

                
    except InvalidLimitException:
        return discord.Embed(title = 'Limit must be greater than :zero:',\
                            description="Enter a valid limit :smile:",\
                            color=0xf58300 )

    except InvalidLeagueCodeException:
        return getLeagueCodes("Invalid League Code!")

    except InvalidTeamCodeException:
        return getTeamCodes("Invalid Team Code!")

def getLeagueCodes(title="League Codes"):
    """
    Returns Leagues and their codes as an Embed

    Parameters:
    -----------
    title: str, optional
        Title of the embed (by default: "League Codes")

    Returns:
    --------
    discord.Embed 
        Embed displaying league codes

    """

    embed = discord.Embed(\
                title=title,\
                description="Refer codes for Top :five: Leagues here:",\
                color=0xf58300)
    embed.add_field(name=':one: Premier League', value = 'PL' + "\n\u200b", inline=False)
    embed.add_field(name=':two: La Liga', value = 'SPA' + "\n\u200b", inline=True)
    embed.add_field(name=':three: Serie A', value = 'SA' + "\n\u200b", inline=False)
    embed.add_field(name=':four: Bundesliga', value = 'BA' + "\n\u200b", inline=True)
    embed.add_field(name=':five:Ligue 1', value = 'FL1', inline=False)
    return embed

def getTeamCodes(title="Team Codes"):
    """
    Returns Teams and their codes as an Embed

    Parameters:
    -----------
    title: str, optional
        Title of the embed (by default: "Team Codes")

    Returns:
    --------
    discord.Embed 
        Embed displaying team codes

    """

    embed = discord.Embed(\
                title=title,\
                description="Refer codes for Top :one: :zero: Teams here:",\
                color=0xf58300)
    embed.add_field(name='Real Madrid', value = 'MAD' + "\n\u200b", inline=True)
    embed.add_field(name='FC Barcelona', value = 'FCB' + "\n\u200b", inline=True)
    embed.add_field(name='Manchester United', value = 'MUFC' + "\n\u200b", inline=True)
    embed.add_field(name='Arsenal', value = 'AFC' + "\n\u200b", inline=True)
    embed.add_field(name='Bayern Munich', value = 'BAY' + "\n\u200b", inline=True)
    embed.add_field(name='Chelsea', value = 'CFC' + "\n\u200b", inline=True)
    embed.add_field(name='Juventus', value = 'JUVE' + "\n\u200b", inline=True)
    embed.add_field(name='Atletico Madrid', value = 'ATM' + "\n\u200b", inline=True)
    embed.add_field(name='Liverpool', value = 'LFC' + "\n\u200b", inline=True)
    embed.add_field(name='Manche$ter City', value = 'MCFC', inline=True)
    return embed

def getHelpEmbed(ctx):
    """
    Generates the 'Help' embed when requested

    Parameters:
    -----------
    ctx: discord.Context
        Context data passed by discord when a command is invoked

    Returns:
    --------
    discord.Embed 
        Showing help data for the commands available

    """
    embed = discord.Embed(
                title="Paneka-Help!",
                description="Shows available commands and their functions",
                color=0xf58300 )
    embed.set_thumbnail(url = "https://img.icons8.com/fluent/144/000000/get-help.png")
    embed.add_field(name = ":one: standings-all [league code]", value = "Detailed Standings, with team codes", inline=False)
    embed.add_field(name = ":two: standings [league code]", value = "Display Standings", inline=False)
    embed.add_field(name = ":three: fixtures ['league' or 'team'] [code] [limit (default: :five: )]", value = "Displays Fixtures", inline=False)
    embed.add_field(name = ":four: league-codes", value = "Displays Leagues and their Respective Codes", inline=False)
    embed.add_field(name = ":five: team-codes", value = "Displayes Teams and their Respectice Codes", inline=False)
    embed.set_footer(text='Requested By: ' + str(ctx.author))

    return embed

if __name__ == "__main__":
    print(getStandings('PL'))