##PYTHON 3 AND IMPORTED PACKAGES NEEDED##

# IMPORTS AND PRESENTATION #

import sqlite3
import requests
import sys
import json
import time

print("cheese.gg Recursive Data Gatherer v0.1, by xaviolo99")

# USER GIVEN DATA #

apiKey = "" #If it doesnt work, create a new one
beginTime = str( ( int(time.time())-1209600 )*1000 ) #https://www.epochconverter.com/ (1209600 seconds is 14 days)
delay = 120/(100*0.95) #seconds in 2 mins/(number of requests allowed per 2 minutes * penalty to avoid rate limiting)

iSumm = ""#accountId
while iSumm == "":
    server = input("RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2: ").lower()
    if server == "ru": #not working atm
        iSumm = "204081143"
    if server == "kr":
        iSumm = "4020503"
    if server == "br1":
        iSumm = "215909221"
    if server == "oc1":
        iSumm = "202402241"
    if server == "jp1":
        iSumm = "201185961"
    if server == "na1":
        iSumm = "34897744"
    if server == "eun1":
        iSumm = "33497422"
    if server == "euw1":
        iSumm = "35306044"
    if server == "tr1":
        iSumm = "177684"
    if server == "la1": #lan
        iSumm = "201267194"
    if server == "la2": #las
        iSumm = "106151"
    if iSumm == "":
        print("Server not recognised")

# CONVERSORS #

rito_to_num = [266, 103, 84, 12, 32, 34, 1, 22, 136, 268, 432, 53, 63, 201, 51, 164, 69, 31, 42, 122, 131, 119, 36, 245, 60, 28, 81, 9, 114, 105, 3, 41, 86, 150, 79, 104, 120, 74,
               420, 39, 427, 40, 59, 24, 126, 202, 222, 429, 43, 30, 38, 55, 10, 141, 85, 121, 203, 240, 96, 7, 64, 89, 127, 236, 117, 99, 54, 90, 57, 11, 21, 62, 82, 25, 267, 75, 111, 76,
               56, 20, 2, 61, 516, 80, 78, 133, 497, 33, 421, 58, 107, 92, 68, 13, 113, 35, 98, 102, 27, 14, 15, 72, 37, 16, 50, 134, 223, 163, 91, 44, 17, 412, 18, 48, 23, 4, 29, 77, 6,
               110, 67, 45, 161, 254, 112, 8, 106, 19, 498, 101, 5, 157, 83, 154, 238, 115, 26, 142, 143]

num_to_alpha = ['Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia',
                "Cho'Gath", 'Corki', 'Darius', 'Diana', 'Draven', 'Dr. Mundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar',
                'Gragas', 'Graves', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', 'Kalista', 'Karma', 'Karthus', 'Kassadin',
                'Katarina', 'Kayle', 'Kayn', 'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", 'LeBlanc', 'Lee Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar',
                'Maokai', 'Master Yi', 'Miss Fortune', 'Wukong', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon',
                'Poppy', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner',
                'Sona', 'Soraka', 'Swain', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot',
                'Varus', 'Vayne', 'Veigar', "Vel'Koz", 'Vi', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']

perk0_to_key = [8005, 8008, 8021, 8112, 8124, 8128, 8214, 8229, 8230, 8326, 8351, 8359, 8437, 8439, 8465]

key_to_alpha = ['Press the Attack', 'Lethal Tempo', 'Fleet Footwork', 'Electrocute', 'Predator', 'Dark Harvest', 'Summon Aery', 'Arcane Comet', 'Phase Rush', 'Unsealed Spellbook',
                'Glacial Augment', 'Kleptomancy', 'Grasp of the Undying', 'Aftershock', 'Guardian']

spellId_to_spell = [12, 3, 21, 13, 4, 14, 6, 7, 1, 11]

spell_to_alpha = ['Teleport', 'Exhaust', 'Barrier', 'Clarity', 'Flash', 'Ignite', 'Ghost', 'Heal', 'Cleanse', 'Smite']

# FUNCTIONS #

#This function checks if there was a server error in the request
def ok(data):
    try:
        print("ERROR (server) ["+str(data["status"]["status_code"])+"]\n")
        return False
    except:
        return True
    
#This function extracts matches from a summoner's match history
def dissect_summoner(sID):
    sData = json.loads(requests.get("https://"+server+".api.riotgames.com/lol/match/v3/matchlists/by-account/"+sID+"?beginTime="+beginTime+"&api_key="+apiKey).text)

    if not ok(sData):
        return

    #try/except in case the summoner has no played games and there is no matches in json
    count = 0
    try:
        for match in sData["matches"]:
            #check if the game is a season 8 soloQ one (maybe add flex)
            if match["season"] < 8 or match["queue"] != 420:
                continue
            
            #store the match if it doesnt exist
            mID = match["gameId"]
            e = db.execute("SELECT EXISTS (SELECT 1 FROM matches WHERE id = ? LIMIT 1);", (mID,)).fetchone()[0]#returns 1 if match exists in db
            if e == 0:
                db.execute("INSERT INTO matches (id) VALUES (?);", (mID,))
                count += 1
    except:
        pass
            
    db.commit()
    print(str(count)+" match(es) found")

#This function extracts summoner ID's and relevant data about champions from a game
def dissect_match(mID):
    mData = json.loads(requests.get("https://"+server+".api.riotgames.com/lol/match/v3/matches/"+mID+"?api_key="+apiKey).text)
    if not ok(mData):
        return

    #find summoners
    count = 0
    for summoner in mData["participantIdentities"]:
        #store match and update summData
        sID = summoner["player"]["accountId"]
        
        #save the match if it doesnt exist
        e = db.execute("SELECT EXISTS (SELECT 1 FROM summoners WHERE id = ? LIMIT 1);", (sID,)).fetchone()[0]#returns 1 if match exists in db
        if e == 0:
            db.execute("INSERT INTO summoners (id) VALUES (?);", (sID,))
            count += 1            

    db.commit()
    print(str(count)+" summoner(s) found")

    #find the other relevant data

    #winner
    check = mData["teams"][0]["teamId"]
    wr = 0
    if mData["teams"][0]["win"] == "Win":
        wr = 1
    if check == 200:
        wr = (wr+1)%2

    #duration [duration]
    duration = mData["gameDuration"]

    for champion in mData["participants"]:
        stats = champion["stats"]
        
        #champion (alphabetically) [champID]
        champID = rito_to_num.index(champion["championId"])

        #champion role [role]
        lane = champion["timeline"]["lane"]
        spec = champion["timeline"]["role"]
        if lane == "TOP":
            role = 0
        if lane == "JUNGLE":
            role = 1
        if lane == "MIDDLE":
            role = 2
        if lane == "BOTTOM":
            if spec == "DUO_CARRY":
                role = 3
            if spec == "DUO_SUPPORT":
                role = 4

        #team and win? [side] [win]
        team = champion["teamId"]
        if team == 100:
            side = 0
            win = wr
        if team == 200:
            side = 1
            win = (wr+1)%2

        #KDA [kills] [deaths] [assists]
        kills = stats["kills"]
        deaths = stats["deaths"]
        assists = stats["assists"]

        #key rune (https://pastebin.com/1wUpcn7i) [keyRune]
        keyRune = perk0_to_key.index(stats["perk0"])

        #summoner spells [spell1] [spell2]
        if champion["spell1Id"] == 4:
            spell1 = 4
            spell2 = champion["spell2Id"]
        elif champion["spell2Id"] == 4:
            spell1 = 4
            spell2 = champion["spell1Id"]
        else:
            spell1 = champion["spell1Id"]
            spell2 = champion["spell2Id"]
            
        spell1 = spellId_to_spell.index(spell1)
        spell2 = spellId_to_spell.index(spell2)

        #crowd control [ccStat] [ccTime]
        ccStat = stats["timeCCingOthers"]
        ccTime = stats["totalTimeCrowdControlDealt"]

        #vision [visionScore] [wardsPlaced] [wardsKilled]
        visionScore = stats["visionScore"]
        wardsPlaced = stats["wardsPlaced"]
        wardsKilled = stats["wardsKilled"]

        #total heal [healing]
        healing = stats["totalHeal"]

        #damage taken [damageTaken] [mitigated]
        damageTaken = stats["totalDamageTaken"]
        mitigated = stats["damageSelfMitigated"]

        #damage dealt [totalDealt] [totalMagic] [champsDealt] [champsMagic] [turretsDealt] [objectiveDealt]
        totalDealt = stats["totalDamageDealt"]
        totalMagic = stats["magicDamageDealt"]
        
        champsDealt = stats["totalDamageDealtToChampions"]
        champsMagic = stats["magicDamageDealtToChampions"]
        
        turretsDealt = stats["damageDealtToTurrets"]
        objectiveDealt = stats["damageDealtToObjectives"]

        #minions [cs] [csJunStolen]
        cs = stats["totalMinionsKilled"]
        csJunStolen = stats["neutralMinionsKilledEnemyJungle"]

        #WIP
##        #deltas [xpDelta] [xpDiffDelta] [csDelta] [csDiffDelta] [goldDelta] [takenDelta] [takenDiffDelta]
##        deltas = champion["timeline"]
##        
##        xpDelta = create_delta(deltas["xpPerMinDeltas"])
##        xpDiffDelta = create_delta(deltas["xpDiffPerMinDeltas"])
##        
##        csDelta = create_delta(deltas["creepsPerMinDeltas"])
##        csDiffDelta = create_delta(deltas["csDiffPerMinDeltas"])
##        
##        takenDelta = create_delta(deltas["damageTakenPerMinDeltas"])
##        takenDiffDelta = create_delta(deltas["damageTakenDiffPerMinDeltas"])
##
##        goldDelta = create_delta(deltas["goldPerMinDeltas"])
        
        #Save To Database
        try:
            db.execute("INSERT INTO data (champID, role, side, win, duration, kills, deaths, assists, keyRune, spell1, spell2, ccStat, ccTime, visionScore, wardsPlaced, wardsKilled, healing, damageTaken, mitigated, "+
                       "totalDealt, totalMagic, champsDealt, champsMagic, turretsDealt, objectiveDealt, cs, csJunStolen) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (champID, role, side, win, duration, kills, deaths, assists, keyRune, spell1, spell2, ccStat, ccTime, visionScore, wardsPlaced, wardsKilled, healing, damageTaken, mitigated,
                       totalDealt, totalMagic, champsDealt, champsMagic, turretsDealt, objectiveDealt, cs, csJunStolen) )
            db.commit()
        except UnboundLocalError:
            print("ERROR (game)")

# CREATE/RECOVER DATABASE #

try:
    f = open('DATA'+server+'.db', 'xt')
    f.close()
    print("No database found. Creating a new one...\n")

    db = sqlite3.connect("DATA"+server+".db")
    db.execute("CREATE TABLE IF NOT EXISTS summoners (id INT);")
    db.execute("CREATE TABLE IF NOT EXISTS matches (id INT);")
    db.execute("CREATE TABLE IF NOT EXISTS actual (match INT, summoner INT);")
    db.execute("INSERT INTO actual (match, summoner) VALUES (1, 1)")

    db.execute("CREATE TABLE IF NOT EXISTS data (champID UNSIGNED TINYINT, role TINYINT, side BIT, win BIT, duration UNSIGNED SMALLINT, kills SMALLINT, deaths SMALLINT, assists SMALLINT, keyRune TINYINT, "+
               "spell1 TINYINT, spell2 TINYINT, ccStat SMALLINT, ccTime SMALLINT, visionScore SMALLINT, wardsPlaced MEDIUMINT, wardsKilled SMALLINT, healing INT, damageTaken INT, mitigated INT, "+
               "totalDealt INT, totalMagic INT, champsDealt INT, champsMagic INT, turretsDealt MEDIUMINT, objectiveDealt INT, cs UNSIGNED MEDIUMINT, csJunStolen MEDIUMINT);")#27 elements (+ deltas)

    dissect_summoner(iSumm)
except:
    print("Database found\n")
    db = sqlite3.connect("DATA"+server+".db")

mInd = db.execute("SELECT match FROM actual;").fetchone()[0]
sInd = db.execute("SELECT summoner FROM actual;").fetchone()[0]

# RECURSION #

try:
    while True:
        #check if it is time to analyze the next stored summoner
        while db.execute( "SELECT id FROM matches WHERE ROWID = ?;", (mInd,) ).fetchone() == None:

            #check if the recursion cant go further
            if db.execute( "SELECT id FROM summoners WHERE ROWID = ?;", (sInd,) ).fetchone() == None:
                print("End of the recursion reached. Exiting...")
                sys.exit()

            #analyze summoner
            bTime = time.clock()
            print("\nAnalysing summoner "+str(sInd+1))
            dissect_summoner(str(db.execute( "SELECT id FROM summoners WHERE ROWID = ?;", (sInd,) ).fetchone()[0]))
            sInd += 1
            db.execute("UPDATE actual SET summoner = ? WHERE ROWID = 1;", (sInd,))
            db.commit()
            if delay-(time.clock()-bTime) > 0:
                time.sleep(delay-(time.clock()-bTime))

        #analyze match
        bTime = time.clock()
        print("\nMatch "+str(mInd))
        dissect_match(str(db.execute( "SELECT id FROM matches WHERE ROWID = ?;", (mInd,) ).fetchone()[0]))
        mInd += 1
        db.execute("UPDATE actual SET match = ? WHERE ROWID = 1;", (mInd,))
        db.commit()
        if delay-(time.clock()-bTime) > 0:
            time.sleep(delay-(time.clock()-bTime))
except KeyboardInterrupt:
    pass

# SAVE #

db.execute("UPDATE actual SET match = ? WHERE ROWID = 1;", (mInd,))
db.execute("UPDATE actual SET summoner = ? WHERE ROWID = 1;", (sInd,))
db.commit()
db.close()
print("\nSaved!")
