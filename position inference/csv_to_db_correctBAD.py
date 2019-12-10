import numpy as np
import sqlite3
import pandas as pd
import time
import sys

bTime = time.time()

try:
    f = open("../DATAcorrected.db", "xt")
    f.close()
except:
    print("\nDelete DATAcorrected.db in order to use the program")
    sys.exit()

db = sqlite3.connect("../DATAcorrected.db")
db.execute("""
    CREATE TABLE IF NOT EXISTS data (
        matchId INT, 
        win BIT, 
        duration INT, 
        
        champIdA1 INT, 
        roleA1 INT, 
        killsA1 INT, deathsA1 INT, assistsA1 INT, 
        keyRuneA1 INT, 
        spell1A1 INT, spell2A1 INT, 
        ccStatA1 INT, ccTimeA1 INT,
        visionScoreA1 INT, wardsPlacedA1 INT, wardsKilledA1 INT, 
        healingA1 INT, 
        damageTakenA1 INT, mitigatedA1 INT, 
        totalDealtA1 INT, totalMagicA1 INT, 
        champsDealtA1 INT, champsMagicA1 INT, 
        turretsDealtA1 INT, objectiveDealtA1 INT, 
        csA1 INT, csJunStolenA1 INT, 
        turretKA1 INT, inhibKA1 INT, 
        goldA1 INT, 
        xpD0_10A1 INT, xpD10_20A1 INT, xpD20_30A1 INT, xpD30_endA1 INT, 
        xpDiffD0_10A1 INT, xpDiffD10_20A1 INT, xpDiffD20_30A1 INT, xpDiffD30_endA1 INT, 
        csD0_10A1 INT, csD10_20A1 INT, csD20_30A1 INT, csD30_endA1 INT, 
        csDiffD0_10A1 INT, csDiffD10_20A1 INT, csDiffD20_30A1 INT, csDiffD30_endA1 INT, 
        goldD0_10A1 INT, goldD10_20A1 INT, goldD20_30A1 INT, goldD30_endA1 INT, 
        takenD0_10A1 INT, takenD10_20A1 INT, takenD20_30A1 INT, takenD30_endA1 INT, 
        dealtD0_10A1 INT, dealtD10_20A1 INT, dealtD20_30A1 INT, dealtD30_endA1 INT, 
        
        champIdA2 INT, 
        roleA2 INT, 
        killsA2 INT, deathsA2 INT, assistsA2 INT, 
        keyRuneA2 INT, 
        spell1A2 INT, spell2A2 INT, 
        ccStatA2 INT, ccTimeA2 INT,
        visionScoreA2 INT, wardsPlacedA2 INT, wardsKilledA2 INT, 
        healingA2 INT, 
        damageTakenA2 INT, mitigatedA2 INT, 
        totalDealtA2 INT, totalMagicA2 INT, 
        champsDealtA2 INT, champsMagicA2 INT, 
        turretsDealtA2 INT, objectiveDealtA2 INT, 
        csA2 INT, csJunStolenA2 INT, 
        turretKA2 INT, inhibKA2 INT, 
        goldA2 INT, 
        xpD0_10A2 INT, xpD10_20A2 INT, xpD20_30A2 INT, xpD30_endA2 INT, 
        xpDiffD0_10A2 INT, xpDiffD10_20A2 INT, xpDiffD20_30A2 INT, xpDiffD30_endA2 INT, 
        csD0_10A2 INT, csD10_20A2 INT, csD20_30A2 INT, csD30_endA2 INT, 
        csDiffD0_10A2 INT, csDiffD10_20A2 INT, csDiffD20_30A2 INT, csDiffD30_endA2 INT, 
        goldD0_10A2 INT, goldD10_20A2 INT, goldD20_30A2 INT, goldD30_endA2 INT, 
        takenD0_10A2 INT, takenD10_20A2 INT, takenD20_30A2 INT, takenD30_endA2 INT, 
        dealtD0_10A2 INT, dealtD10_20A2 INT, dealtD20_30A2 INT, dealtD30_endA2 INT, 
        
        champIdA3 INT, 
        roleA3 INT, 
        killsA3 INT, deathsA3 INT, assistsA3 INT, 
        keyRuneA3 INT, 
        spell1A3 INT, spell2A3 INT, 
        ccStatA3 INT, ccTimeA3 INT,
        visionScoreA3 INT, wardsPlacedA3 INT, wardsKilledA3 INT, 
        healingA3 INT, 
        damageTakenA3 INT, mitigatedA3 INT, 
        totalDealtA3 INT, totalMagicA3 INT, 
        champsDealtA3 INT, champsMagicA3 INT, 
        turretsDealtA3 INT, objectiveDealtA3 INT, 
        csA3 INT, csJunStolenA3 INT, 
        turretKA3 INT, inhibKA3 INT, 
        goldA3 INT, 
        xpD0_10A3 INT, xpD10_20A3 INT, xpD20_30A3 INT, xpD30_endA3 INT, 
        xpDiffD0_10A3 INT, xpDiffD10_20A3 INT, xpDiffD20_30A3 INT, xpDiffD30_endA3 INT, 
        csD0_10A3 INT, csD10_20A3 INT, csD20_30A3 INT, csD30_endA3 INT, 
        csDiffD0_10A3 INT, csDiffD10_20A3 INT, csDiffD20_30A3 INT, csDiffD30_endA3 INT, 
        goldD0_10A3 INT, goldD10_20A3 INT, goldD20_30A3 INT, goldD30_endA3 INT, 
        takenD0_10A3 INT, takenD10_20A3 INT, takenD20_30A3 INT, takenD30_endA3 INT, 
        dealtD0_10A3 INT, dealtD10_20A3 INT, dealtD20_30A3 INT, dealtD30_endA3 INT, 
        
        champIdA4 INT, 
        roleA4 INT, 
        killsA4 INT, deathsA4 INT, assistsA4 INT, 
        keyRuneA4 INT, 
        spell1A4 INT, spell2A4 INT, 
        ccStatA4 INT, ccTimeA4 INT,
        visionScoreA4 INT, wardsPlacedA4 INT, wardsKilledA4 INT, 
        healingA4 INT, 
        damageTakenA4 INT, mitigatedA4 INT, 
        totalDealtA4 INT, totalMagicA4 INT, 
        champsDealtA4 INT, champsMagicA4 INT, 
        turretsDealtA4 INT, objectiveDealtA4 INT, 
        csA4 INT, csJunStolenA4 INT, 
        turretKA4 INT, inhibKA4 INT, 
        goldA4 INT, 
        xpD0_10A4 INT, xpD10_20A4 INT, xpD20_30A4 INT, xpD30_endA4 INT, 
        xpDiffD0_10A4 INT, xpDiffD10_20A4 INT, xpDiffD20_30A4 INT, xpDiffD30_endA4 INT, 
        csD0_10A4 INT, csD10_20A4 INT, csD20_30A4 INT, csD30_endA4 INT, 
        csDiffD0_10A4 INT, csDiffD10_20A4 INT, csDiffD20_30A4 INT, csDiffD30_endA4 INT, 
        goldD0_10A4 INT, goldD10_20A4 INT, goldD20_30A4 INT, goldD30_endA4 INT, 
        takenD0_10A4 INT, takenD10_20A4 INT, takenD20_30A4 INT, takenD30_endA4 INT, 
        dealtD0_10A4 INT, dealtD10_20A4 INT, dealtD20_30A4 INT, dealtD30_endA4 INT, 
        
        champIdA5 INT, 
        roleA5 INT, 
        killsA5 INT, deathsA5 INT, assistsA5 INT, 
        keyRuneA5 INT, 
        spell1A5 INT, spell2A5 INT, 
        ccStatA5 INT, ccTimeA5 INT,
        visionScoreA5 INT, wardsPlacedA5 INT, wardsKilledA5 INT, 
        healingA5 INT, 
        damageTakenA5 INT, mitigatedA5 INT, 
        totalDealtA5 INT, totalMagicA5 INT, 
        champsDealtA5 INT, champsMagicA5 INT, 
        turretsDealtA5 INT, objectiveDealtA5 INT, 
        csA5 INT, csJunStolenA5 INT, 
        turretKA5 INT, inhibKA5 INT, 
        goldA5 INT, 
        xpD0_10A5 INT, xpD10_20A5 INT, xpD20_30A5 INT, xpD30_endA5 INT, 
        xpDiffD0_10A5 INT, xpDiffD10_20A5 INT, xpDiffD20_30A5 INT, xpDiffD30_endA5 INT, 
        csD0_10A5 INT, csD10_20A5 INT, csD20_30A5 INT, csD30_endA5 INT, 
        csDiffD0_10A5 INT, csDiffD10_20A5 INT, csDiffD20_30A5 INT, csDiffD30_endA5 INT, 
        goldD0_10A5 INT, goldD10_20A5 INT, goldD20_30A5 INT, goldD30_endA5 INT, 
        takenD0_10A5 INT, takenD10_20A5 INT, takenD20_30A5 INT, takenD30_endA5 INT, 
        dealtD0_10A5 INT, dealtD10_20A5 INT, dealtD20_30A5 INT, dealtD30_endA5 INT,
        
        champIdE1 INT, 
        roleE1 INT, 
        killsE1 INT, deathsE1 INT, assistsE1 INT, 
        keyRuneE1 INT, 
        spell1E1 INT, spell2E1 INT, 
        ccStatE1 INT, ccTimeE1 INT,
        visionScoreE1 INT, wardsPlacedE1 INT, wardsKilledE1 INT, 
        healingE1 INT, 
        damageTakenE1 INT, mitigatedE1 INT, 
        totalDealtE1 INT, totalMagicE1 INT, 
        champsDealtE1 INT, champsMagicE1 INT, 
        turretsDealtE1 INT, objectiveDealtE1 INT, 
        csE1 INT, csJunStolenE1 INT, 
        turretKE1 INT, inhibKE1 INT, 
        goldE1 INT, 
        xpD0_10E1 INT, xpD10_20E1 INT, xpD20_30E1 INT, xpD30_endE1 INT, 
        xpDiffD0_10E1 INT, xpDiffD10_20E1 INT, xpDiffD20_30E1 INT, xpDiffD30_endE1 INT, 
        csD0_10E1 INT, csD10_20E1 INT, csD20_30E1 INT, csD30_endE1 INT, 
        csDiffD0_10E1 INT, csDiffD10_20E1 INT, csDiffD20_30E1 INT, csDiffD30_endE1 INT, 
        goldD0_10E1 INT, goldD10_20E1 INT, goldD20_30E1 INT, goldD30_endE1 INT, 
        takenD0_10E1 INT, takenD10_20E1 INT, takenD20_30E1 INT, takenD30_endE1 INT, 
        dealtD0_10E1 INT, dealtD10_20E1 INT, dealtD20_30E1 INT, dealtD30_endE1 INT,
        
        champIdE2 INT, 
        roleE2 INT, 
        killsE2 INT, deathsE2 INT, assistsE2 INT, 
        keyRuneE2 INT, 
        spell1E2 INT, spell2E2 INT, 
        ccStatE2 INT, ccTimeE2 INT,
        visionScoreE2 INT, wardsPlacedE2 INT, wardsKilledE2 INT, 
        healingE2 INT, 
        damageTakenE2 INT, mitigatedE2 INT, 
        totalDealtE2 INT, totalMagicE2 INT, 
        champsDealtE2 INT, champsMagicE2 INT, 
        turretsDealtE2 INT, objectiveDealtE2 INT, 
        csE2 INT, csJunStolenE2 INT, 
        turretKE2 INT, inhibKE2 INT, 
        goldE2 INT, 
        xpD0_10E2 INT, xpD10_20E2 INT, xpD20_30E2 INT, xpD30_endE2 INT, 
        xpDiffD0_10E2 INT, xpDiffD10_20E2 INT, xpDiffD20_30E2 INT, xpDiffD30_endE2 INT, 
        csD0_10E2 INT, csD10_20E2 INT, csD20_30E2 INT, csD30_endE2 INT, 
        csDiffD0_10E2 INT, csDiffD10_20E2 INT, csDiffD20_30E2 INT, csDiffD30_endE2 INT, 
        goldD0_10E2 INT, goldD10_20E2 INT, goldD20_30E2 INT, goldD30_endE2 INT, 
        takenD0_10E2 INT, takenD10_20E2 INT, takenD20_30E2 INT, takenD30_endE2 INT, 
        dealtD0_10E2 INT, dealtD10_20E2 INT, dealtD20_30E2 INT, dealtD30_endE2 INT, 
        
        champIdE3 INT, 
        roleE3 INT, 
        killsE3 INT, deathsE3 INT, assistsE3 INT, 
        keyRuneE3 INT, 
        spell1E3 INT, spell2E3 INT, 
        ccStatE3 INT, ccTimeE3 INT,
        visionScoreE3 INT, wardsPlacedE3 INT, wardsKilledE3 INT, 
        healingE3 INT, 
        damageTakenE3 INT, mitigatedE3 INT, 
        totalDealtE3 INT, totalMagicE3 INT, 
        champsDealtE3 INT, champsMagicE3 INT, 
        turretsDealtE3 INT, objectiveDealtE3 INT, 
        csE3 INT, csJunStolenE3 INT, 
        turretKE3 INT, inhibKE3 INT, 
        goldE3 INT, 
        xpD0_10E3 INT, xpD10_20E3 INT, xpD20_30E3 INT, xpD30_endE3 INT, 
        xpDiffD0_10E3 INT, xpDiffD10_20E3 INT, xpDiffD20_30E3 INT, xpDiffD30_endE3 INT, 
        csD0_10E3 INT, csD10_20E3 INT, csD20_30E3 INT, csD30_endE3 INT, 
        csDiffD0_10E3 INT, csDiffD10_20E3 INT, csDiffD20_30E3 INT, csDiffD30_endE3 INT, 
        goldD0_10E3 INT, goldD10_20E3 INT, goldD20_30E3 INT, goldD30_endE3 INT, 
        takenD0_10E3 INT, takenD10_20E3 INT, takenD20_30E3 INT, takenD30_endE3 INT, 
        dealtD0_10E3 INT, dealtD10_20E3 INT, dealtD20_30E3 INT, dealtD30_endE3 INT, 
        
        champIdE4 INT, 
        roleE4 INT, 
        killsE4 INT, deathsE4 INT, assistsE4 INT, 
        keyRuneE4 INT, 
        spell1E4 INT, spell2E4 INT, 
        ccStatE4 INT, ccTimeE4 INT,
        visionScoreE4 INT, wardsPlacedE4 INT, wardsKilledE4 INT, 
        healingE4 INT, 
        damageTakenE4 INT, mitigatedE4 INT, 
        totalDealtE4 INT, totalMagicE4 INT, 
        champsDealtE4 INT, champsMagicE4 INT, 
        turretsDealtE4 INT, objectiveDealtE4 INT, 
        csE4 INT, csJunStolenE4 INT, 
        turretKE4 INT, inhibKE4 INT, 
        goldE4 INT, 
        xpD0_10E4 INT, xpD10_20E4 INT, xpD20_30E4 INT, xpD30_endE4 INT, 
        xpDiffD0_10E4 INT, xpDiffD10_20E4 INT, xpDiffD20_30E4 INT, xpDiffD30_endE4 INT, 
        csD0_10E4 INT, csD10_20E4 INT, csD20_30E4 INT, csD30_endE4 INT, 
        csDiffD0_10E4 INT, csDiffD10_20E4 INT, csDiffD20_30E4 INT, csDiffD30_endE4 INT, 
        goldD0_10E4 INT, goldD10_20E4 INT, goldD20_30E4 INT, goldD30_endE4 INT, 
        takenD0_10E4 INT, takenD10_20E4 INT, takenD20_30E4 INT, takenD30_endE4 INT, 
        dealtD0_10E4 INT, dealtD10_20E4 INT, dealtD20_30E4 INT, dealtD30_endE4 INT, 
        
        champIdE5 INT, 
        roleE5 INT, 
        killsE5 INT, deathsE5 INT, assistsE5 INT, 
        keyRuneE5 INT, 
        spell1E5 INT, spell2E5 INT, 
        ccStatE5 INT, ccTimeE5 INT,
        visionScoreE5 INT, wardsPlacedE5 INT, wardsKilledE5 INT, 
        healingE5 INT, 
        damageTakenE5 INT, mitigatedE5 INT, 
        totalDealtE5 INT, totalMagicE5 INT, 
        champsDealtE5 INT, champsMagicE5 INT, 
        turretsDealtE5 INT, objectiveDealtE5 INT, 
        csE5 INT, csJunStolenE5 INT, 
        turretKE5 INT, inhibKE5 INT, 
        goldE5 INT, 
        xpD0_10E5 INT, xpD10_20E5 INT, xpD20_30E5 INT, xpD30_endE5 INT, 
        xpDiffD0_10E5 INT, xpDiffD10_20E5 INT, xpDiffD20_30E5 INT, xpDiffD30_endE5 INT, 
        csD0_10E5 INT, csD10_20E5 INT, csD20_30E5 INT, csD30_endE5 INT, 
        csDiffD0_10E5 INT, csDiffD10_20E5 INT, csDiffD20_30E5 INT, csDiffD30_endE5 INT, 
        goldD0_10E5 INT, goldD10_20E5 INT, goldD20_30E5 INT, goldD30_endE5 INT, 
        takenD0_10E5 INT, takenD10_20E5 INT, takenD20_30E5 INT, takenD30_endE5 INT, 
        dealtD0_10E5 INT, dealtD10_20E5 INT, dealtD20_30E5 INT, dealtD30_endE5 INT
    );
    """)

print("Database created", round(time.time()-bTime, 3), "seconds")
bTime = time.time()

db2 = sqlite3.connect("../DATA.db")
output = db2.execute("SELECT * FROM data").fetchall()
db2.close()

print("Old database loaded", round(time.time()-bTime, 3), "seconds")
bTime = time.time()

table = pd.read_csv("correctedData.csv", low_memory=False)
array = table.values.tolist()

for team in array:
    output[ team[1]-1 ] = list(output[ team[1]-1 ])
    for i in range(5):
        output[ team[1]-1 ][ 4 + 275*team[0] + 55*i ] = team[ i+2 ]
    output[ team[1]-1 ] = tuple(output[ team[1]-1 ])

print("Contents updated", round(time.time()-bTime, 3), "seconds")
bTime = time.time()

db.executemany("""
    INSERT INTO data VALUES (
        ?, ?, ?,
        
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    );
""", output )

db.commit()
db.close()

print("Done!", round(time.time()-bTime, 3), "seconds")
