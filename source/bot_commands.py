import discord
import requests
import json
import os
import datetime as dt

from dotenv import load_dotenv
from source.utils import putTableAll, putTableLong
from source.league_code import LEAGUE_CODE


def getStandings(code, mode='long'):
    """
    Function that delivers standings in text format.
    Queries the cache for the requested data, if not found,
    Loads the data from API and caches it
    """
    load_dotenv()

    API_KEY = os.getenv('API_KEY')
    headers = {'X-Auth-Token': str(API_KEY)}

    try:
        assert(mode in ['long', 'all'])
        leagueName = code

        if leagueName not in LEAGUE_CODE:
            return "```diff\n- Please Check the league code!\
                    \n  PL  - Premier League\
                    \n  SPA - La Liga\
                    \n  SA  - Serie A\
                    \n  BL  - Bundesliga\
                    \n  FL1 - Ligue One```"
        else:
            id = LEAGUE_CODE.get(leagueName)

            #Checking Cache
            if os.path.exists(f"cache/{leagueName}.json"):
                print('Reading from cache :D')
                with open(f"cache/{leagueName}.json", 'r') as cacheData:
                    obj = json.load(cacheData)
                    if mode == 'all':
                        return putTableAll(obj)
                    return putTableLong(obj)
            else:

                #Fetching data from API
                r = requests.get(f"https://api.football-data.org/v2/competitions/{id}/standings", headers=headers)
                obj = r.json()

                #Writing data to cache
                with open(f"cache/{leagueName}.json", 'w') as cachedata:
                    json.dump(obj, cachedata, indent=4)

                if mode == 'all':
                    return putTableAll(obj)
                return putTableLong(obj)
                
    except AssertionError:
        return '```diff\n- Invalid Args passed!```'


def getHelpEmbed(ctx):
    """
    Generates the Help embed when
    """
    embed = discord.Embed(
                title="Paneka-Help!",
                description="Shows available commands and their functions",
                color=0xf58300 )
    embed.set_thumbnail(url = "https://img.icons8.com/fluent/144/000000/get-help.png")
    embed.add_field(name = ":exclamation: standings-all [league]", value = "Detailed Standings, with team codes", inline=False)
    embed.add_field(name = ":exclamation: standings [league]", value = "Display Standings", inline=False)
    embed.add_field(name = ":exclamation: fixtures [league] [limit (default: 5)]", value = "Displays Fixtures in League", inline=False)
    embed.set_footer(text='Requested By: ' + str(ctx.author))

    return embed



def getFixtures(code, limit: int):
    """
    Displays the fixtures in the requested league as an embed
    Fetches fixtures from JSON file and renders embed for it,
    Displays 'limit' matches
    """
    load_dotenv()

    API_KEY = os.getenv('API_KEY')
    headers = {'X-Auth-Token': str(API_KEY)}

    try:
        assert(limit > 0)

        leagueName = code

        if leagueName not in LEAGUE_CODE:
            embed = discord.Embed(\
                title="Invalid League!",\
                description="Refer codes for Top :five: Leagues here:",\
                color=0xf58300)
            embed.add_field(name='Premier League', value = 'PL' + "\n\u200b", inline=False)
            embed.add_field(name='La Liga', value = 'SPA' + "\n\u200b", inline=True)
            embed.add_field(name='Serie A', value = 'SA' + "\n\u200b", inline=False)
            embed.add_field(name='Bundesliga', value = 'BA' + "\n\u200b", inline=True)
            embed.add_field(name='Ligue 1', value = 'FL1', inline=False)
            return embed

        else:
            id = LEAGUE_CODE.get(leagueName)

            #Checking Cache
            if os.path.exists(f"cache/{leagueName}-MAT.json"):
                print('Reading from cache :D')
                with open(f"cache/{leagueName}-MAT.json", 'r') as cacheData:
                    obj = json.load(cacheData)
            else:

                #Fetching data from API
                r = requests.get(f"https://api.football-data.org/v2/competitions/{id}/matches?status=SCHEDULED", headers=headers)
                obj = r.json()

                #Writing data to cache
                with open(f"cache/{leagueName}-MAT.json", 'w') as cachedata:
                    json.dump(obj, cachedata, indent=4)

            fixtures = discord.Embed(title = obj['competition']['name'],\
                            description = 'Fixtures',\
                            color=0xf58300)
            if len(obj['matches']) == 0:
                fixtures.add_field(name = 'No remaining matches in the current season!',\
                                   value= '\u200b')
            else:
                for i, match in enumerate(obj['matches']):
                    if i > limit - 1:
                        break
                    matchTime = dt.datetime.strptime(match['utcDate'][:-1], '%Y-%m-%dt%H:%M:%S')
                    
                    #Converting to IST from UTC
                    matchTime += dt.timedelta(hours = 5, minutes = 30)
                    homeTeam = match['homeTeam']['name']
                    awayTeam = match['awayTeam']['name']

                    date = matchTime.strftime('%d %B %Y')
                    time = matchTime.strftime('%I:%M %p')
                    fixtures.add_field(name=f'{homeTeam}  :regional_indicator_v::regional_indicator_s:  {awayTeam}',\
                                        value=f'Date: {date}\nTime: {time}'+ str('\n\u200b' if i != limit - 1 else ' '),
                                        inline=False)
                    
                
            return fixtures

                
    except AssertionError:
        return discord.Embed(title = 'Limit must be greater than :zero:',\
                            description="Enter a valid limit :smile:",\
                            color=0xf58300 ) 


if __name__ == "__main__":
    print(getStandings('PL'))