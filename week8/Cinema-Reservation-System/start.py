import sqlite3
import create_database
from settings import DB_NAME
from cinema_manager import CinemaManager
from cinema_interface import CinemaInterface


def main():
    create_database.main()
    conn = sqlite3.connect(DB_NAME)
    cm = CinemaManager(conn)
    ci = CinemaInterface(cm)
    ci.start()

if __name__ == '__main__':
    main()
