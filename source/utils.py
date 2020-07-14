import json

def putTableAll(obj):
    """
    Displays the standings in long format
    Displays team code if available or first 4 letters of team name,
    Matches Played, Won, Drawn, Lost
    Points
    Goals For, Against, Difference
    """
    try:
        assert(type(obj) == dict)

        fin = open('source/teamcodes.json', 'r')
        mapper = json.load(fin)


        str_re = '```bash\nLEAGUE: ' + str(obj['competition']['name']) +\
                 ' ' *(45 -2 - 8 - 10 - len(str(obj['competition']['name']))) +\
                 'MATCHDAY: ' +str(obj['season']['currentMatchday']) + '\n' 
        str_re += '╔════╤══════╤════╤════╤════╤════╤═════╤═════╗\n'
        str_re += '║ SN │ TEAM │ M  │ W  │ D  │ L  │ PTS │ GD  ║\n'
        str_re += '╠════╪══════╪════╪════╪════╪════╪═════╪═════╣\n'
        for team in obj['standings'][0]['table']:
            text = '║ %-2d │ %-4s │ %-2d │ %-2d │ %-2d │ %-2d │ %-3d │ %+-3d ║\n'\
                    %  (team['position'], mapper.get(team['team']['name'],team['team']['name'][:4])[:4], team['playedGames'], team['won'],\
                        team['draw'], team['lost'], team['points'], team['goalDifference'])
           
            str_re += text
            
        str_re += '╚════╧══════╧════╧════╧════╧════╧═════╧═════╝```'
        fin.close()
        return str_re
    
    except AssertionError:
        return 'Error!'

def putTableLong(obj):
    """
    Displays a basic standings showing Team Names,
    Matches Played and Points obtained.
    """
    try:
        assert(type(obj) == dict)

        str_re = '```bash\nLEAGUE: ' + str(obj['competition']['name']) +\
                 ' ' *(45 -2 - 8 - 10 - len(str(obj['competition']['name']))) +\
                 'MATCHDAY: ' +str(obj['season']['currentMatchday']) + '\n' 
        str_re += '╔════╤══════════════════════════╤═════╤═════╗\n'
        str_re += '║ SN │        TEAM NAME         │ MAT │ PTS ║\n'
        str_re += '╠════╪══════════════════════════╪═════╪═════╣\n'
        for team in obj['standings'][0]['table']:
            text = '║ %-2d │ %-24s │ %-3d │ %-3d ║\n'\
                    %  (team['position'], team['team']['name'][:24], team['playedGames'],team['points'])
           
            str_re += text
            
        str_re += '╚════╧══════════════════════════╧═════╧═════╝```'
        return str_re
    
    except AssertionError:
        return 'Error!'


def fetchImage(code):
    if code in ['PL', 'FL1', 'BL', 'SPA', 'SA']:
        return f"source/logos/{code}.jpg"
    else:
        return None