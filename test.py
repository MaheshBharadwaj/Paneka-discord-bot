import requests
import json
import sys
import os
from dotenv import load_dotenv

from source.utils import putTableAll, putTableLong
from source.league_code import LEAGUE_CODE


def getStandings(code, mode='long'):

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
            if os.path.exists(f"cache/{leagueName}.json"):
                print('Reading from cache :D')
                with open(f"cache/{leagueName}.json", 'r') as cacheData:
                    obj = json.load(cacheData)
                    if mode == 'all':
                        return putTableAll(obj)
                    return putTableLong(obj)
            else:
                r = requests.get(f"https://api.football-data.org/v2/competitions/{id}/standings", headers=headers)
                obj = r.json()
                with open(f"cache/{leagueName}.json", 'w') as cachedata:
                    json.dump(obj, cachedata)

                if mode == 'all':
                    return putTableAll(obj)
                return putTableLong(obj)
                
    except AssertionError:
        return '```diff\n- Invalid Args passed!```'


if __name__ == "__main__":
    print(getStandings('PL'))