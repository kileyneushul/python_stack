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
    
    def make_withdrawal(self, amount):
        self.accountBalance -= amount
    
    def display_user_balance(self):
        print("User: {}, Balance ${}".format(self.name, self.accountBalance))
    
    def transfer_money(self, other_user, amount):
        self.accountBalance -= amount
        other_user.accountBalance += amount
        return other_user.accountBalance

kiley = User("Kiley", "kileyneushul@gmail.com")
gaby = User("Gaby", "gabrielhernandezpaz@hotmail.com")
frida = User("Frida", "fantasticfrida@gmail.com")

print(kiley.name)
print(gaby.email)
print(frida.accountBalance)

kiley.accountDeposit(700)
kiley.accountDeposit(800)
kiley.accountDeposit(900)
kiley.make_withdrawal(300)
print(kiley.accountBalance)
kiley.display_user_balance()

gaby.accountDeposit(4000)
gaby.accountDeposit(4001)
gaby.make_withdrawal(3000)
gaby.display_user_balance()


frida.accountDeposit(1000)
frida.make_withdrawal(34)
frida.make_withdrawal(890)
frida.make_withdrawal(100)
frida.display_user_balance()

#Transfer Money
kiley.transfer_money(frida, 500)
kiley.display_user_balance()
frida.display_user_balance()









