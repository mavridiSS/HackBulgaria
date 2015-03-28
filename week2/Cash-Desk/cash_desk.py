class Bill:
    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __hash__(self):
        return hash(str(self.amount))

    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return self.__str__()

a = Bill(10)
print(a)


class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([int(bill) for bill in self.bills])

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk:
    def __init__(self):
        self.desk_money = list()

    def take_money(self, money):
        if (isinstance(money, Bill)):
            self.desk_money.append(int(money))
        else:
            for bill in money:
                self.desk_money.append(int(bill))

    def total(self):
        return sum([bill for bill in self.desk_money])

    def inspect(self):
        for bill in sorted(set(sorted(self.desk_money))):
            print("{}$ bills - {}".format(bill, self.desk_money.count(bill)))

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(Bill(10))
desk.take_money(batch)

print(desk.total())
desk.inspect()
