class User: 
    def __init__(self, user_name, email_address): 
    #attributes defined here
        self.name = user_name
        self.email = email_address
        self.accountBalance = 0
    
    #methods defined here
    def accountDeposit(self, amount): 
        self.accountBalance += amount
    
    def make_withdrawal(self, amount):
        self.accountBalance -= amount
    
    def display_user_balance(self):
        print("User: {}, Balance ${}".format(self.name, self.accountBalance))
    
    def transfer_money(self, other_user, amount):
        self.accountBalance -= amount
        other_user.accountBalance += amount
        return other_user.accountBalance

#Instances (0bjects) created here
kiley = User("Kiley", "kileyneushul@gmail.com")
gaby = User("Gaby", "gabrielhernandezpaz@hotmail.com")
frida = User("Frida", "fantasticfrida@gmail.com")

#Checking If Info will be printed from created objects
print(kiley.name)
print(gaby.email)
print(frida.accountBalance)

# Depositing/Withdrawing money from User #1's account
kiley.accountDeposit(700)
kiley.accountDeposit(800)
kiley.accountDeposit(900)
kiley.make_withdrawal(300)
print(kiley.accountBalance)
kiley.display_user_balance()

# Depositing/Withdrawing money from User #2's account
gaby.accountDeposit(4000)
gaby.accountDeposit(4001)
gaby.make_withdrawal(3000)
gaby.display_user_balance()

# Depositing/Withdrawing money from User #3's account
frida.accountDeposit(1000)
frida.make_withdrawal(34)
frida.make_withdrawal(890)
frida.make_withdrawal(100)
frida.display_user_balance()

#Transfer Money from user #1 to user #3's account
kiley.transfer_money(frida, 500)
kiley.display_user_balance()
frida.display_user_balance()









