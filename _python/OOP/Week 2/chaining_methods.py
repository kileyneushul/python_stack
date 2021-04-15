class User: 
    def __init__(self, user_name, email_address): 
    #attributes defined here
        self.name = user_name
        self.email = email_address
        self.accountBalance = 0
        self.other_user_account_balance = 0
    
    #methods defined here
    def accountDeposit(self, amount): 
        self.accountBalance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.accountBalance -= amount
        return self
    
    def display_user_balance(self):
        print("User: {}, Balance ${}".format(self.name, self.accountBalance))
        return self
    
    def transfer_money(self, other_user, amount):
        self.accountBalance -= amount
        other_user.accountBalance += amount
        return self

#Instances (0bjects) created here
kiley = User("Kiley", "kileyneushul@gmail.com")
gaby = User("Gaby", "gabrielhernandezpaz@hotmail.com")
frida = User("Frida", "fantasticfrida@gmail.com")

#Checking If Info will be printed from created objects
print(kiley.name)
print(gaby.email)
print(frida.accountBalance)

# Depositing/Withdrawing money from User #1's account
kiley.accountDeposit(700).accountDeposit(800).accountDeposit(900).make_withdrawal(300).display_user_balance().transfer_money(frida,500).display_user_balance()

# Depositing/Withdrawing money from User #2's account
gaby.accountDeposit(4000).accountDeposit(4001).make_withdrawal(3000).display_user_balance()

# Depositing/Withdrawing money from User #3's account
frida.accountDeposit(1000).make_withdrawal(34).make_withdrawal(890).make_withdrawal(100).display_user_balance()











