import pandas as pd
import numpy as np
from faker import Faker
import random as rd

fake = Faker()

# Fakülteler bölüm adları oluşturuluyor
faculties = {
    'engineering': ['computer', 'electronics', 'civil'],
    'science': ['psychology', 'maths', 'physics'],
    'education': ['mathsteaching', 'physicsteaching', 'literatureteaching']
}

# Term sayısı, her termdeki ders sayısı belirleniyor
num_terms = 8
num_courses_per_term = 6

# Her bölümün derleri belirleniyor
course_names = {
    'computer': {
        'Term 1': ['Introduction to Computing', 'Programming Fundamentals', 'Web Technologies', 'Computer Ethics',
                   'Discrete Mathematics', 'Digital Design'],
        'Term 2': ['Data Structures', 'Computer Architecture', 'Algorithm Analysis', 'Human-Computer Interaction',
                   'Linear Algebra', 'Database Systems'],
        'Term 3': ['Advanced Programming', 'Operating Systems', 'Computer Networks', 'Software Engineering',
                   'Artificial Intelligence', 'System Security'],
        'Term 4': ['Machine Learning', 'Distributed Systems', 'Mobile Application Development', 'Web Development',
                   'Graphics and Visualization', 'Cryptography'],
        'Term 5': ['Cloud Computing', 'Big Data Analytics', 'Internet of Things', 'Game Development',
                   'Blockchain Technology', 'Cyber-Physical Systems'],
        'Term 6': ['Robotics', 'Quantum Computing', 'Virtual Reality', 'Augmented Reality', 'Computer Vision',
                   'Natural Language Processing'],
        'Term 7': ['Ethical Hacking', 'Advanced Database Systems', 'Wireless Networking', 'Data Mining',
                   'Software Project Management', 'Advanced Algorithms'],
        'Term 8': ['Information Theory and Coding', 'Parallel Computing', 'Humanoid Robots',
                   'Advanced Web Technologies', 'Geographical Information Systems', 'Autonomous Systems']
    },
    'electronics': {
        'Term 1': ['Basic Electronics', 'Circuit Theory', 'Digital Logic Design', 'Electronics Workshop',
                   'Signals and Systems', 'Electromagnetic Fields'],
        'Term 2': ['Analog Circuits', 'Microcontrollers', 'Communication Systems', 'Instrumentation and Measurement',
                   'Control Systems', 'Power Electronics'],
        'Term 3': ['Digital Signal Processing', 'VLSI Design', 'Embedded Systems', 'Optoelectronics',
                   'Radio Frequency Design', 'Renewable Energy Systems'],
        'Term 4': ['Antennas and Wave Propagation', 'Electronic Materials and Devices', 'Microwave Engineering',
                   'Photonics', 'Nanoelectronics', 'Biomedical Electronics'],
        'Term 5': ['Wireless Communication', 'Advanced Control Systems', 'Sensors and Actuators',
                   'Power System Engineering', 'Satellite Communication', 'Optical Communication'],
        'Term 6': ['Radar and Navigation Systems', 'Flexible Electronics', 'Integrated Circuit Design',
                   'Quantum Electronics', 'Robotics and Automation', 'Digital System Design'],
        'Term 7': ['Consumer Electronics', 'Power Quality', 'Energy Harvesting', 'Wireless Sensor Networks',
                   'Electromagnetic Compatibility', 'Analog Signal Processing'],
        'Term 8': ['Smart Grid Technologies', 'High Frequency Circuit Design', 'Neuroengineering',
                   'Internet of Things Applications', 'Automotive Electronics', 'Electronic System Design']
    },
    'civil': {
        'Term 1': ['Civil Engineering Basics', 'Construction Materials', 'Engineering Mechanics',
                   'Environmental Studies', 'Fluid Mechanics', 'Geology'],
        'Term 2': ['Structural Analysis', 'Concrete Technology', 'Geotechnical Engineering',
                   'Hydrology and Water Resources', 'Transportation Engineering', 'Surveying'],
        'Term 3': ['Foundation Engineering', 'Earthquake Engineering', 'Pavement Design', 'Urban Planning',
                   'Traffic Engineering', 'Bridge Engineering'],
        'Term 4': ['Building Technology', 'Water Supply and Waste Water Engineering', 'Soil Mechanics',
                   'Construction Project Management', 'Steel Structures', 'Environmental Impact Assessment'],
        'Term 5': ['Advanced Structural Analysis', 'Hydraulic Structures', 'Reinforced Concrete Design',
                   'Sustainable Construction', 'Coastal Engineering', 'Remote Sensing and GIS'],
        'Term 6': ['Advanced Geotechnical Engineering', 'Building Information Modeling', 'Water Resource Management',
                   'Advanced Transportation Engineering', 'Seismic Design of Structures', 'Green Building Design'],
        'Term 7': ['Construction Economics', 'Land Development Engineering', 'Highway Engineering',
                   'Structural Dynamics', 'Geosynthetics and Reinforced Soil Structures',
                   'Construction Safety and Health'],
        'Term 8': ['Urban Transportation Planning', 'Advanced Environmental Engineering', 'Prestressed Concrete',
                   'Geotechnical Earthquake Engineering', 'Structural Rehabilitation and Retrofitting',
                   'Disaster Risk Management']
    },
    'psychology': {
        'Term 1': ['Introduction to Psychology', 'Biopsychology', 'Research Methods in Psychology',
                   'Developmental Psychology', 'Social Psychology', 'Cognitive Psychology'],
        'Term 2': ['Personality Psychology', 'Abnormal Psychology', 'Psychological Statistics',
                   'Experimental Psychology', 'Psychology of Learning', 'Sensation and Perception'],
        'Term 3': ['Clinical Psychology', 'Counseling Psychology', 'Health Psychology', 'Positive Psychology',
                   'Forensic Psychology', 'Neuropsychology'],
        'Term 4': ['Child and Adolescent Psychology', 'Geropsychology', 'Industrial and Organizational Psychology',
                   'Psychology of Gender', 'Environmental Psychology', 'Cross-Cultural Psychology'],
        'Term 5': ['Sport Psychology', 'Human Sexuality', 'Psychopharmacology', 'Family Therapy',
                   'Psychology of Addiction', 'Educational Psychology'],
        'Term 6': ['Consumer Psychology', 'Psychology of Religion', 'Evolutionary Psychology', 'School Psychology',
                   'Psychology of Creativity', 'Media Psychology'],
        'Term 7': ['Advanced Research Methods', 'Psychology of Emotion', 'History and Systems of Psychology',
                   'Psychology of Language', 'Cognitive Neuroscience', 'Applied Behavior Analysis'],
        'Term 8': ['Independent Study in Psychology', 'Senior Seminar in Psychology', 'Psychology Internship',
                   'Advanced Topics in Psychology', 'Psychology Capstone Project', 'Community Psychology']
    },
    'maths': {
        'Term 1': ['Calculus I', 'Linear Algebra I', 'Discrete Mathematics', 'Probability Theory',
                   'Fundamentals of Mathematical Logic', 'Mathematical Statistics'],
        'Term 2': ['Calculus II', 'Linear Algebra II', 'Real Analysis', 'Complex Analysis', 'Numerical Methods',
                   'Abstract Algebra'],
        'Term 3': ['Calculus III', 'Topology', 'Differential Equations', 'Operations Research', 'Game Theory',
                   'Mathematical Modeling'],
        'Term 4': ['Vector Analysis', 'Group Theory', 'Graph Theory', 'Mathematical Physics', 'Number Theory',
                   'Computational Mathematics'],
        'Term 5': ['Functional Analysis', 'Partial Differential Equations', 'Cryptography', 'Combinatorics',
                   'Statistical Methods', 'Advanced Calculus'],
        'Term 6': ['Measure Theory', 'Rings and Modules', 'Mathematical Finance', 'Algebraic Geometry',
                   'Dynamical Systems', 'Geometric Topology'],
        'Term 7': ['Homological Algebra', 'Complex Variables', 'Mathematical Logic', 'Quantum Computing',
                   'Stochastic Processes', 'Category Theory'],
        'Term 8': ['Advanced Topics in Mathematics', 'Mathematics Education', 'Senior Thesis in Mathematics',
                   'Mathematical Biology', 'Integral Equations', 'Algebraic Topology']
    },
    'physics': {
        'Term 1': ['Mechanics', 'Thermodynamics', 'Electromagnetism', 'Optics', 'Modern Physics',
                   'Computational Physics'],
        'Term 2': ['Quantum Mechanics I', 'Statistical Mechanics', 'Solid State Physics', 'Nuclear Physics',
                   'Classical Mechanics', 'Electronics for Physicists'],
        'Term 3': ['Quantum Mechanics II', 'Particle Physics', 'Electrodynamics', 'Relativity', 'Astrophysics',
                   'Experimental Physics'],
        'Term 4': ['Condensed Matter Physics', 'Plasma Physics', 'Atomic Physics', 'Biophysics', 'Quantum Field Theory',
                   'Theoretical Physics'],
        'Term 5': ['Advanced Quantum Mechanics', 'Advanced Electrodynamics', 'Quantum Optics', 'Cosmology',
                   'Laser Physics', 'Nanophysics'],
        'Term 6': ['High Energy Physics', 'General Relativity', 'Photonics', 'Nuclear and Particle Astrophysics',
                   'Nonlinear Dynamics', 'Environmental Physics'],
        'Term 7': ['Superconductivity', 'Quantum Electronics', 'Astroparticle Physics', 'Fluid Dynamics',
                   'Space Physics', 'Quantum Information Theory'],
        'Term 8': ['Advanced Topics in Physics', 'Physics Education', 'Physics Research Project',
                   'Magnetism and Magnetic Materials', 'Quantum Computation', 'Advanced Statistical Mechanics']
    },
    'mathsteaching': {
        'Term 1': ['Foundations of Mathematics Education', 'Teaching Algebra', 'Educational Psychology',
                   'Curriculum Development', 'Instructional Strategies', 'Assessment in Mathematics Education'],
        'Term 2': ['Teaching Geometry', 'Mathematics and Technology', 'Learning Theories in Mathematics',
                   'Teaching Statistics and Probability', 'Classroom Management',
                   'Diversity and Inclusion in Mathematics'],
        'Term 3': ['Advanced Algebra Teaching', 'Research Methods in Mathematics Education',
                   'Mathematical Problem Solving', 'Teaching Calculus',
                   'Professional Development in Mathematics Education', 'Mathematics Curriculum Analysis'],
        'Term 4': ['Teaching Mathematics in Middle School', 'Teaching Mathematics in High School',
                   'Historical Perspectives in Mathematics Education', 'Special Needs in Mathematics Education',
                   'Mathematics Coaching and Leadership', 'Mathematics Education Policy'],
        'Term 5': ['Assessment Design and Analysis', 'Mathematical Modelling in Education',
                   'Advanced Topics in Mathematics Teaching', 'Teaching and Learning of Algebraic Thinking',
                   'Quantitative Research Methods', 'Mathematics Teacher Education'],
        'Term 6': ['Educational Statistics', 'Teaching Mathematics with Technology',
                   'Comparative Mathematics Education', 'Teaching Mathematics in Diverse Classrooms',
                   'Advanced Geometrical Concepts in Teaching', 'Philosophy of Mathematics Education'],
        'Term 7': ['Mathematics Education Practicum', 'Advanced Research in Mathematics Education',
                   'International Perspectives in Mathematics Education', 'STEM Education and Mathematics',
                   'Quantitative Reasoning in Mathematics', 'Teaching Mathematics Through Problem-Based Learning'],
        'Term 8': ['Capstone Project in Mathematics Education', 'Mathematics Education Seminar',
                   'Ethics in Mathematics Education', 'Contemporary Issues in Mathematics Education',
                   'Mathematics Education Leadership', 'Innovations in Mathematics Teaching']
    },
    'physicsteaching': {
        'Term 1': ['Introduction to Physics Teaching', 'Teaching Mechanics', 'Physics Curriculum and Instruction',
                   'Educational Technology in Physics', 'Pedagogical Content Knowledge for Physics',
                   'Classroom Management in Physics Education'],
        'Term 2': ['Teaching Electromagnetism', 'Physics Education Research Methods', 'Teaching Modern Physics',
                   'Inquiry-Based Physics Education', 'Physics Laboratory Teaching', 'Assessment in Physics Education'],
        'Term 3': ['Teaching Thermodynamics', 'Physics Education and Public Understanding',
                   'Teaching Physics with Simulations', 'Advanced Topics in Physics Teaching', 'Teaching Optics',
                   'Physics Learning Theories'],
        'Term 4': ['Teaching Quantum Physics', 'Physics Teacher Professional Development',
                   'Physics Education Policy and Leadership', 'Teaching Physics in Middle School',
                   'Teaching Physics in High School', 'History and Philosophy of Physics Education'],
        'Term 5': ['Advanced Mechanics in Physics Education', 'Teaching Physics Through Experiments',
                   'STEM Integration in Physics Teaching', 'Physics Education Technology Applications',
                   'Teaching Nuclear and Particle Physics', 'Project-Based Learning in Physics'],
        'Term 6': ['Physics Education Practicum', 'Teaching Astrophysics', 'Environmental Physics Education',
                   'Physics Outreach and Communication', 'Physics Education Seminar',
                   'Advanced Research in Physics Teaching'],
        'Term 7': ['Physics Education Capstone Project', 'Physics Education in Informal Settings',
                   'Physics Education and Society', 'Contemporary Issues in Physics Education',
                   'Physics Teacher Mentorship', 'Physics Education and Global Challenges'],
        'Term 8': ['Physics Education Internship', 'Advanced Laboratory Techniques in Physics Teaching',
                   'Physics Education and Diversity', 'Physics Education and Assessment',
                   'Innovative Teaching Strategies in Physics', 'Physics Education Thesis']
    },
    'literatureteaching': {
        'Term 1': ['Foundations of Literature Education', 'Teaching Poetry', 'Literature and Society',
                   'Instructional Strategies in Literature', 'Adolescent Literature',
                   'Literature Curriculum Development'],
        'Term 2': ['Teaching Prose and Fiction', 'Literature Education Research Methods', 'Teaching Drama and Theater',
                   'Literature Education and Technology', 'Literature in Diverse Classrooms',
                   'Assessment in Literature Education'],
        'Term 3': ['Teaching World Literature', 'Children’s Literature in Education',
                   'Literature Education Policy and Leadership', 'Literary Theory and Criticism in Education',
                   'Creative Writing in Teaching', 'Literature Education and Public Understanding'],
        'Term 4': ['Teaching American Literature', 'Teaching British Literature', 'Literature Education and Ethics',
                   'Comparative Literature in Education', 'Young Adult Literature', 'Literature Education Practicum'],
        'Term 5': ['Teaching Non-Western Literature', 'Advanced Topics in Literature Teaching',
                   'Literature Education and Global Perspectives', 'Teaching Literature Through Film',
                   'Contemporary Literature in Education', 'Literature Education Seminar'],
        'Term 6': ['Literature Education Research Project', 'Teaching Shakespeare',
                   'Multimodal Literacies in Literature Education', 'Literature Education and Social Justice',
                   'Teaching Literature to English Language Learners', 'Literature Education Capstone Project'],
        'Term 7': ['Literature Education and Special Needs', 'Teaching Literary Genres',
                   'Literature Education and Critical Pedagogy', 'Digital Humanities in Literature Education',
                   'Teaching Literary Analysis', 'Literature Education Policy Analysis'],
        'Term 8': ['Literature Education Thesis', 'Advanced Literary Theories in Education',
                   'Teaching Literature and Media', 'Literature Education Internship',
                   'Contemporary Issues in Literature Education', 'Literature Education and Community Engagement']
    }
}


student_id = 10000

# Öğrenciler oluşturulup random fakülte ve bölüme atanıyor
students = [{'Student_ID': fake.unique.random_int(min=student_id, max=99999),
             'Name': fake.name(),
             'Average': round(np.random.uniform(60.0, 100.0), 2),
             'Department': np.random.choice([dept for sub in faculties.values() for dept in sub]),
             'Term': np.random.choice([f'Term {i + 1}' for i in range(num_terms)])}
            for _ in range(8192)]

students_df = pd.DataFrame(students)
students_in_term = {}

# Her bir term'e 5-15 arası öğrenci atanıyor
for dept in faculties.values():
    for department in dept:
        for term in range(1, num_terms + 1):
            term_key = f"{department}_Term_{term}"
            term_students = students_df[
                (students_df['Department'] == department) & (students_df['Term'] == f'Term {term}')]
            students_in_term[term_key] = np.random.choice(term_students['Student_ID'],
                                                          size=rd.randint(5, 15), replace=False).tolist()

courses = []
registrations = []

# Kursları ve kayıtlı öğrencilerini oluşturur
for faculty, depts in faculties.items():
    for dept in depts:
        for term in range(1, num_terms + 1):
            term_key = f'{dept}_Term_{term}'
            course_seq = 1
            for course_name in course_names[dept][f'Term {term}']:
                course_id = f"{faculty[:1].upper()}{dept[:3].upper()}{term:01d}{course_seq:02d}"  # Kurs IDsi oluştur
                course_student_ids = students_in_term[term_key]
                courses.append({
                    'Course_ID': course_id,
                    'Department': dept,
                    'Course_Name': course_name,
                    'Term': f'Term {term}',
                    'Student_IDs': course_student_ids
                })
                for student_id in course_student_ids:
                    registrations.append({
                        'Course_ID': course_id,
                        'Student_ID': student_id
                    })
                course_seq += 1


courses_df = pd.DataFrame(courses)
registrations_df = pd.DataFrame(registrations)
students_registered_courses = []

for student_id in students_df['Student_ID']:
    registered_courses = registrations_df[registrations_df['Student_ID'] == student_id]['Course_ID'].tolist()
    students_registered_courses.append(registered_courses)

students_df['Registered_Courses'] = students_registered_courses
students_df = students_df[students_df['Registered_Courses'].str.len() > 0]

students_df.to_csv('university_students.csv', index=False)
courses_df.to_csv('courses.csv', index=False)
registrations_df.to_csv('course_registrations.csv', index=False)

print(students_df.head())
print(courses_df.head())
print(registrations_df.head())
