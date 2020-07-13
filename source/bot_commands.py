import discord
import requests
import json
import os

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
            return "```diff\n- Please Check the league code!```"
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
                    json.dump(obj, cachedata)

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
    embed.add_field(name = ":exclamation: standings-all [PL or SPA or SA]", value = "Detailed Standings, with team codes", inline=False)
    embed.add_field(name = ":exclamation: standings [PL or SPA or SA]", value = "Display Standings", inline=False)
    embed.set_footer(text='Requested by: ' + str(ctx.author))

    return embed


if __name__ == "__main__":
    print(getStandings('PL'))