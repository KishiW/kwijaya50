'''
Tawab Berri
The Duo-lingos - Tawab Berri, Jacob Lukose, Jack Blair
SoftDev
2024-10-18
K19 - SQLite basics
time spent: 2.8 hrs
'''
import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

import pprint as p


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
students = []
courses = []
with open('students.csv', 'r') as f:
    read = csv.DictReader(f)
    for row in read:
        students.append(row)
        print(row)

with open('courses.csv', 'r') as ftwo:
    readtwo = csv.DictReader(ftwo)
    for row in readtwo:
        courses.append(row)
p.pprint(students)
p.pprint(courses)

c.execute("CREATE TABLE students (code TEXT, mark INTEGER, id INTEGER PRIMARY KEY)")
for i in students:
    name = i['name']
    age = int(i['age'])
    id = int(i['id'])
    c.execute(f"INSERT INTO students VALUES ({name}, {age}, {id})")

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
for i in courses:
    code = i['code']
    mark = int(i['mark'])
    id = int(i['id'])
    c.execute(f"INSERT INTO courses VALUES ({code}, {mark}, {id})")

#==========================================================

db.commit() #save changes
db.close()  #close database
