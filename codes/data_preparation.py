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

    # get the file name from path
    strFileName = pstrPath[pstrPath.rfind('/') + 1:]

    # open the file for reading
    objData = open(pstrPath, 'r')

    # initialize a loop counter
    intCounter = 0

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

        # output counter info
        if (intCounter + 1) % 100000 == 0:
            print(str(intCounter + 1) + ' rows were read from ' + strFileName)

        # increment the counter
        intCounter += 1

    return lstData

def flstListifyRow(pstrRow, zero_pad = True, required_length = 100):
    '''
    flstListifyRow - prepares string input to the form where each character is
        a separate list item with its respective ASCII value. It zero-pads
        the list to the required length (zero in ASCII corresponds to NULL).
        Zero-padding is dependent on a separate function, flstZeroPad

    Inputs:
        pstrRow - string that should be converted to a list of ASCII codes
        zero_pad - if set to True, the function will keep the required lenght
            of the output list. In case the length of the list does not reach
            required length, the remaining length is supplemented with zeros
        required_length - the length at which the string will be cut off, and
            upto which it will be zero-padded

    Outputs:
        List of ASCII values converted from the input string, each value
        representing a separate character. If zero-padding is selected, the list
        is complemented with zeros at the indexes where its lenght doesn't reach
        the required length
    '''
    assert type(pstrRow) == str, 'Not a string, can\'t continue'
    assert required_length > 0, 'The output must have positive length'

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
