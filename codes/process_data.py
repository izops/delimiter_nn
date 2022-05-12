# create large one-column file for data generating

import os, csv, numpy as np

# define modes to use ('append' vs 'overwrite')
strMode = 'overwrite'

# define source file delimiter
strDelim = ';'

# define path of the source file
strPathIn = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/sources/MP_AU_VERTRAG_INVENTUR_20210312.asc'
strPathOut = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/out1.txt'

def CreateOneColumn(pstrIn, pstrOut, pstrDelim, pstrMode):
    '''
    Splits a text file into a one column file by words

    Inputs:
        pstrIn - string with the source file full path
        pstrOut - string with the target file full path
        pstrDelim - delimiter used in the source file
        pstrMode - mode in which the process operates - append or overwrite

    Output:
        No value/object returned, a new file with one column of processed data
        is created during the process
    '''
    # check if the input file exists
    assert os.path.isfile(pstrIn), 'Source doesn\'t exist'

    # open the source file, read only
    objIn = open(pstrIn, 'r')

    # open the target file in append mode, if selected
    if strMode == 'append' and os.path.isfile(pstrOut):
        objOut = open(pstrOut, 'a')
    else:
        objOut = open(pstrOut, 'w')

    # parse every row of the source file and output it by word to the target file
    for strRow in objIn:
        # split the row to lines for csv parser
        lstLines = strRow.splitlines()

        # parse the split row to words by csv parser
        objParser = csv.reader(lstLines, delimiter = pstrDelim)

        # get the 'words' from the input
        lstWords = list(objParser)

        # process every word and write it to the new file
        for strWord in lstWords[0]:
            strSafeWord = fstrTreatWord(strWord)
            objOut.write(strSafeWord + '\n')

    # save and close the target file
    objOut.close()

    # close the source file
    objIn.close()


def fstrTreatWord(pstrWord):
    '''
    Wraps the word in quotes if it contains potential separators. Escapes double
    quotes.

    Inputs:
        pstrWord - string to be treated

    Output:
        treated string
    '''
    # copy the word for changes
    strTreated = pstrWord

    # replace every double quote with two double quotes
    if strTreated.find('"'):
        strTreated = strTreated.replace('"', '""')

    # try to find comma, semicolon, tab, two double quotes and space
    if (strTreated.find(',') >= 0 or strTreated.find(';') >= 0 or
        strTreated.find('\t') >= 0 or strTreated.find(' ') >= 0 or
        strTreated.find('""') >= 0):
        # close the word in quotations
        strTreated = '"' + strTreated + '"'

    return strTreated

def fRandomDelim():
    '''
    Generate random delimiter

    Inputs: None

    Outputs: randomly generated delimiter and its index in the delimiter list
    '''
    # set the set of possible delimiters to choose from
    lstDelims = [',', ';', ' ', '\t']

    # generate a random index based on the number of delimiters
    intRand = int(np.random.uniform() * len(lstDelims))

    # return random delimiter and its index
    return lstDelims[intRand], intRand
