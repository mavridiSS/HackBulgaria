import sqlite3


def main():
    company = sqlite3.connect('company.db')

    cursor = company.cursor()
    create_table = """ CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,
                                                        name TEXT,
                                                        monthly_salary INTEGER,
                                                        yearly_bonus INTEGER,
                                                        position TEXT)
    """
    cursor.execute(create_table)

    company.commit()

    workers = [("Ivan Ivanov", 5000, 10000, "Software Developer"),
               ("Rado Rado", 500, 0, "Technical Support Intern"),
               ("Ivo Ivo", 10000, 100000, "CEO"),
               ("Petar Petrov", 3000, 1000, "Marketing Manager"),
               ("Maria Georgieva", 8000, 10000, "COO")]

    cursor.executemany(""" INSERT INTO users(name,monthly_salary, yearly_bonus, position)
                           VALUES(?, ?, ?, ?)""", workers)
    company.commit()

if __name__ == '__main__':
    main()

