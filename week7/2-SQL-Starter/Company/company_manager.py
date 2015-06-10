import sqlite3


class CompanyManager():
    def __init__(self, conn):
        self.conn = conn
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def list_employees(self):
        list_employees = """ SELECT id,name,position FROM users """
        result = self.cursor.execute(list_employees)
        return result

    def monthly_spending(self):
        monthly_spending = """ SELECT monthly_salary FROM users """
        result = self.cursor.execute(monthly_spending)
        return result

    def yearly_spending(self):
        yearly_spending = """ SELECT monthly_salary,yearly_bonus FROM users """
        result = self.cursor.execute(yearly_spending)
        return result

    def add_employee(self, worker):
        add_worker = """ INSERT INTO users(name,monthly_salary, yearly_bonus, position)
                         VALUES(?, ?, ?, ?)"""
        self.cursor.execute(add_worker, worker)

    def delete_employee(self, number):
        worker = """ DELETE FROM users WHERE id=?"""
        self.cursor.execute(worker, number)

    def commit(self):
        self.conn.commit()


