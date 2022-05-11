# create large one-column file for data generating

import os, csv

# define path of the source file
strPathIn = ''
strPathOut = ''

# check if the input file exists
assert os.path.isfile(strPathIn)

# make sure the output file doesn't exist (to not overwrite)
assert os.path.isfile(strPathOut) == False

# 
