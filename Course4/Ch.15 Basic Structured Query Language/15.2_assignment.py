import sqlite3

conn = sqlite3.connect('mbox.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fileName = input("Enter file name: ")
if len(fileName) < 1:
    fileName = 'mbox.txt'

fileHandle = open(fileName)
for line in fileHandle:
    if not line.startswith('From: '):
        continue
    line = line.strip().split()
    index = line[1].index('@')
    org = line[1][index + 1:]
    cur.execute('SELECT count FROM Counts WHERE org= ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (? , 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org= ?', (org,))
    conn.commit()

dataByOrder = 'SELECT * FROM Counts ORDER BY count DESC'

for row in cur.execute(dataByOrder):
    print('{:25s} {:5}'.format(row[0], row[1]))

cur.close()
