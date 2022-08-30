# generate valid training data

import pandas as pd
import random

# set constants

# set size of the data sample
INT_SAMPLE_ROW_COUNT = 50

# set path to output files
STR_PATH_SLICE_FILES = 'data/output/slices/'

# set available separators and their labels
DCT_SEPARATORS = {',': '0', ';': '1', '\t': '2'}

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
    name_data = STR_PATH_SLICE_FILES + str(p_name) + '.slices'

    # save the slice without row indexes
    p_slice.to_csv(name_data, sep = p_separator, index = False)

def save_labels(p_slice, p_separator, p_name):
    # create file name for data labels
    name_label = STR_PATH_SLICE_FILES + str(p_name) + '.labels'

    # get label of the current separator
    sep_label = DCT_SEPARATORS[p_separator]

    # create a text file with separator labels for each data row and header
    labels_file = open(name_label, 'w')

    for row_index in range(p_slice.shape[0] + 1):
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
        'data/sources/vertrag.csv',
        'data/sources/exposure.csv',
        'data/sources/wtw.csv'
    ]
    source_separators = [',', ',', ',']
    source_encoding = ['latin1', None, None]

    # set the file name counter
    counter = 0

    for source_index in range(len(source_paths)):
        # insert safety fuse
        if counter == 100000:
            break

        # read in the data
        current_source = read_source_data(
            source_paths[source_index],
            source_separators[source_index],
            source_encoding[source_index]
        )

        # calculate maximum number of iterations through the data
        iterate = int(current_source.shape[0] * current_source.shape[1] * 0.12)

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

            # print checkpoints
            if counter % 1000 == 0 and counter > 0:
                print(str(counter/1000) + 'k files generated')

            # insert safety fuse
            if counter == 100000:
                break
            else:
                # increment counter
                counter += 1

def total_data():
    # set the number of existing files
    num_files = 137915

    # create data and labels files
    data_file = open('data/output/data.txt', 'w')
    labels_file = open('data/output/labels.txt', 'w')

    # append all files together
    file_index = 0

    while file_index <= num_files:
        # read data slice
        read_data = open('data/output/slices/' + str(file_index) + '.slices')

        for row in read_data:
            data_file.write(row)

        read_data.close()

        # read labels slice
        read_label = open('data/output/slices/' + str(file_index) + '.labels')

        for row in read_label:
            labels_file.write(row)

        read_label.close()

        # log output
        if file_index % 1000 == 0 and file_index > 0:
            print(str(int(file_index / 1000)) + 'k files read')

        # next slice
        file_index += 1

    # close the files
    data_file.close()
    labels_file.close()

total_data()
