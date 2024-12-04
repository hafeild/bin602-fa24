'''
(TODO: Fill in)
'''

import cli_argparse_demo as rand_generator 
import count
import plot 


def main():
    randomNumbersAsStr = [str(x) for x in rand_generator.printRandomNumbers(1, 50, 1000, True)]
    countsAsStr = [f'{key} {value}' for key,value in count.tallyLines(randomNumbersAsStr).items()]
    plot.plotFrequencies(countsAsStr, 'Random numbers', 'Frequencies')


if __name__ == "__main__":
    main()