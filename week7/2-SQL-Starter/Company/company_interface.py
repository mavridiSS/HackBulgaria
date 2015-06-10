import re


class CompanyInterface():
    COMMANDS = """Commands are:
                  1)list_employees,
                  2)monthly_spending,
                  3)yearly_spending,
                  4)add_employee,
                  5)delete_employee <id>"""

    def __init__(self, company_manager):
        self.__cm = company_manager

    def __command_dispatcher(self, command):
        if command == "list_employees":
            self.list_employees()

        elif command == "monthly_spending":
            self.monthly_spending()

        elif command == "yearly_spending":
            self.yearly_spending()

        elif command == "add_employee":
            worker = [input("name>"),
                      input("monthly_salary>"),
                      input("yearly_bonus>"),
                      input("position>")]
            self.add_employee(worker)

        elif "delete_employee" in command:
            number = re.search(r'\d+', command).group()
            self.delete_employee(number)

        else:
            self.print_wrong_command()

        self.__cm.commit()

        if self.wanna_quit():
            return False

    def list_employees(self):
        result = self.__cm.list_employees()
        for user in result:
            print(user["id"], "-", user["name"], "-", user["position"])

    def monthly_spending(self):
        result = self.__cm.monthly_spending()
        monthly = sum([salary["monthly_salary"] for salary in result])
        print("The company is spending {} BGN every month!".format(monthly))

    def yearly_speding(self):
        result = self.__cm.yearly_spending()
        yearly = sum([row["yearly_bonus"] + row["monthly_salary"] * 12
                      for row in result])
        print("The company is spending {} BGN every year!".format(yearly))

    def add_employee(self, worker):
        self.__cm.add_employee(worker)

    def delete_employee(self, number):
        self.__cm.delete_employee(number)

    def print_wrong_command(self):
        print("Wrong command!")
        self.print_commands()

    def print_commands(self):
        print(self.__class__.COMMANDS)

    def start(self):
        while True:
            command = input("command>")
            if self.__command_dispatcher(command) == False:
                break
            else:
                continue

    def wanna_quit(self):
        user_input = input("Do you want to quit? [Y|N]:")
        if user_input.upper() == "Y":
            return True
        elif user_input.upper() == "N":
            return False
