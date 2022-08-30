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
    name_data = STR_PATH_SLICE_FILES + p_name + '.slices'

    # save the slice without row indexes
    p_slice.to_csv(name_data, sep = p_separator, index = False)

def save_labels(p_slice, p_separator, p_name):
    # create file name for data labels
    name_label = STR_PATH_SLICE_FILES + p_name + '.labels'

    # get label of the current separator
    sep_label = DCT_SEPARATORS[p_separator]

    # create a text file with separator labels for each data row and header
    labels_file = open(name_label, 'w')

    for row_index in range(p_slice.shape[1] + 1):
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
    source_separators = [',', ',', ',']
    source_encoding = [None, None, 'latin1']

    # set the file name counter
    counter = 0

    for source_index in range(len(source_paths)):
        # read in the data
        current_source = read_source_data(
            source_paths[source_index],
            source_separators[source_index],
            source_encoding[source_index]
        )

        # calculate maximum number of iterations through the data
        iterate = int(current_source.shape[0] * current_source.shape[1] * 0.15)

        for sample_count in range(iterate):
            # generate data slice
            slice = generate_slice(current_source)

            # randomly generate index of separator to use
            sep_index = random.randint(0, 2)

            # get the list of all separators
            list_sep = list(DCT_SEPARATORS.keys())

            # save the data and labels with the random separator, use counter
            # as name
            save_bundle(slice, list_sep[sep_index], counter)

            # increment counter
            counter += 1

            # insert safety fuse
            if counter == 100000:
                break

# run the generator
generate_data()
