'''
This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py - this code is incomplete as you need to modify the program to store the role column in the Member table to complete the assignment.

Each student gets their own file for the assignment. Download this file and save it as roster_data.json. Move the downloaded file into the same folder as your roster.py program.

Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data, run the following SQL command:

SELECT User.name,Course.title, Member.role FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
The output should look as follows:
Zohaib|si363|0
Zoe|si310|0
Once that query gives the correct data, run this query:
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
You should get one row with a string that looks like XYZZY53656C696E613333.
'''

import json
import sqlite3

conn = sqlite3.connect('assignment_json_data.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
  id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name  TEXT UNIQUE
);

CREATE TABLE Course (
  id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title TEXT UNIQUE
);

CREATE TABLE Member (
  user_id     INTEGER,
  course_id   INTEGER,
  role        INTEGER,
  PRIMARY KEY (user_id, course_id)
)
''')

fileName = input("Enter file name or press 'enter': ")
if len(fileName) < 1:
    fileName = 'roster_data.json'

str_data = open(fileName).read()
print(f'There are {len(str_data)} characters')

# Convers str_data to a list
json_data = json.loads(str_data)
'''
for data in json_data:
    name = data[0]
    course = data[1]
    role = data[2]

2 ways to destructure like in JS
for name, course, role in json_data:

for data in json_data:
    name, course, role = data
'''
for name, course, role in json_data:
    # print((name, course, role))

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
    course_id = cur.fetchone()[0]

    cur.execute(
        '''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''', (user_id, course_id, role,))

    conn.commit()

sqlCom1 = '''
SELECT User.name,Course.title, Member.role FROM
User JOIN Member JOIN Course
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
'''
for row in cur.execute(sqlCom1):
    print(f'{row[0]} | {row[1]} | {row[2]}')

sqlCom2 = '''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
User JOIN Member JOIN Course
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1;
'''
for row in cur.execute(sqlCom2):
    print(f'{row[0]}')

cur.close()
