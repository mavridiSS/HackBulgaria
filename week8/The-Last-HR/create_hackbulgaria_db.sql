DROP TABLE IF EXISTS students;

CREATE TABLE students(student_id INTEGER PRIMARY KEY,
                      student_name TEXT UNIQUE,
                      github_name TEXT);

DROP TABLE IF EXISTS courses;

CREATE TABLE courses(course_id INTEGER PRIMARY KEY,
					 course_name TEXT UNIQUE);

DROP TABLE IF EXISTS student_courses;

CREATE TABLE student_courses(student_id INTEGER,
                             course_id INTEGER,
                             FOREIGN KEY(student_id) REFERENCES students(student_id),
                             FOREIGN KEY(course_id) REFERENCES courses(course_id));