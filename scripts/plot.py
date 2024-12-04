'''
File:   plot.py
Author: Hank Feild
Date:   2024-11-26
Purpose: Plot the frequencies of items. Expects stdin in the format: item count.
'''

import argparse
import matplotlib.pyplot as plt
import sys 

def plotFrequencies(inputFileDescriptor, xLabel, yLabel):
    '''Creates a bar plot of the frequencies in the given input file. Inputs 
    should be pairs of items, counts (space separated), one per line. The items
    are sorted before plotting.
    
    Parameters:
        inputFileDescriptor (file): The file to read from.
        xLabel (str): The label to give the X axis.
        yLabel (str): The label to give the Y axis.
    '''
    values = []

    for line in inputFileDescriptor:
        x, y = line.strip().split()
        y = int(y)
        values.append((x, y))
    values.sort(key=lambda item: item[0])

    plt.bar(range(len(values)), [y for (x,y) in values])
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

def main():
    '''Plot frequencies form stdin.'''
    
    parser = argparse.ArgumentParser(
        prog='plot.py',
        description='Produces a bar plot of item count pairs.'
    )

    # Adds two positional arguments.
    parser.add_argument('xLabel', help='The label of the x-axis', type=str)
    parser.add_argument('yLabel', help='The label of the y-axis', type=str)

    args = parser.parse_args()

    plotFrequencies(sys.stdin, args.xLabel, args.yLabel)

if __name__ == '__main__':
    main()