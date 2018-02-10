#This program joins the data gathered from all diferents regions into one big file

import sqlite3
import sys

print("cheese.gg Data Assembler v1.0.1, by xaviolo99")

#check if data.db already exists
try:
    f = open("DATA.db", "xt")
    f.close()
except:
    print("\nDelete DATA.db in order to use the program")
    sys.exit()

#create data.db with the desired conditions
db = sqlite3.connect("DATA.db")
output = db.execute("CREATE TABLE IF NOT EXISTS data (champID UNSIGNED TINYINT, role TINYINT, side BIT, win BIT, duration UNSIGNED SMALLINT, kills SMALLINT, deaths SMALLINT, assists SMALLINT, keyRune TINYINT, "+
                     "spell1 TINYINT, spell2 TINYINT, ccStat SMALLINT, ccTime SMALLINT, visionScore SMALLINT, wardsPlaced MEDIUMINT, wardsKilled SMALLINT, healing INT, damageTaken INT, mitigated INT, "+
                     "totalDealt INT, totalMagic INT, champsDealt INT, champsMagic INT, turretsDealt MEDIUMINT, objectiveDealt INT, cs UNSIGNED MEDIUMINT, csJunStolen MEDIUMINT, xpDelta0_10 MEDIUMINT, "+
                     "xpDelta10_20 MEDIUMINT, xpDelta20_30 MEDIUMINT, xpDelta30_end MEDIUMINT, xpDiffDelta0_10 MEDIUMINT, xpDiffDelta10_20 MEDIUMINT, xpDiffDelta20_30 MEDIUMINT, xpDiffDelta30_end MEDIUMINT, "+
                     "csDelta0_10 SMALLINT, csDelta10_20 SMALLINT, csDelta20_30 SMALLINT, csDelta30_end SMALLINT, csDiffDelta0_10 SMALLINT, csDiffDelta10_20 SMALLINT, csDiffDelta20_30 SMALLINT, "+
                     "csDiffDelta30_end SMALLINT, goldDelta0_10 MEDIUMINT, goldDelta10_20 MEDIUMINT, goldDelta20_30 MEDIUMINT, goldDelta30_end MEDIUMINT, takenDelta0_10 UNSIGNED MEDIUMINT, "+
                     "takenDelta10_20 UNSIGNED MEDIUMINT, takenDelta20_30 UNSIGNED MEDIUMINT, takenDelta30_end UNSIGNED MEDIUMINT, takenDiffDelta0_10 UNSIGNED MEDIUMINT, takenDiffDelta10_20 UNSIGNED MEDIUMINT, "+
                     "takenDiffDelta20_30 UNSIGNED MEDIUMINT, takenDiffDelta30_end UNSIGNED MEDIUMINT);")

#dump the data from each endpoint to data.db
for server in ["RU", "KR", "BR1", "OC1", "JP1", "NA1", "EUN1", "EUW1", "TR1", "LA1", "LA2"]:
    try:
        db2 = sqlite3.connect("DATA"+server.lower()+".db")
        output = db2.execute("SELECT * FROM data").fetchall()

        for row in output:
            db.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "+
                       "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", row)

        db2.close()
        db.commit()
    except:
        pass
db.close()

print("\nDone!")
