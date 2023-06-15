'''
Musical Track Database
This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml file to be used for this assignment. You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the Library.xml data that is provided.

To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)

Track	                                    Artist	            Album	              Genre
Chase the Ace	                            AC/DC	              Who Made Who	      Rock
D.T.	                                    AC/DC	              Who Made Who	      Rock
For Those About To Rock (We Salute You)	  AC/DC	              Who Made Who	      Rock
'''

# import to parse and manipulate XML data
import xml.etree.ElementTree as ET
# to interact with SQLite
import sqlite3

conn = sqlite3.connect('assignment_track.sqlite')
cur = conn.cursor()

# Delete table if already exists, and create new TABLEs
# use executescript to do multiple scripts
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fileName = input("Enter file name: ")
if len(fileName) < 1:
    fileName = 'Library.xml'

# example of how Library.xml looks
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


parsedXML = ET.parse(fileName)
# includes the third dict and its children
neededData = parsedXML.findall('dict/dict/dict')
print('Dict Count: ', len(neededData))

for track in neededData:
    if (lookup(track, 'Track ID') is None):
        continue

    artist = lookup(track, 'Artist')
    genre = lookup(track, 'Genre')
    album = lookup(track, 'Album')
    title = lookup(track, 'Name')
    len = lookup(track, 'Total Time')
    rating = lookup(track, 'Rating')
    count = lookup(track, 'Play Count')

    # if title is None or artist is None or album is None or genre is None:
    #     continue
    # better way to write above
    if any(value is None for value in (title, artist, album, genre)):
        continue
    # print(f"{title}, {artist}, {album}, {genre}")

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    # fetchone() returns a tuple if data, but None if no data
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute(
        'INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)', (artist_id, album,))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute(
        'INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)', (title, album_id, genre_id, len, rating, count))

    conn.commit()
