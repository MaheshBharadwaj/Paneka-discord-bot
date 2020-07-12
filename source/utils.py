import json

def putTableAll(obj):
    try:
        assert(type(obj) == dict)

        fin = open('source/teamcodes.json', 'r')
        mapper = json.load(fin)


        str_re = '```bash\nLEAGUE: ' + str(obj['competition']['name']) + ' ' *(45 -2 - 8 - 10 - len(str(obj['competition']['name']))) + 'MATCHDAY: ' +str(obj['season']['currentMatchday']) + '\n' 
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
    try:
        assert(type(obj) == dict)
        fin = open('source/teamcodes.json', 'r')

        str_re = '```bash\nLEAGUE: ' + str(obj['competition']['name']) + ' ' *(45 -2 - 8 - 10 - len(str(obj['competition']['name']))) + 'MATCHDAY: ' +str(obj['season']['currentMatchday']) + '\n' 
        str_re += '╔════╤══════════════════════════╤═════╤═════╗\n'
        str_re += '║ SN │        TEAM NAME         │ MAT │ PTS ║\n'
        str_re += '╠════╪══════════════════════════╪═════╪═════╣\n'
        for team in obj['standings'][0]['table']:
            text = '║ %-2d │ %-24s │ %-3d │ %-3d ║\n'\
                    %  (team['position'], team['team']['name'][:24], team['playedGames'],team['points'])
           
            str_re += text
            
        str_re += '╚════╧══════════════════════════╧═════╧═════╝```'
        fin.close()
        return str_re
    
    except AssertionError:
        return 'Error!'
