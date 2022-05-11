# create large one-column file for data generating

import os, csv

# define path of the source file
strPathIn = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/sources/in1.txt'
strPathOut = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/out1.txt'

# check if the input file exists
assert os.path.isfile(strPathIn)

# make sure the output file doesn't exist (to not overwrite)
assert os.path.isfile(strPathOut) == False

#
