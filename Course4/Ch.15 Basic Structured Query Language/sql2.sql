-- create Artist table
CREATE TABLE "Artist" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- create Genre
CREATE TABLE Genre (
  id INTEGER NOT BULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name TEXT
)

-- create Album
CREATE TABLE Album (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  artist_id INTEGER,
  title TEXT
)

-- create Track
CREATE TABLE Track (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title TEXT,
  album_id INTEGER,
  genre_id INTEGER,
  len INTEGER, rating INTEGER, count INTEGER
)

-- below are some example sql (exercise done in SQLite Browser)
INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1)

INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Black Dog', 5, 297, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Stairway', 5, 482, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('About to Rock', 5, 356, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Who We Are', 5, 412, 0, 2, 1)