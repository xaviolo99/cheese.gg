import sqlite3
import time
import math
import sys

#CONVERSORS
num_to_alpha = ['Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia',
                "Cho'Gath", 'Corki', 'Darius', 'Diana', 'Draven', 'Dr. Mundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar',
                'Gragas', 'Graves', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'Sa", 'Kalista', 'Karma', 'Karthus', 'Kassadin',
                'Katarina', 'Kayle', 'Kayn', 'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", 'LeBlanc', 'Lee Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar',
                'Maokai', 'Master Yi', 'Miss Fortune', 'Wukong', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon',
                'Poppy', 'Pyke', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner',
                'Sona', 'Soraka', 'Swain', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot',
                'Varus', 'Vayne', 'Veigar', "Vel'Koz", 'Vi', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']

#stats between 0 and 3, in this order [Damage, Toughness, Control, Mobility, Utility, Range]
#exceptions: -warwick mobility 2 instead of 1 -xayah control 2 instead of 3
num_to_stats = [[2, 2, 2, 2, 0, 1], [3, 1, 2, 3, 0, 2], [3, 1, 1, 3, 1, 1], [1, 3, 3, 1, 2, 1], [2, 3, 3, 1, 0, 1], [3, 1, 3, 0, 2, 2], [3, 1, 3, 0, 2, 2], [2, 0, 3, 0, 2, 3], [3, 0, 2, 2, 0, 2],
                [3, 1, 2, 2, 1, 3], [1, 1, 3, 2, 3, 2], [1, 2, 3, 1, 0, 1], [3, 0, 2, 0, 0, 2], [1, 2, 3, 1, 2, 1], [3, 0, 2, 2, 0, 3], [3, 2, 2, 3, 0, 1], [3, 1, 3, 1, 0, 2], [2, 3, 2, 0, 0, 0],
                [3, 0, 1, 2, 0, 3], [3, 2, 2, 0, 0, 0], [3, 2, 2, 2, 0, 0], [3, 0, 1, 2, 0, 2], [2, 3, 1, 0, 0, 0], [3, 2, 2, 3, 0, 1], [2, 2, 2, 2, 0, 2], [2, 2, 1, 2, 2, 0], [3, 0, 0, 3, 1, 3],
                [3, 1, 3, 1, 0, 2], [3, 2, 2, 2, 2, 1], [3, 1, 2, 3, 0, 1], [2, 3, 3, 2, 1, 1], [3, 1, 1, 1, 2, 2], [2, 3, 1, 1, 0, 0], [2, 1, 1, 2, 0, 2], [2, 3, 3, 2, 0, 1], [3, 2, 1, 2, 2, 2],
                [2, 2, 2, 2, 0, 0], [3, 0, 2, 0, 2, 2], [3, 2, 1, 0, 0, 1], [3, 2, 2, 2, 0, 1], [1, 1, 3, 2, 3, 2], [1, 1, 3, 1, 3, 2], [2, 2, 2, 2, 2, 1], [3, 2, 2, 2, 0, 0], [3, 0, 1, 2, 2, 3],
                [3, 0, 2, 0, 0, 3], [3, 0, 2, 1, 0, 3], [3, 1, 0, 3, 1, 2], [3, 0, 1, 3, 2, 2], [2, 1, 2, 1, 2, 2], [3, 0, 1, 0, 2, 2], [3, 2, 1, 3, 0, 1], [3, 0, 0, 3, 0, 1], [3, 1, 1, 1, 3, 2],
                [2, 1, 1, 2, 2, 1], [3, 1, 3, 1, 0, 2], [3, 1, 1, 2, 0, 1], [3, 1, 2, 3, 2, 2], [3, 2, 1, 3, 1, 0], [3, 0, 1, 0, 1, 3], [3, 0, 2, 3, 0, 2], [3, 2, 2, 3, 1, 1], [1, 3, 3, 1, 1, 1],
                [3, 1, 3, 2, 0, 2], [3, 0, 0, 3, 0, 2], [2, 1, 2, 1, 3, 2], [3, 1, 2, 0, 2, 3], [1, 3, 3, 1, 0, 1], [3, 1, 3, 0, 2, 2], [1, 3, 3, 1, 2, 1], [3, 1, 0, 2, 0, 0], [3, 0, 1, 1, 0, 2],
                [2, 2, 2, 2, 1, 1], [3, 2, 0, 0, 2, 1], [2, 1, 3, 0, 2, 2], [1, 1, 3, 1, 2, 2], [2, 3, 2, 0, 1, 1], [1, 3, 3, 1, 0, 1], [3, 1, 0, 3, 2, 3], [3, 1, 2, 2, 2, 1], [1, 3, 2, 1, 2, 1],
                [2, 2, 2, 1, 0, 1], [2, 1, 2, 1, 2, 3], [1, 3, 3, 1, 2, 1], [3, 2, 2, 2, 0, 1], [2, 3, 3, 2, 0, 0], [3, 0, 2, 3, 1, 2], [3, 0, 3, 2, 0, 1], [1, 2, 3, 3, 3, 1], [2, 3, 3, 2, 1, 0],
                [2, 2, 2, 2, 2, 1], [2, 2, 2, 2, 1, 0], [3, 1, 2, 2, 0, 1], [3, 2, 2, 3, 0, 0], [3, 2, 2, 1, 0, 1], [3, 1, 2, 2, 2, 2], [2, 2, 3, 2, 0, 1], [3, 1, 2, 2, 2, 1], [2, 3, 2, 2, 3, 0],
                [2, 2, 0, 2, 0, 0], [2, 3, 2, 2, 0, 0], [2, 3, 3, 1, 0, 1], [3, 1, 0, 1, 2, 2], [1, 3, 3, 1, 1, 0], [2, 1, 2, 1, 2, 2], [1, 1, 2, 1, 3, 2], [2, 2, 2, 0, 0, 2], [3, 0, 2, 0, 0, 2],
                [2, 3, 2, 1, 3, 1], [3, 0, 2, 1, 3, 2], [3, 0, 1, 2, 0, 1], [1, 2, 2, 0, 3, 1], [3, 0, 2, 1, 2, 2], [1, 2, 3, 1, 3, 2], [3, 0, 2, 2, 0, 2], [2, 3, 1, 1, 2, 1], [3, 2, 1, 2, 0, 0],
                [3, 0, 2, 2, 2, 2], [3, 0, 1, 2, 0, 2], [2, 3, 2, 2, 0, 0], [2, 2, 2, 1, 1, 2], [3, 0, 2, 0, 0, 2], [3, 0, 2, 2, 0, 2], [3, 0, 3, 0, 0, 2], [3, 0, 2, 0, 0, 3], [2, 2, 3, 2, 1, 0],
                [3, 1, 2, 0, 0, 2], [3, 2, 1, 1, 1, 2], [2, 3, 2, 2, 0, 0], [2, 2, 2, 2, 1, 0], [3, 2, 2, 1, 0, 2], [3, 0, 2, 0, 0, 3], [2, 2, 2, 2, 1, 0], [3, 1, 2, 3, 2, 1], [2, 2, 2, 0, 2, 1],
                [2, 3, 3, 2, 0, 1], [3, 0, 1, 3, 0, 1], [3, 0, 2, 2, 0, 3], [2, 1, 2, 2, 3, 2], [3, 1, 2, 2, 1, 3], [3, 0, 3, 0, 1, 2]]

try:
    f = open("CHAMPS_ALL.db", "xt")
    f.close()
except:
    print("\nDelete CHAMPS_ALL.db in order to use the program")
    sys.exit()

#LOAD DATA
bTime = time.time()
db = sqlite3.connect("DATA.db")
pre = db.execute("SELECT * FROM data").fetchall()
db.close()

print("Data loaded, "+str(time.time()-bTime)+"s")

#PREPARE DATA
bTime = time.time()

#Append the static data
champData = []
champSamples = []
for champ in range(len(num_to_stats)):
    champSamples.append(0)
    champData.append(num_to_stats[champ])
    champData[champ].extend([0] * 41) #6 static+ 37 dynamic

#Calculate the SUMS for the median and variance of every aspect
for point in pre:
    champ = point[0]
    champSamples[champ] += 1

    #Static (Damage, Toughness, Control, Mobility, Utility, Range) [0, 5]

    #WR (mean) [6]
    champData[champ][6] += point[3]

    #Duration (mean, variance) [7, 8]
    champData[champ][7] += point[4]
    champData[champ][8] += point[4] ** 2

    #Kills, Deaths, Assists (mean, variance) [9, 10] [11, 12] [13, 14]
    champData[champ][9] += point[5]
    champData[champ][10] += point[5] ** 2

    champData[champ][11] += point[6]
    champData[champ][12] += point[6] ** 2

    champData[champ][13] += point[7]
    champData[champ][14] += point[7] ** 2

    #ccStat (mean, variance) [15, 16]
    champData[champ][15] += point[11]
    champData[champ][16] += point[11] ** 2

    #visionScore (mean, variance) [17, 18]
    champData[champ][17] += point[13]
    champData[champ][18] += point[13] ** 2

    #Healing (mean, variance) [19, 20]
    champData[champ][19] += point[16]
    champData[champ][20] += point[16] ** 2

    #Damage Taken (mean, variance) [21, 22]
    champData[champ][21] += point[17]
    champData[champ][22] += point[17] ** 2

    #Damage Mitigated (mean, variance) [23, 24]
    champData[champ][23] += point[18]
    champData[champ][24] += point[18] ** 2

    #Damage Dealt (mean, variance) [25, 26]
    champData[champ][25] += point[19]
    champData[champ][26] += point[19] ** 2

    #Damage Dealt Magic (mean, variance) [27, 28]
    champData[champ][27] += point[20]
    champData[champ][28] += point[20] ** 2

    #Damage Dealt Champions (mean, variance) [29, 30]
    champData[champ][29] += point[21]
    champData[champ][30] += point[21] ** 2

    #Damage Dealt Champions Magic (mean, variance) [31, 32]
    champData[champ][31] += point[22]
    champData[champ][32] += point[22] ** 2

    #Damage Dealt Objectives (mean, variance) [33, 34]
    champData[champ][33] += point[24]
    champData[champ][34] += point[24] ** 2

    #Turret Kills (mean, variance) [35, 36]
    champData[champ][35] += point[27]
    champData[champ][36] += point[27] ** 2

    #Inhib Kills (mean, variance) [37, 38]
    champData[champ][37] += point[28]
    champData[champ][38] += point[28] ** 2

    #CS (mean, variance) [39, 40]
    champData[champ][39] += point[25]
    champData[champ][40] += point[25] ** 2

    #Gold (mean, variance) [41, 42]
    champData[champ][41] += point[29]
    champData[champ][42] += point[29] ** 2

    #Duration on win/loss (mean, variance) [43, 44] [45, 46]
    if point[3] == 1:
        champData[champ][43] += point[4]
        champData[champ][44] += point[4] ** 2
    else:
        champData[champ][45] += point[4]
        champData[champ][46] += point[4] ** 2

def mean(ind):
    champData[champ][ind] = round(champData[champ][ind]/champSamples[champ], 6)
    
def sd(ind1, ind2): #ind1 is variance, ind2 is mean
    champData[champ][ind1] = round(math.sqrt((champData[champ][ind1]/champSamples[champ]) - champData[champ][ind2] ** 2), 6)

#Calculate the actual mean/variance
for champ in range(len(num_to_stats)):
    
    #WR (mean)
    mean(6)

    #Duration (mean, variance)
    mean(7)
    sd(8, 7)

    #Kills, Deaths, Assists (mean, variance)
    mean(9)
    sd(10, 9)
    
    mean(11)
    sd(12, 11)
    
    mean(13)
    sd(14, 13)

    #ccStat (mean, variance)
    mean(15)
    sd(16, 15)

    #visionScore (mean, variance)
    mean(17)
    sd(18, 17)

    #Healing (mean, variance)
    mean(19)
    sd(20, 19)

    #Damage Taken (mean, variance)
    mean(21)
    sd(22, 21)

    #Damage Mitigated (mean, variance)
    mean(23)
    sd(24, 23)

    #Damage Dealt (mean, variance)
    mean(25)
    sd(26, 25)

    #Damage Dealt Magic (mean, variance)
    mean(27)
    sd(28, 27)

    #Damage Dealt Champions (mean, variance)
    mean(29)
    sd(30, 29)

    #Damage Dealt Champions Magic (mean, variance)
    mean(31)
    sd(32, 31)

    #Damage Dealt Objectives (mean, variance)
    mean(33)
    sd(34, 33)

    #Turret Kills (mean, variance)
    mean(35)
    sd(36, 35)

    #Inhib Kills (mean, variance)
    mean(37)
    sd(38, 37)

    #CS (mean, variance)
    mean(39)
    sd(40, 39)

    #Gold (mean, variance)
    mean(41)
    sd(42, 41)

    #Duration on win/loss (mean, variance)
    champData[champ][43] = round(champData[champ][43]/(champSamples[champ]*champData[champ][6]), 6)
    champData[champ][44] = round(math.sqrt((champData[champ][44]/(champSamples[champ]*champData[champ][6])) - champData[champ][43] ** 2), 6)
    
    champData[champ][45] = round(champData[champ][45]/(champSamples[champ]*(1-champData[champ][6])), 6)
    champData[champ][46] = round(math.sqrt((champData[champ][46]/(champSamples[champ]*(1-champData[champ][6]))) - champData[champ][45] ** 2), 6)


print("Data prepared, "+str(time.time()-bTime)+"s")

db = sqlite3.connect("CHAMPS_ALL.db")
db.execute("CREATE TABLE IF NOT EXISTS data (champID INT, damage REAL, toughness REAL, control REAL, mobility REAL, utility REAL, range REAL, winrate REAL, durationM REAL, durationSD REAL, "+
                    "killsM REAL, killsSD REAL, deathsM REAL, deathsSD REAL, assistsM REAL, assistsSD REAL, ccstatM REAL, ccstatSD REAL, visionscoreM REAL, visionscoreSD REAL, healingM REAL, "+
                    "healingSD REAL, damagetakenM REAL, damagetakenSD REAL, mitigatedM REAL, mitigatedSD REAL, damagedealtM REAL, damagedealtSD REAL, dealtmagicM REAL, dealtmagicSD REAL, "+
                    "dealtchampsM REAL, dealtchampsSD REAL, dealtchampsmagicM REAL, dealtchampsmagicSD REAL, dealtobjectivesM REAL, dealtobjectivesSD REAL, turretkillsM REAL, turretkillsSD REAL, "+
                    "inhibkillsM REAL, inhibkillsSD REAL, csM REAL, csSD REAL, goldM REAL, goldSD REAL, durwinM REAL, durwinSD REAL, durlossM REAL, durlossSD REAL);")

for champ in range(len(champData)):
    hehe = [champ]
    hehe.extend(champData[champ])
    db.execute("INSERT INTO data VALUES (? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", tuple(hehe))
db.commit()

print("All done!")
