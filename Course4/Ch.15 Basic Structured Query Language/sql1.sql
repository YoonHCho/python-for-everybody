-- to Create a table
CREATE TABLE Users (
  name VARCHAR(128)
  email VARCHAR(128)
)


-- to insert a new user
INSERT INTO Users (name, email)
VALUES            ('New', 'new@new.com')

-- to delete a user
DELETE FROM Users
WHERE       email='what@what.com'

-- to update a user
UPDATE Users
SET         name='Molla'
WHERE       email='me@me.com'

-- to retrieve records * means all the columns or you can specify columns?
SELECT * FROM Users
WHERE         email='them@them.com'

-- to sort the data ORDER BY
SELECT * FROM Users
ORDER BY      email

SELECT * FROM Users
ORDER BY      name