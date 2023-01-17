import sqlite3

# creates new database
db = sqlite3.connect("C:\\Users\\joani\\Documents\\HyperionDev\\T47\\database.db")

# creates cursor object
cursor = db.cursor()

# drops any tables from previous running
cursor.execute("""DROP TABLE python_programming""")

# creates python_programming table in database
cursor.execute("""
CREATE TABLE python_programming (
ID int NOT NULL,
NAME varchar(30),
GRADE int(3)
)
""")

# commits database changes
db.commit()

# stores data as tuples, then lists these in entries var
row1 = (55, "Carl Davis", 61)
row2 = (66, "Dennis Fredrickson", 88)
row3 = (77, "Jane Richards", 78)
row4 = (12, "Peyton Sawyer", 45)
row5 = (2, "Lucas Brooke", 99)

entries = [row1, row2, row3, row4, row5]

# adds entries to table
cursor.executemany("""
INSERT INTO python_programming
VALUES (?,?,?) """, entries)

# selects all entries where grade is between 60 and 80
cursor.execute("""SELECT * FROM python_programming
WHERE GRADE>60 AND GRADE<80""")
print(cursor.fetchall())

# sets Carl Davis's grade to 65
cursor.execute("""UPDATE python_programming
SET GRADE=65
WHERE NAME='Carl Davis'""")

# deletes Dennis Fredrickson's row
cursor.execute("""DELETE FROM python_programming
WHERE ID=66""")

# changes the grade of all people with ID below 55
cursor.execute("""UPDATE python_programming
SET GRADE=100
WHERE ID<55
""")

# prints entire table to show changes
cursor.execute("SELECT * FROM python_programming")
print(cursor.fetchall())

db.commit()
db.close()

