# import modules and functions
import tensorflow as tf
import data_preparation as dp

# set paths
strPathData = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/sample_data.txt'
strPathLabels = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/sample_labels.txt'

# import data
lstData = dp.flstReadData(strPathData)
lstLabels = dp.flstReadData(strPathLabels, True)

# create tensors
train_data = tf.data.Dataset.from_tensor_slices(lstData)
train_labels = tf.data.Dataset.from_tensor_slices(lstLabels)

for e in train_data:
    print(e)
