class account:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount

    def show_balance(self):
        print("balance:",self.balance)

acc = account(50000)
acc.deposit(10000)
acc.withdraw(4500)
acc.show_balance()
