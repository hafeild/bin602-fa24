'''
File:   hello_world.py
Author: Hank Feild
Date:   2024-11-26
Purpose: Simple hello world program that also reads in data from the user.
'''

def sayHello():
    '''Interacts with the user, saying hi and asking their name.'''
    print('Hello, world!')
    name = input('Enter your name: ')
    print(f'Hello, {name}!')
    
def main():
    sayHello()

if __name__ == '__main__':
    main()