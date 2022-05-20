# split a single large file to small files by set number of rows

# import modules
import os

def SplitFile(pstrPathIn, pstrPathOut, pintNumRows):
    '''
    Splits a text file to smaller files with the predefined number of rows

    Inputs:
        pstrPathIn - full path and file name of the source file to split
        pstrPathOut - path to folder where the output files will be saved
        pintNumRows - number of rows of the new files

    Outputs: None
        The output path contains ceil(infile length / pintNumRows) files with
        the rows from the source file
    '''
    # define default file name and extension
    STR_FILE = 'outfile'
    STR_EXTENSION = '.txt'

    # check that the source file exists
    assert os.path.isfile(pstrPathIn), 'The source file doesn\'t exist'

    # check if the output path exists, if not, create it
    if not os.path.exists(pstrPathOut):
        # create the directory and inform the user
        os.makedirs(pstrPathOut)
        print('New folder was created to store output: ' + pstrPathOut)

    # initialize file and row counters
    intF = 0
    intR = 0

    # open the source file
    objSource = open(pstrPathIn, 'r')

    # add slash to the output path if needed
    if pstrPathOut[-1] != '/':
        strPathOut = pstrPathOut + '/'
    else:
        strPathOut = pstrPathOut

    # split the file to smaller files by set number of rows
    for strRow in objSource:
        # create a new file
        if intR % pintNumRows == 0:
            # close the previous file if it exists
            if intF > 0:
                objCurrentTarget.close()

            # create a new file full path
            strFile = strPathOut + STR_FILE + str(intF) + STR_EXTENSION

            # create a new file to write to
            objCurrentTarget = open(strFile, 'w')

            # increment the file counter
            intF += 1

        # write rows to the current target file
        objCurrentTarget.write(strRow)

        # increment rows counter
        intR += 1

    # close the last target file
    objCurrentTarget.close()

    # close the source file
    objSource.close()

    # inform the user about the process end (use intF because of 0-indexing)
    print('The file has been successfully split to ' + str(intF) + ' files.')

p1 = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/source.txt'
p2 = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/split'
i1 = 1000
SplitFile(p1, p2, i1)
