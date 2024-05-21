from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__, template_folder='.') # template_folder is the path to the folder with index.html

GPA_DATABASE = 'gpa_database.db' # name of the database file

def fetch_semester_data():
    conn = sqlite3.connect(GPA_DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM semesters")
    semesters = c.fetchall()
    conn.close()
    return semesters

def fetch_courses_for_semester(semester_id):
    conn = sqlite3.connect(GPA_DATABASE)
    c = conn.cursor()
    c.execute("SELECT courses.id, courses.name, courses.credits, Semester_Course.grade FROM courses JOIN Semester_Course ON courses.id = Semester_Course.course_id WHERE Semester_Course.semester_id = ?", (semester_id,))
    courses = c.fetchall()
    conn.close()

    courses_out = []

    for course in courses:
        course_id = course[0]
        course_name = course[1]
        course_credits = course[2]
        course_grade = course[3]
        course_dict = {'id': course_id, 'name': course_name, 'credits': course_credits, 'grade': course_grade}
        courses_out.append(course_dict)

    return courses_out

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_semesters', methods=['GET'])
def get_semesters():
    semesters = fetch_semester_data()
    semesters_with_courses = []

    for semester in semesters:
        semester_id = semester[0]
        semester_name = semester[1]
        courses = fetch_courses_for_semester(semester_id)
        semester_dict = {'id': semester_id, 'name': semester_name, 'courses': courses}
        semesters_with_courses.append(semester_dict)
    
    return jsonify({"semesters": semesters_with_courses})

if __name__ == '__main__':
    app.run(debug=True)
