# process the data for neural network
import os

def flstReadData(pstrPath):
    '''
    Imports a data text file to a list

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
