'''
File:   cli_sys_demo.py
Author: Hank Feild
Date:   2024-11-26
Purpose: Demonstrates how to use argparse to read command line arguments.
'''

import argparse
import random

def printRandomNumbers(rangeStart, rangeEnd, count, returnNumbers=False):
    '''Prints `count` random numbers in the range [`rangeStart`, `rangeEnd`].
    
    Parameters:
        rangeStart (int): The smallest possible random value that can be produced.
        rangeEnd (int): The largest possible random value that can be produced.
        count (int): The number of random numbers to produce.
        returnNumbers (bool): If True, returns the numbers as a list instead of printing. 
    '''
    numbers = []
    for i in range(count):
        randomNumber = random.randint(rangeStart, rangeEnd)
        if returnNumbers:
            numbers.append(randomNumber)
        else:
            print(randomNumber)

    if returnNumbers:
        return numbers

def main():
    '''Reads command line arguments '''
    
    parser = argparse.ArgumentParser(
        prog='cli_argparse_demo.py',
        description='Produces <count> random integers in the range [<start>, <end>]'
    )

    # Adds three positional arguments.
    parser.add_argument('start', help='The smallest possible value that could be produced', type=int)
    parser.add_argument('end', help='The largest possible value that could be produced', type=int)
    parser.add_argument('count', help='The number of random numbers to print', type=int)

    # argparse also supports named arguments with flags that can be in any 
    # order, e.g., something like: 
    #       cli_argparse_demo.py -start 10 -end 50 -count 15

    args = parser.parse_args()

    # Generate and print the random numbers.
    printRandomNumbers(args.start, args.end, args.count)

if __name__ == '__main__':
    main()