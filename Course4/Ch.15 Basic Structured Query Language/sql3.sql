-- Many to Many Relationship
-- All work done in DB Browwer for SQLite
CREATE TABLE User (
  id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name    TEXT,
  email   TEXT
)

CREATE TABLE Course (
  id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title   TEXT
)

CREATE TABLE Member (
  user_id     INTEGER,
  course_id   INTEGER,
  role        INTEGER,
  PRIMARY KEY (user_id, course_id)
)

/*
You can only have 1 Primary key in a table because it needs to be unique.
however, it is possible to have a COMPOSITE primary key.
which consists of multiple columns. This means that the combination of values from these columns
must be unique within the table, but each individual column may contain duplicate values. Example:

| StudentID | CourseID | Grade |
|-----------|----------|-------|
| 1         | 101      | A     |
| 1         | 102      | B     |
| 2         | 101      | A-    |
| 3         | 102      | C+    |

*/

-- User table
INSERT INTO User (name, email) VALUES ('Jane', 'jane@fake.com')
INSERT INTO User (name, email) VALUES ('Ed', 'ed@fake.com')
INSERT INTO User (name, email) VALUES ('Sue', 'sue@fake.com')

-- Course table
INSERT INTO Course (title) VALUES ('Python')
INSERT INTO Course (title) VALUES ('SQL')
INSERT INTO Course (title) VALUES ('PHP')

-- Member table
INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1)
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0)
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0)

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0)
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1)

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1)
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0)

-- get data
SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name
