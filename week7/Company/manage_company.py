import sqlite3
import re

company = sqlite3.connect('company.db')

"""
Will return me a Row object which has notations like dict "row["email"]" for example
"""

company.row_factory = sqlite3.Row

cursor = company.cursor()


def wanna_quit():
    user_input = input("Do you want to quit? [Y|N]:")
    if user_input.upper() == "Y":
        return True
    elif user_input.upper() == "N":
        return False

while True:
    user_input = input("command>")
    if user_input == "list_employees":
        list_employees = """ SELECT id,name,position FROM users """
        result = cursor.execute(list_employees)
        for user in result:
            print(user["id"], "-", user["name"], "-", user["position"])

    elif user_input == "monthly_spending":
        monthly_spending = """ SELECT monthly_salary FROM users """
        result = cursor.execute(monthly_spending)
        monthly_salary = sum([salary["monthly_salary"] for salary in result])
        print("The company is spending {} BGN every month!".format(monthly_salary))

    elif user_input == "yearly_spending":
        yearly_spending = """ SELECT monthly_salary,yearly_bonus FROM users """
        result = cursor.execute(yearly_spending)
        yearly_salary = sum([row["yearly_bonus"] + row["monthly_salary"] * 12
                            for row in result])
        print("The company is spending {} BGN every year!".format(yearly_salary))

    elif user_input == "add_employee":
        worker = [input("name>"),
                  input("monthly_salary>"),
                  input("yearly_bonus>"),
                  input("position>")]
        add_worker = """ INSERT INTO users(name,monthly_salary, yearly_bonus, position)
                         VALUES(?, ?, ?, ?)"""
        cursor.execute(add_worker, worker)

    elif "delete_employee" in user_input:
        number = re.search(r'\d+', user_input).group()
        delete_worker = """ DELETE FROM users WHERE id=?"""
        cursor.execute(delete_worker, number)
    else:
        print("""Wrong command! Commands are:
               1)list_employees,
               2)monthly_spending,
               3)yearly_spending,
               4)add_employee,
               5)delete_employee <id>""")
    company.commit()
    if wanna_quit():
        break
    else:
        continue
