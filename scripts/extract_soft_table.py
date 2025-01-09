'''
Filename:   extract_soft_table.py
Author:     Hank Feild
Date:       2025-01-09
Purpose:    Extracts a table by name from a SOFT-formatted file.
'''

import argparse
import sys

def extractSOFTTable(inputStream, tableName, outputStream):
    '''Extract the lines for the given table from the input stream. E.g.
    if tableName is "Data_matrix_for_GSE2034", and the following is in
    the input stream:
    
        !series_table_begin = Data_matrix_for_GSE2034
        REF_ID gene1 gene2 ....
        patient1 ...
        patient2 ...
        !series_table_end
    
    then all of the lines between but not including !series_table_begin and
    !series_table_end will be output to the outputStream.
    
    Parameters:
        inputStream (stream): The stream containing the SOFT data.
        tableName (str): The name of the table to extract; must be the full name.
        outputStream (stream): The stream to write the table to. 
    '''
    inTable = False
    
    for line in inputStream:
        if inTable:
            # Check if we're at the end of the table -- if so, return.
            if line.startswith('!series_table_end'):
                return
            # Otherwise, write the line to output stream.
            outputStream.write(line)
        else:
            if line.strip() == f'!series_table_begin = {tableName}':
                inTable = True


def main():
    '''Read a file or stdin from the CLI along with a table name and output
    the table data to stdou.'''
    
    parser = argparse.ArgumentParser(
        prog='extract_soft_table.py',
        description='Extracts a table by name from a SOFT formatted file.'
    )
    
    parser.add_argument('inputFile', 
        help='The path of the SOFT file from which to extract the table (use "-" for stdin)',
        type=argparse.FileType('r'))
    parser.add_argument('tableName', 
        help='The name of the table to extract from the SOFT data', 
        type=str)
    
    args = parser.parse_args()
    
    extractSOFTTable(args.inputFile, args.tableName, sys.stdout)

if __name__ == '__main__':
    main()