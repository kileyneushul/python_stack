class BankAccount:
    def __init__(self, interestRate, balance=0):
    #attributes listed here
        self.interest = interestRate
        self.balance = balance
        self.balance2 = 0

    
    #methods listed here
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawl(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print("Balance: ${}").format(self.balance)
        return self

    def second_account_deposit(self, amount2):
        self.balance2 += amount2
        return self
    
    def second_account_withdrawl(self, amount2):
        self.balance2 -= amount2
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def second_account_info(self):
        print("Balance: ${}").format(self.balance2)
        return self


    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance*self.interest)
        return self



class User: 
    def __init__(self, user_name, email_address): 
    #attributes defined here
        self.name = user_name
        self.email = email_address
        self.accountBalance = BankAccount(0.01)
    
    #methods defined here
    def accountDeposit(self, amount): 
        self.accountBalance.deposit(amount)
        return self
    
    def make_withdrawl(self, amount):
        self.accountBalance.withdrawl(amount)
        return self
    
    def display_user_balance(self):
        self.accountBalance.display_account_info()
        return self
    
    def accountDeposit2(self, amount2): 
        self.accountBalance.second_account_deposit
        return self
    
    def accountWithdrawl2(self, amount2):
        self.accountBalance.second_account_withdrawl
        return self
    
    def display_user_balance_second(self):
        self.accountBalance.second_account_info
        return self
    
    def transfer_money(self, other_user, amount):
        self.accountBalance -= amount
        other_user.accountBalance += amount
        return other_user.accountBalance

kiley = User("Kiley Neushul", "kileyneushul@gmail.com")
frida = User("Frida Hernandez", "fridahazelhernandez8@gmail.com")  
gaby = User("Gaby Hernandez", "ghernandezpaz@hotmail.com")



print(kiley.name)
print(frida.email)
print(gaby.email)
print(gaby.name)

kiley.accountDeposit(100).make_withdrawl(50)
kiley.accountDeposit2(400000).accountWithdrawl2(300).accountWithdrawl2(6548)


kiley.display_user_balance()
kiley.display_user_balance_second()


# gaby.accountDeposit(500).make_withdrawl(10)
# gaby.accountDeposit2(93211).accountdeposit2(90234).accountWithdrawl2(54344)

# kiley.display_user_balance()
# gaby.display_user_balance()

# kiley.display_user_balance_second()
# gaby.display_user_balance_second()





    #The one that is calling upon the other, must run last. 