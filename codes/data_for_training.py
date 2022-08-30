# generate valid training data

import pandas as pd
import random

# set constants

# set size of the data sample
INT_SAMPLE_ROW_COUNT = 50

# set path to output files
STR_PATH_SLICE_FILES = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/slices/'

# set available separators and their labels
DCT_SEPARATORS = {',': '0', ';': '1', '\t': '2'}

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

def save_slice(p_slice, p_separator, p_name):
    # create file name for slice
    name_data = STR_PATH_SLICE_FILES + p_name + '.slice'

    # save the slice
    p_slice.to_csv(name_data, sep = p_separator)

def save_labels(p_slice, p_separator, p_name):
    # create file name for data labels
    name_label = STR_PATH_SLICE_FILES + p_name + '.label'

    # get label of the current separator
    sep_label = DCT_SEPARATORS[p_separator]

    # create a text file with separator labels for each data row and header
    labels_file = open(name_label, 'w')

    for row_index in 0:p_slice.shape[1]:
        # save current label in a separate row
        labels_file.write(sep_label + '\n')

    # close the file
    labels_file.close()

def save_bundle(p_slice, p_separator, p_name):
    save_slice(p_slice, p_separator, p_name)
    save_labels(p_slice, p_separator, p_name)

def generate_data():
    # set the list of source data to be used
    source_paths = [
        'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/sources/vertrag.csv',
        'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/sources/exposure.csv',
        'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/sources/wtw.csv'
    ]
