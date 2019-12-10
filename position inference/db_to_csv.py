import sqlite3
import pandas as pd
import time

#LOAD DATA
bTime = time.time()
db = sqlite3.connect("../DATA.db")

x = []
x.extend(db.execute("""SELECT champIdA1, keyRuneA1, spell1A1, spell2A1, champIdA2, keyRuneA2, spell1A2, spell2A2, champIdA3, keyRuneA3, spell1A3, spell2A3,
                    champIdA4, keyRuneA4, spell1A4, spell2A4, champIdA5, keyRuneA5, spell1A5, spell2A5  FROM data""").fetchall())
x.extend(db.execute("""SELECT champIdE1, keyRuneE1, spell1E1, spell2E1, champIdE2, keyRuneE2, spell1E2, spell2E2, champIdE3, keyRuneE3, spell1E3, spell2E3,
                    champIdE4, keyRuneE4, spell1E4, spell2E4, champIdE5, keyRuneE5, spell1E5, spell2E5  FROM data""").fetchall())

y = []
y.extend(db.execute("SELECT roleA1, roleA2, roleA3, roleA4, roleA5 FROM data").fetchall())
y.extend(db.execute("SELECT roleE1, roleE2, roleE3, roleE4, roleE5 FROM data").fetchall())

db.close()
print("Data loaded, "+str(time.time()-bTime)+"s")


#SELECT GOOD ROWS
bTime = time.time()
to_csv = [["TOPchampId", "TOPkeyRune", "TOPspell1", "TOPspell2", "JNGchampId", "JNGkeyRune", "JNGspell1", "JNGspell2", "MIDchampId", "MIDkeyRune", "MIDspell1", "MIDspell2",
           "ADCchampId", "ADCkeyRune", "ADCspell1", "ADCspell2", "SUPchampId", "SUPkeyRune", "SUPspell1", "SUPspell2"]]

count = 0
for team in range(len(y)):
    check = [0, 0, 0, 0, 0]
    
    for champ in y[team]:
        if champ != -1:
            check[champ] = 1
            
    correct = True
    for pos in check:
        if pos == 0:
            correct = False

    if correct:
        count += 1
        to_csv.append([])
        for i in range(5):
            to_csv[-1].extend(x[team][y[team].index(i)*4:(y[team].index(i)+1)*4])

print(str(count)+"/"+str(len(y)))
print("Data selected, "+str(time.time()-bTime)+"s")

#WRITE GOOD ROWS AS CSV

bTime = time.time()
pd.DataFrame(to_csv).to_csv("positionData.csv", index=False, header=False)

print("CSV written, "+str(time.time()-bTime)+"s")
