# process the data for neural network
import os

def flstReadData(
    pstrPath,
    is_label = False,
    zero_pad = True,
    required_length = 100
):
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
        if not is_label:
            # modify the data to match requirements
            lstRow = flstListifyRow(strRow, zero_pad, required_length)
        else:
            # convert labels to clean form
            strProcessed = strRow.replace('\n', '')
            lstRow = int(strProcessed)

        # add row to the list
        lstData.append(lstRow)

    return lstData

def flstListifyRow(pstrRow, zero_pad = True, required_length = 100):
    assert type(pstrRow) == str, 'Not a string, can\'t continue'

    # remove the line breaks from the string
    strProcessed = pstrRow.replace('\n', '')

    # convert the string to ASCII list
    lstSplit = list(map(ord, strProcessed))

    # modify the list to match length requirements
    # if zero padding is not required, shortening should not be either (RNN)
    if zero_pad:
        if len(lstSplit) < required_length:
            # zero padding required, match it
            lstSplit = flstZeroPad(lstSplit, required_length)
        else:
            # shorten the string to the required length
            lstSplit = lstSplit[:required_length]

    return lstSplit

def flstZeroPad(plstInput, pintLength):
    '''
    Create zero padding of a list to required length.

    Inputs:
        plstInput - input list to zero pad
        pintLength - length to which the list will be zero padded

    Output:
        List zero-padded to a required length
    '''
    # create zero padding with the required length
    lstZeros = [0] * (pintLength - len(plstInput))

    # concatenate the lists
    lstProcessed = plstInput + lstZeros

    return lstProcessed
