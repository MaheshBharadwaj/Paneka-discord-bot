<h1 align="center">Paneka</h1>
<p align = "center"><img src = "https://maheshk23.imfast.io/Paneka/logo.png"><br><br>
<img src = "https://img.shields.io/github/languages/top/MaheshBharadwaj/paneka?logo=python&logoColor=%23dddddd&style=flat-square">
<img src = "https://img.shields.io/github/v/tag/MaheshBharadwaj/paneka?color=%2349a305&label=Release&logo=github&logoColor=%23dddddd&style=flat-square">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/MaheshBharadwaj/paneka?color=%2349a305&label=Contributors&logo=GitHub&style=flat-square">
</p>
<hr>

# Introduction
Football bot for discord written in `python` using [discord.py](https://pypi.org/project/discord.py/) and currenty hosted on [heroku](https://heroku.com).

# Commands
### 1. Help
Displays the commands available for usage

**usage:** `!help`

<p align="center">
<img alt="help image" src="https://maheshk23.imfast.io/Paneka/help-command.png">
</p>

### 2. Standings All
Generates a more _detailed_ table showing goals for, against, matches won and lost

**usage:** `!standings-all [league code]`

<p align="center">
<img alt="standings-all image" src="https://maheshk23.imfast.io/Paneka/standings-all.png">
</p>

### 3. Standings
Generates the _current standings_ in the requested league.

**usage:** `!standings [league code]`

<p align="center">
<img alt="standings image" src="https://maheshk23.imfast.io/Paneka/standings.png">
</p>

### 4. Fixtures
Displays the next matches scheduled for the team or league as the case maybe.


**usage:** `!fixtures ['league' | 'team'][league code | team code] [limit: default 5]`

Limit restricts the number of fixtures displayed and is by default 5

#### 4.1 League Fixtures

<p align="center">
<img alt="League Fixtures image" src="https://maheshk23.imfast.io/Paneka/league-fixtures.png">
</p>

#### 4.2 Team Fixtures

<p align="center">
<img alt="Team Fixtures image" src="https://maheshk23.imfast.io/Paneka/team-fixtures.png">
</p>


# How to run locally:
 - fork and clone repository
 - ```bash
   cd paneka/
   pip install -r requirements.txt
   
   #create a file '.env'
   touch .env
   ```
 - Become a discord developer and create a new bot
 - Copy the token under `Build-A-Bot`
 - Store the key in `.env` as follows:<br>
   `DISCORD_KEY=The code`<br>
   **NOTE: NO spaces around the '='**
 - `python3 bot.py` to run the bot
 - Add the bot to your guild(server) by inviting it using the OAuth2 link present in the developer application window
 - The bot is now ready :D
 
 
