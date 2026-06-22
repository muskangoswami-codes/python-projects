class account:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount

    def show_balance(self):
        print("balance:",self.balance)

amount=int(input("enetr the amount:"))
deposit_amount=int(input("enter the deposit amount:"))
withdraw_amount=int(input("enter the withdraw amount:"))

acc = account(amount)
acc.deposit(deposit_amount)
acc.withdraw(withdraw_amount)
acc.show_balance()
