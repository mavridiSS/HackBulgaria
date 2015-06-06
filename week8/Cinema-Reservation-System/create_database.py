import sqlite3
from settings import DB_NAME, DB_SQL_FILE


def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    with open(DB_SQL_FILE, "r") as f:
        cursor.executescript(f.read())


if __name__ == '__main__':
    main()
