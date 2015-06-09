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
        self.__acc_history.append("Deposited {}{}".format(amount,
                                                          self.__currency))

    def balance(self):
        balance = "Balance check -> {}{}"
        self.__acc_history.append(balance.format(self.__balance,
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
        acc_str = "Bank account for {} with balance of {}{}"
        return acc_str.format(self.__name, self.__balance, self.__currency)

    def __int__(self):
        check = "__int__check -> {}{}"
        self.__acc_history.append(check.format(self.__balance,
                                               self.__currency))
        return self.__balance

    def transfer_to(self, other, amount):
        trf_to = "Transfer to {} for {}{}"
        trf_from = "Transfer from {} for {}{}"
        if self.__balance >= amount:
            self.withdraw(amount)
            other.deposit(amount)
            self.__acc_history.append(trf_to.format(other.__name,
                                                    amount,
                                                    self.__currency))
            other.__acc_history.append(trf_from.format(self.__name,
                                                       amount,
                                                       self.__currency))
            return True
        else:
            return False

    def history(self):
        return self.__acc_history
