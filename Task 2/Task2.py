class Account():
    def __init__(self, account_number, account_holder, balance):
        self.account_number =  account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"{self.account_holder} has Insufficient Balance")
        else:
            self.balance -= amount

    def get_balance(self): 
        print(self.balance)

    def __str__(self):
        return f"Account Holder:{self.account_holder}, Account Number: {self.account_number}, Balance:{self.balance}"


class Bank():
    def __init__(self):
       #accounts (list of Account objects)
       self.accounts = list()

    def add_account(self, account):
        self.accounts.append(account)
    
    def Find_account(self, account_number):
        found = None
        for i in self.accounts:
            if i.account_number == account_number:
                print(i)
                found = True
        if found == None:
            print("No Account Found")

    def list_accounts(self):
        for i in self.accounts:
            print(i)

man1 = Account(4120, "Abheesh", 40000)
man2 = Account(2102, "Abdullah", 400000)
man3 = Account(1101, "Satish", 25000)
man1.deposit(40000)
man2.withdraw(40000)
man2.get_balance()
man1.get_balance()

bank = Bank()
bank.add_account(man1)
bank.add_account(man2)
bank.add_account(man3)
bank.Find_account(1101)
bank.list_accounts()
bank.accounts[0].deposit(40000)
bank.accounts[2].withdraw(40000)
bank.Find_account(1101)
bank.Find_account(2102)