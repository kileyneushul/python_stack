class BankAccount:
    def __init__(self, interestRate=0, balance=0):
    #attributes listed here
        self.interest = interestRate
        self.balance = balance

    
    #methods listed here
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print("Balance: ${}").format(self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance*self.interest)
        return self
    
kileyAccount = BankAccount(balance=300000)
gabyAccount = BankAccount(.02, 2000000)

kileyAccount.deposit(5000).deposit(3000).deposit(9000).withdraw(5017).yield_interest().display_account_info()
gabyAccount.deposit(900000).deposit(600000).withdraw(34098).withdraw(45000).withdraw(150000).yield_interest().display_account_info()







    