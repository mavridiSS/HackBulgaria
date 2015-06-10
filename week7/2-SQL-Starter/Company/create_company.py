import sqlite3
from settings import DB_NAME, DB_SQL_FILE


def main():
    company = sqlite3.connect(DB_NAME)
    cursor = company.cursor()
    with open(DB_SQL_FILE, 'r') as f:
        cursor.executescript(f.read())

if __name__ == '__main__':
    main()

