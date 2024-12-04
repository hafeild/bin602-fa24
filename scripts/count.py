'''
File:    count.py
Author:  Hank Feild
Date:    2024-11-26
Purpose: Tallies the frequency of distinct lines from stdin. Produces 
         line-count pairs (separated by a space) to stdout.

Example stdin:

    10
    20
    15
    10
    25
    30
    20
    10

Example output:

    10 3
    20 2
    15 1
    25 1
    30 1
'''
import sys
from collections import defaultdict 

def tallyLines(inputFileDescriptor):
    '''Tallies distinct lines from the given input file.
    
    Parameters:
        inputFileDescriptor (file): The file to read from.
    
    Return (dict[str:int]): A mapping of distinct lines from the input to their counts.
    '''
    lineCounts = defaultdict(int)

    for line in inputFileDescriptor:
        lineCounts[line.strip()] += 1

    return lineCounts

def main():
    '''Tallies distinct lines from stdin and output them with their counts to stdout.'''
    for line,count in tallyLines(sys.stdin).items():
        print(line, count)

if __name__ == '__main__':
    main()