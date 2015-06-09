import requests
import sqlite3
from settings import DB_NAME, DB_SQL_FILE, URL


class HackBulgariaDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        with open(DB_SQL_FILE, "r") as f:
            self.cursor.executescript(f.read())
        self.conn.commit()
        r = requests.get(URL)
        self.data = r.json()

    def populate_tables(self):
        for student in self.data:
            try:
                self.cursor.execute("""INSERT INTO students(student_name)
                                       VALUES(?)""", (student['name'], ))
            except Exception as e:
                print(e)
            if student['github']:
                self.cursor.execute("""UPDATE students SET github_name=? WHERE student_name=?""", (student['github'], student['name']))
            self.cursor.execute("""SELECT student_id FROM students
                                   WHERE student_name is ?""", (student['name'], ))
            studentid = self.cursor.fetchone()[0]

            for course in student["courses"]:
                try:
                    self.cursor.execute("""INSERT INTO courses(course_name)
                                           VALUES(?)""", (course['name'], ))
                except Exception as e:
                    print(e)
                self.cursor.execute('''SELECT course_id FROM courses
                                       WHERE course_name is ?''', (course['name'], ))
                courseid = self.cursor.fetchone()[0]

                self.cursor.execute("""SELECT student_id,course_id
                                       FROM student_courses
                                       WHERE student_id= ? AND course_id= ?""", (studentid, courseid))
                student_course = self.cursor.fetchone()
                if not student_course:
                    self.cursor.execute("""INSERT INTO student_courses(student_id,course_id)
                                           VALUES(?, ?)""", (studentid, courseid))
        self.conn.commit()

    def list_users_with_github(self):
        result = self.cursor.execute("""SELECT student_name,github_name
                                        FROM students
                                        WHERE github_name is not null
                                        GROUP BY student_name""")
        return result.fetchall()

    def list_courses(self):
        self.cursor.execute("""SELECT * FROM courses""")
        return self.cursor.fetchall()

    def list_student_courses(self):
        self.cursor.execute("""SELECT students.student_name, GROUP_CONCAT(courses.course_name)
                               FROM students
                               INNER JOIN student_courses ON students.student_id=student_courses.student_id
                               INNER JOIN courses ON student_courses.course_id=courses.course_id
                               GROUP BY students.student_name""")
        return self.cursor.fetchall()

    def list_most_attending_students(self):
        self.cursor.execute("""SELECT students.student_name,COUNT(courses.courses_name) AS count
                               FROM students
                               INNER JOIN student_courses ON students.student_id=student_courses.student_id
                               INNER JOIN courses ON student_courses.course_id=courses.course_id
                               GROUP BY students.student_name
                               ORDER BY count DESC LIMIT 10""")
        return self.cursor.fetchall()


def main():
    db = HackBulgariaDB()
    db.populate_tables()
    for row in db.list_users_with_github():
        print("{} - {}".format(row[0], row[1]))
    for row in db.list_courses():
        print("{} - {}".format(row[0], row[1]))
    for row in db.list_student_courses():
        print("{} is attending {}".format(row[0], row[1]))
    for row in db.list_most_attending_students():
        print("{} is attending {} courses".format(row[0], row[1]))


if __name__ == '__main__':
    main()
