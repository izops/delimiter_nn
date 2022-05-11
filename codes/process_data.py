# create large one-column file for data generating

import os, csv

# define modes to use ('append' vs 'overwrite')
strMode = 'append'

# define path of the source file
strPathIn = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/sources/MP_AU_VERTRAG_INVENTUR_20210312.asc'
strPathOut = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/out1.txt'

# check if the input file exists
assert os.path.isfile(strPathIn), 'Source doesn\'t exist'

# open the source file, read only
objIn = open(strPathIn, 'r')

# open the target file in append mode, if selected
if strMode == 'append' and os.path.isfile(strPathOut):
    objOut = open(strPathOut, 'a')
else:
    objOut = open(strPathOut, 'w')


# save and close the target file
objOut.save()
objOut.close()

# close the source file
objIn.close()
