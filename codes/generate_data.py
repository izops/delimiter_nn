# generate data

import numpy as np, os

# define default output file names
STR_FILE_NAME_DATA = 'data.txt'
STR_FILE_NAME_LABELS = 'labels.txt'
STR_FILE_NAME_IN = 'outfile'
STR_FILE_EXTENSION_IN = '.txt'

def GenerateData(
    pstrPathSource,
    pintNumFiles,
    pintNumFileRows,
    pstrPathOut,
    pintNumCols
):
    assert os.path.isdir(pstrPathSource), 'Provide a path with source files'
    assert pintNumFiles > 0, 'No source files, can\'t continue'
    assert os.path.isdir(pstrPathOut), 'Provide an output path'
    assert pintNumCols > 0, 'There has to be at least one column in the output'

    # create output file path
    if pstrPathOut[-1] != '/':
        strPath = pstrPathOut + '/'
    else:
        strPath = pstrPathOut

    # open the output files for writing
    objData = open(strPath + STR_FILE_NAME_DATA, 'w')
    objLabels = open(strPath + STR_FILE_NAME_LABELS, 'w')

    # generate a random number based on the number of source files
    intFile = int(np.random.uniform() * pintNumFiles)

    # generate full name of the generated source file
    strFileIn = strPath + STR_FILE_NAME_IN + str(intFile) + STR_FILE_EXTENSION_IN

    # initialize empty lists for the file and for the output
    lstFile = list()
    lstOut = list()

    # open the source file
    objInFile = open(strFileIn)

    # read the file into the list
    for strRow in objInFile:
        lstFile.append(strRow)

    # generate a random array with possible row indexes
    npRowIndexes = np.random.rand(pintNumWords) * len(lstFile)
    npRowIndexes = npRowIndexes.astype(int)

    # generate a random delimiter and its label to

    # get the respective words and write them to data and labels
    for intIndex in range(len(npRowIndexes)):
        # get the selected word
        strWord = lstFile[npRowIndexes[intIndex]]

        # write selected word to data and generate respective labels
        WriteToFiles(objData, objLabels, strWord)

        # add the last symbol based on the position of the loop
        if intIndex == len(npRowIndexes) - 1:
            # last word, add line break
            objData.write('\n')
            objLabels.write('\n')
        else:
            # not the last word, add delimiter and its label



    # get a data row from the source file

def WriteToFiles(pobjData, pobjLabels, pstrWord):
    # do the operation only if the word is not missing
    if len(pstrWord) > 0:
        # generate array of zeros with as many zeros as characters in the word
        npLabels = np.zeros(len(pstrWord))

        # convert the array to integers and then to a list
        npLabels = npLabels.astype(int)
        lstLabels = npLabels.tolist()

        # convert the numeric list to a list of characters
        lstLabels = map(str, lstLabels)
        lstLabels = list(lstLabels)

        # create a single string with labels
        strLabels = ' '.join(lstLabels)

        # write the word to the data file and labels to the labels file
        pobjData.write(pstrWord)
        pobjLabels.write(strLabels)

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

    # set the delimiter to return
    strDelim = lstDelims[intRand]

    # set the numeric label to return
    intLabel = intRand + 1

    # return random delimiter and its index
    return strDelim, intLabel
