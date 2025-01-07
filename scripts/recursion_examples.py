'''
File:   recursion_examples.py
Author: Hank Feild
Date:   2024-12-20
Purpose: Provides several examples of recursive functions.
'''
import turtle

# TODO define factorial(n) recursively
def factorial(n):
    '''Calculates n! recursively.
    
    Parameters:
        n (int): positive integer to compute the factorial of.
    
    Return (int): n!
    '''
    assert n >= 0, 'n must be positive'
    assert isinstance(n, int), 'n must be an integer'

    # Base case: n is 0:
    if n == 0:
        return 1
    
    # Recursive case.
    return n * factorial(n-1)

def factorialIterative(n):
    '''Calculates n! iteratively.
    
    Parameters:
        n (int): positive integer to compute the factorial of.
    
    Return (int): n!
    '''
    assert n >= 0, 'n must be positive'
    assert isinstance(n, int), 'n must be an integer'

    product = 1 # captures our base case value
    for i in range(1, n+1):
        product = i * product
    return product

def koch(tortoise, length, depth):
    '''Draws a Koch curve recursively.
    
    Parameters:
        tortoise (Turtle): The Turtle to draw with.
        length (float): The length of the curve.
        depth (int): The level of detail to provide (the depth of the recursion).
    '''
    if depth == 0:
        tortoise.forward(length)
        # tortoise.getscreen().update()

    else:
        koch(tortoise, length/3, depth-1)
        tortoise.left(60)
        koch(tortoise, length/3, depth-1)
        tortoise.right(120)
        koch(tortoise, length/3, depth-1)
        tortoise.left(60)
        koch(tortoise, length/3, depth-1)


def kochSnowflake(length, depth):
    '''Draws three Koch curves to make a Koch snowflake.
    
    Parameters:
        length (float): The length of each side of the snowflake.
        depth (int): The depth of the recursive features.
    '''
    pat = turtle.Turtle()
    screen = pat.getscreen()
    screen.setup(800,800,0,0)
    screen.setworldcoordinates(-400, -400, 400, 400)
    # pat.speed(0)
    screen.tracer(0)
    pat.up()
    pat.goto(-length/2, length/2)
    pat.down()
    input("Press enter when ready: ")

    for side in range(3):
        koch(pat, length, depth)
        pat.right(120)
        pat.getscreen().update()

    screen.mainloop()



def main():
    # kochSnowflake(400, 10)
    for n in [0, 5, 10]:
    #     print(f'{n}! = {factorial(n)}')
        print(f'{n}! = {factorialIterative(n)}')

if __name__ == '__main__':
    main()