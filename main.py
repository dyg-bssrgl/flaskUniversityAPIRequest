from flask import Flask, jsonify
import pandas as pd
import ast

app = Flask(__name__)

num_terms = 8

# CSV dosyalarını yükle
students_df = pd.read_csv('university_students.csv')
courses_df = pd.read_csv('courses.csv')

# Fakülteler ve bölümleri
faculties = {
    'engineering': ['computer', 'electronics', 'civil'],
    'science': ['psychology', 'maths', 'physics'],
    'education': ['mathsteaching', 'physicsteaching', 'literatureteaching']
}


@app.route('/faculties', strict_slashes=False, methods=['GET'])
def get_faculties():
    faculties_info = {}
    for faculty, departments in faculties.items():
        faculties_info[faculty] = {dept: f"/faculties/{faculty}/{dept}" for dept in departments}
    return jsonify(faculties_info)


@app.route('/faculties/<faculty>/<department>', strict_slashes=False, methods=['GET'])
def get_department_info(faculty, department):
    department_info = {}
    for term in range(1, num_terms + 1):
        term_key = f'Term {term}'
        term_courses = courses_df[(courses_df['Department'] == department) & (courses_df['Term'] == term_key)]
        student_count = term_courses['Student_IDs']
        flattened_list = []
        for item in student_count:
            flattened_list.append(item)
        flattened_list2 = flattened_list[0].split(',')
        department_info[term_key] = {
            'student_count': len(flattened_list2),
            'course_count': len(term_courses),
            'link': f"/faculties/{faculty}/{department}/{term_key}"
        }
    return jsonify(department_info)


@app.route('/faculties/<faculty>/<department>/<term>', strict_slashes=False, methods=['GET'])
def get_term_courses(faculty, department, term):
    term_courses_info = courses_df[(courses_df['Department'] == department) & (courses_df['Term'] == term)].to_dict(
        orient='records')
    for course in term_courses_info:
        student_ids_str = courses_df.loc[(courses_df['Department'] == department) & (courses_df['Term'] == term) & (
                    courses_df['Course_ID'] == course['Course_ID']), 'Student_IDs'].iloc[0]
        student_ids_list = ast.literal_eval(student_ids_str)
        course['student_count'] = len(student_ids_list)
        course['link'] = f"/faculties/{faculty}/{department}/{term}/{course['Course_ID']}"
    return jsonify(term_courses_info)


@app.route('/faculties/<faculty>/<department>/<term>/<course_id>', strict_slashes=False, methods=['GET'])
def get_course_students(faculty, department, term, course_id):
    course_students = courses_df[courses_df['Course_ID'] == course_id]['Student_IDs'].iloc[0]
    # course_students'ı liste olarak işle
    if isinstance(course_students, str):
        course_students = ast.literal_eval(course_students)  # String'i liste olarak değerlendir
    students_info = students_df[students_df['Student_ID'].isin(course_students)].to_dict(orient='records')
    return jsonify(students_info)


if __name__ == '__main__':
    app.run(debug=True)
