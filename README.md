<h1 align="center">Paneka</h1>
<p align = "center"><img src = "https://maheshk23.imfast.io/Paneka/logo.png"><br><br>
<img src = "https://img.shields.io/github/languages/top/MaheshBharadwaj/paneka?logo=python&logoColor=%23dddddd&style=flat-square">
<img src = "https://img.shields.io/github/v/tag/MaheshBharadwaj/paneka?color=%2349a305&label=Release&logo=github&logoColor=%23dddddd&style=flat-square">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/MaheshBharadwaj/paneka?color=%2349a305&label=Contributors&logo=GitHub&style=flat-square">
<img alt="Hits" src="http://hits.dwyl.com/MaheshBharadwaj/Paneka-discord-bot.svg"><br><br>
<h2 align="center">Click <a href = "https://discord.com/api/oauth2/authorize?client_id=731544990446256198&permissions=60416&scope=bot">Here</a> To invite the bot to your server!</h2>
</p>
<hr>

# Introduction
Football bot for discord written in `python` using [discord.py](https://pypi.org/project/discord.py/) and currenty hosted on [heroku](https://heroku.com).

The API used for fetching football data is [football-data.org](https://football-data.org)'s free tier and hence we have a rate limit of **10 Requests / Min** and **12** Competitions.

# Commands
### 1. Help
Displays the commands available for usage

**usage:** `.help`

<p align="center">
<img alt="help image" src="https://maheshk23.imfast.io/Paneka/help-command-v2.png">
</p>

### 2. Standings All
Generates a more _detailed_ table showing goals for, against, matches won and lost

**usage:** `.standings-all [league code]`

<p align="center">
<img alt="standings-all image" src="https://maheshk23.imfast.io/Paneka/standings-all-v2.png">
</p>

### 3. Standings
Generates the _current standings_ in the requested league.

**usage:** `.standings [league code]`

<p align="center">
<img alt="standings image" src="https://maheshk23.imfast.io/Paneka/standings-v2.png">
</p>

### 4. Fixtures
Displays the next matches scheduled for the team or league requested.

**usage:** `.fixtures [league code | team code] [limit: default 5]`

Limit restricts the number of fixtures displayed and is by default 5

#### 4.1 League Fixtures

<p align="center">
<img alt="League Fixtures image" src="https://maheshk23.imfast.io/Paneka/league-fixtures-v2.png">
</p>

#### 4.2 Team Fixtures

<p align="center">
<img alt="Team Fixtures image" src="https://maheshk23.imfast.io/Paneka/team-fixtures-v2.png">
</p>

### 5. Live Scores
Displays the live scores of matches in league requested or team requested

**usage:** `.live [league code | team code] [limit: default 5]`

Limit restricts number of matches displayed and is by default 5

<p align="center">
<img alt="Team Fixtures image" src="https://maheshk23.imfast.io/Paneka/live-league-v2.png">
</p>

### 6. Invite
Sends the URL to invite bot into servers as a _Direct Message_

**usage:** `.invite`

<p align="center">
<img alt="Invite Command image" src="https://maheshk23.imfast.io/Paneka/invite-command-v2.png">
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
   `DISCORD_TOKEN=The Bot code`<br>
   **NOTE:** NO _spaces_ around the `'='`
 - Get a **free** football-data API key from [football-data.org](https://www.football-data.org/)
 - Store this key in `.env` on a new line as:<br>
   `API_KEY=The API code`<br>
   **NOTE:** NO _spaces_ around the `'='`
 - `python3 bot.py` to run the bot
 - Add the bot to your guild(server) by inviting it using the OAuth2 link present in the developer application window
 - The bot is now ready :D
 
 # League Codes
 All the supported leagues and their codes are listed below

| League | Code |
| :----- | :--: |
| **Bundesliga**<br>Germany | `BL` |
| **Brazillian Serie A**<br>Brazil | `BSA` |
| **English Championship**<br>England | `ECL` |
| **Eredivisie**<br>Netherlands | `ERD` |
| **Ligue One**<br>France | `FL1` |
| **Premier League**<br>England | `PL` |
| **Primeira Liga**<br>Porugal | `PPL` |
| **Serie A**<br>Italy | `SA` |
| **La Liga**<br>Spain| `SPA` |


 ## Credits: 
 Logo Courtesy:
 Icons made by [Freepik](https://www.flaticon.com/authors/freepik) from [Flaticon](https://www.flaticon.com/)
 
 
