import create_company
import sqlite3
from settings import DB_NAME
from company_interface import CompanyInterface
from company_manager import CompanyManager


def main():
    create_company.main()
    conn = sqlite3.connect(DB_NAME)
    cm = CompanyManager(conn)
    ci = CompanyInterface(cm)
    ci.start()

if __name__ == '__main__':
    main()
