class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
   
    def make_deposit(self, amount):	
    	self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(self.name, 'has',  self.account_balance, '$')

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
turki = User("Turki Bt", "turki@gmail.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(100)
guido.make_withdrawal(200)
guido.display_user_balance()

monty.make_deposit(100)
monty.make_deposit(100)
monty.make_withdrawal(50)
monty.make_withdrawal(50)
monty.display_user_balance()

turki.make_deposit(1000)
turki.make_withdrawal(50)
turki.make_withdrawal(50)
turki.make_withdrawal(50)
turki.display_user_balance()

turki.transfer_money(monty, 100)
print('After transfer money')
turki.display_user_balance()
monty.display_user_balance()
