# generate valid training data

import pandas as pd
import random

# set size of the data sample
INT_SAMPLE_ROW_COUNT = 50

# set path to data
str_data_path = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/sources/vertrag.csv'
str_data_path = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/sources/exposure.csv'

# import source file to memory
data_source = pd.read_csv(str_data_path, encoding = 'latin1')

def read_source_data(pstr_file_path, pstrSep, p_encoding = None):
    if p_encoding is None:
        loaded_data = pd.read_csv(pstr_file_path, sep = pstrSep)
    else:
        loaded_data = pd.read_csv(
            pstr_file_path,
            sep = pstrSep,
            encoding = p_encoding
        )

    return loaded_data

def generate_slice(p_data):
    # get the dimensions of the source data
    data_size = p_data.shape

    # set behavior based on the required treshold
    if data_size[0] < INT_SAMPLE_ROW_COUNT:
        # not enough data to meet sample requirements, start from the first row
        start_row = 0
    else:
        # generate a random row index to start from based on the data size
        start_row = random.randint(
            INT_SAMPLE_ROW_COUNT,
            data_size[0] - INT_SAMPLE_ROW_COUNT
        )

    # create a slice starting with a randomly selected row
    slice = p_data.iloc[start_row:(start_row + INT_SAMPLE_ROW_COUNT), :]

    # generate random number of columns based on the data size
    col_count = random.randint(1, data_size[1])

    # generate a list of column indexes to use
    col_indexes = random.sample(range(data_size[1]), col_count)

    # select random columns from the slice
    slice = slice.iloc[:, col_indexes]

    return slice

asdf = generate_slice(data_source)
print(asdf.head())
