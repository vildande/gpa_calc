# GPA Calculator


## How it works
A flask app read the data from sqlite database, calculates gpa and displays info through index.html.


## How to use

First, you need a database with data
### Database
Create SQLITE database. In the scripts folder, there's db.py that creates the database for you.

The database structure is as follows:
Semesters
    id
    name - name for the semester, e.g. Fall 2023

Courses
    id
    name - name for the course, e.g. MATH 101
    credits - amounts of credits for the course, e.g. 2, 6, 8.

Semesters_courses - multiple semesters that have multiple courses
    id
    semester_id
    course_id
    grade - the grade for the course, in scale from 0 to 4, e.g.  2.33, 3.67, 4


Fill this database however you like. This info will be used to calculate the gpa.

// the default name for the database file is gpa_database.db
// your db file should be in the same folder as app.py



## Run the app
Run app.py 

app.py will run a flask server at 127.0.0.1:5000. 

Open localhost:5000 in browser.

You'll see a webpage with your 'transript' and gpa calculated.






