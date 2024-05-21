# creates sqlite database for the info about semesters, courses, credits, grades

import sqlite3

def create_database():
    conn = sqlite3.connect('gpa_database.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS semesters
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS courses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 credits INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS Semester_Course
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 semester_id INTEGER,
                 course_id INTEGER,
                 grade REAL,
                 FOREIGN KEY (semester_id) REFERENCES semesters(id),
                 FOREIGN KEY (course_id) REFERENCES courses(id))''')
    
    conn.commit()
    conn.close()




create_database()
