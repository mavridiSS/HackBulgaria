class BankAccount:

    def __init__(self, name, balance, currency):
        if (isinstance(name, str)):
            self.__name = name
        else:
            raise TypeError
        if (isinstance(balance, int)):
            self.__balance = balance
        else:
            raise TypeError
        if(isinstance(currency, str)):
            self.__currency = currency
        else:
            raise TypeError
        self.__acc_history = ["Account was created"]

    def deposit(self, amount):
        self.__balance += amount
        self.__acc_history.append(
            "Deposited {}{}".format(amount, self.__currency))

    def balance(self):
        self.__acc_history.append("Balance check -> {}{}".format(self.__balance,
                                                                 self.__currency))
        return self.__balance

    def withdraw(self, amount):
        if self.__balance < amount or amount <= 0:
            self.__acc_history.append(
                "Withdraw for {}{} failed".format(amount, self.__currency))
            raise ValueError
            return False
        else:
            self.__balance -= amount
            self.__acc_history.append(
                "{}{} was withdrawed".format(amount, self.__currency))
            return True

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.__name,
                                                                 self.__balance,
                                                                 self.__currency)

    def __int__(self):
        self.__acc_history.append("__int__check -> {}{}".format(self.__balance,
                                                                self.__currency))
        return self.__balance

    def transfer_to(self, other, amount):
        if self.__balance >= amount:
            self.withdraw(amount)
            other.deposit(amount)
            self.__acc_history.append(
                "Transfer to {} for {}{}".format(other.__name, amount, self.__currency))
            other.__acc_history.append(
                "Transfer from {} for {}{}".format(self.__name, amount, self.__currency))
            return True
        return False

    def history(self):
        return self.__acc_history

rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")
rado.balance()
print(rado.history())
