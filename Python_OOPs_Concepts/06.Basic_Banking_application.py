import sys
class Customer:
    '''Customer class with bank related operation'''
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
    
    def deposit(self,amt):
        self.balance = self.balance+amt
        print('After the deposit the balance:',self.balance)
    
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficcent Amount in your bank")
            sys.exit()
        self.balance  = self.balance-amt
        print('After withdraw the balance ',self.balance)

print("Welcome to DurgaBank")
name = input('Enter your name')
c = Customer(name)
while True:
    print('Deposit \n w-Withdraw\n e-Exit')
    option = input('Choose your Option')
    if option.lower() == 'd':
        amt = float(input('Enter the amount to deposit'))
        c.deposit(amt)

    elif option == 'w' or option == 'W':
        amt  = float(input('Enter the amount to withdraw'))
        c.withdraw(amt)

    elif option=='e' or option=='E':
        print("Thanks for Banking")
        sys.exit()

    else:
        print('Choose valid option')

