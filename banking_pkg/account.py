

def show_balance(balance):
    print(float(balance))

def deposit(balance):
    deposit_amount = float(input('Enter amount to deposit: '))
    return balance + deposit_amount
    


def withdraw(balance):
    withdraw_amount = float(input('Enter amount to withdraw: '))
    return  balance - withdraw_amount

def logout(name):
    print(f'Goodbye {name}')
