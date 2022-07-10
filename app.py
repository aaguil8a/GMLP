from cgi import print_directory
from regex import F
from sqlalchemy import true
# folder to py
from banking_pkg.account import *

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print('=== Automated Teller Machine ===')
name = input('Enter name to register: ')
pin = int(input('Enter PIN: '))
balance = 0
print(f'{name} has been registered with a starting balance of ${balance}')


while True:
    print('=== Automated Teller Machine ===')
    name_to_validate = input('Enter name to register: ')
    pin_to_validate = int(input('Enter PIN: '))
    if name_to_validate == name and pin_to_validate == pin:
        print('Login successful!')
        break
    
    else:
        print('Invalid credentials')


while True:
    atm_menu(name)
    option = int(input('Choose an option: '))
    if option == 1:
        show_balance(balance)
    
    elif option == 2:
        balance = deposit(balance)
        print('Current Balance: ', balance)     
    
    elif option == 3:
        balance = withdraw(balance)
        print('Current Balance: ', balance)
        
    
    elif option == 4:
        logout(name)
        break



