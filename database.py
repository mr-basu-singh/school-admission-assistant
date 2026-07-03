import sqlite3

conn = sqlite3.connect("database/school.db")
cursor = conn.cursor()

# -------------------------
# Create Tables
# -------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS fees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade TEXT,
    admission_fee INTEGER,
    annual_fee INTEGER,
    transport_fee INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS seats(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade TEXT,
    available_seats INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transport(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    area TEXT,
    available TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS faq(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS campus_visit(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT,
    slots INTEGER
)
""")

# -------------------------
# Clear old data
# -------------------------

cursor.execute("DELETE FROM fees")
cursor.execute("DELETE FROM seats")
cursor.execute("DELETE FROM transport")
cursor.execute("DELETE FROM faq")
cursor.execute("DELETE FROM campus_visit")

# -------------------------
# Fees
# -------------------------

fees = [
("Grade 1",20000,60000,18000),
("Grade 2",20000,62000,18000),
("Grade 3",20000,65000,18000),
("Grade 4",20000,68000,18000),
("Grade 5",20000,72000,18000),
("Grade 6",25000,78000,20000),
("Grade 7",25000,80000,20000),
("Grade 8",25000,82000,20000),
("Grade 9",30000,90000,22000),
("Grade 10",30000,95000,22000),
("Grade 11",35000,110000,25000),
("Grade 12",35000,115000,25000)
]

cursor.executemany("""
INSERT INTO fees(
grade,
admission_fee,
annual_fee,
transport_fee
)
VALUES(?,?,?,?)
""", fees)

# -------------------------
# Seats
# -------------------------

seats = [
("Grade 1",18),
("Grade 2",12),
("Grade 3",6),
("Grade 4",8),
("Grade 5",4),
("Grade 6",10),
("Grade 7",15),
("Grade 8",7),
("Grade 9",3),
("Grade 10",5),
("Grade 11",9),
("Grade 12",11)
]

cursor.executemany("""
INSERT INTO seats(
grade,
available_seats
)
VALUES(?,?)
""", seats)

# -------------------------
# Transport
# -------------------------

transport = [
("Noida Sector 62","Yes"),
("Noida Sector 18","Yes"),
("Greater Noida","Yes"),
("Ghaziabad","Yes"),
("Indirapuram","Yes"),
("Delhi NCR","No")
]

cursor.executemany("""
INSERT INTO transport(
area,
available
)
VALUES(?,?)
""", transport)

# -------------------------
# FAQ
# -------------------------

faq = [
("What is the admission process?",
"Submit application, verify documents, attend interaction, pay fees."),
("What documents are required?",
"Birth Certificate, Aadhaar Card, Passport Photos, Previous Report Card."),
("Can parents visit the campus?",
"Yes. Campus visits can be booked online.")
]

cursor.executemany("""
INSERT INTO faq(
question,
answer
)
VALUES(?,?)
""", faq)

# -------------------------
# Campus Visit
# -------------------------

visits = [
("Monday",20),
("Tuesday",20),
("Wednesday",15),
("Thursday",20),
("Friday",20),
("Saturday",10)
]

cursor.executemany("""
INSERT INTO campus_visit(
day,
slots
)
VALUES(?,?)
""", visits)

conn.commit()

print("Database Created Successfully!")

conn.close()