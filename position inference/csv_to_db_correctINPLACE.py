import numpy as np
import sqlite3
import pandas as pd
import time
import sys

bTime = time.time()

table = pd.read_csv("correctedData.csv", low_memory=False)
array = table.values[:,[0, 2, 3, 4, 5, 6, 1]].tolist()

print("CSV readed", round(time.time()-bTime, 3), "seconds")
bTime = time.time()

try:
    db = sqlite3.connect("../DATAcorrected.db")
except:
    print("Do a copy of your current file DATA.db called DATAcorrected.db (this is done to ensure no data is lost (incorrect data btw haha))")

for team in array:
    if team[0] == 0:
        db.execute("UPDATE data SET roleA1 = ?, roleA2 = ?, roleA3 = ?, roleA4 = ?, roleA5 = ? WHERE ROWID = ?;", team[1:])
    else:
        db.execute("UPDATE data SET roleE1 = ?, roleE2 = ?, roleE3 = ?, roleE4 = ?, roleE5 = ? WHERE ROWID = ?;", team[1:])
        
db.commit()
db.close()

print("Database updated!", round(time.time()-bTime, 3), "seconds")
