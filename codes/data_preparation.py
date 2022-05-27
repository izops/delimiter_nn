# process the data for neural network
import os

def flstReadData(pstrPath, zero_pad = True, required_length = 100):
    '''
    Imports a text file to a list

    Inputs:
        pstrPath - full file path containing the data

    Output: list containing imported data from the text file
    '''
    # check that the file exists
    assert os.path.isfile(pstrPath), 'This is not a valid file'

    # open the file for reading
    objData = open(pstrPath, 'r')

    # initialize an empty list for storing the data
    lstData = []

    # read in each row into the list
    for strRow in objData:
        # remove line breaks from the row
        strRead = strRow.replace('\n', '')

        # break down the row to separate characters
        lstRow = list(strRead)

        # add row to the list
        lstData.append(lstRow)

    return lstData

def flstConvertToASCII(plstData):
    # check if the input is a list
    assert type(plstData) == list, 'The input must be a list of data'

    # initialize an empty list for outputs
    lstOut = []

    # convert each sublist to an ASCII code
    for lstSublist in plstData:
        lstOut.append(list(map(ord, lstSublist)))

    return lstOut

def flstListifyRow(pstrRow, zero_pad = True, required_length = 100):
    assert type(pstrRow) == str, 'Not a string, can\'t continue'

    # remove the line breaks from the string
    strProcessed = pstrRow.replace('\n', '')

    # modify the string to match length requirements
    if zero_pad:
        if len(strProcessed) < required_length:
            # zero padding required, match it
            strProcessed = fstrZeroPad(strProcessed, required_length)

def fstrZeroPad(pstrInput, pintLength):
    '''
    Create zero padding of a string to required length.

    Inputs:
        pstrInput - input string to zero pad
        pintLength - length to which the string will be zero padded

    Output:
        String zero-padded to a required
    '''
    # create zero padding with the required length
    strZeros = '0' * (pintLength - len(pstrInput))

    # concatenate the strings
    strProcessed = pstrInput + strZeros

    return strProcessed
