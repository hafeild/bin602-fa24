'''
File:   cli_sys_demo.py
Author: Hank Feild
Date:   2024-11-26
Purpose: Demonstrates how to use sys to read command line arguments.
'''

import sys
import random

def printRandomNumbers(rangeStart, rangeEnd, count):
    '''Prints `count` random numbers in the range [`rangeStart`, `rangeEnd`].
    
    Parameters:
        rangeStart (int): The smallest possible random value that can be produced.
        rangeEnd (int): The largest possible random value that can be produced.
        count (int): The number of random numbers to produce.
    '''
    for i in range(count):
        print(random.randint(rangeStart, rangeEnd))

def main():
    '''Reads command line arguments '''
    
    usage = ('python3 cli_sys_demo.py <start> <end> <count>\n\n'+
            'Produces <count> random integers in the range [<start>, <end>].\n')
    
    if '-h' in sys.argv:
        print(usage, end='')
        sys.exit()

    if len(sys.argv) < 4:
        sys.stderr.write('Too few arguments!\n')
        sys.stderr.write(usage)
        sys.exit(1)

    # Parse command line arguments.
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    count = int(sys.argv[3])

    # Generate and print the random numbers.
    printRandomNumbers(start, end, count)

if __name__ == '__main__':
    main()