# import modules and functions
import numpy as np
import tensorflow as tf
from tensorflow import keras
import data_preparation as dp

# set paths
strPathData = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/sample_data.txt'
strPathLabels = 'c:/Users/ivan.zustiak/OneDrive - Zurich Insurance/snake/emea_oth_nn_separator/data/output/sample_labels.txt'

# set number of classes to assign in the datasets
INT_NUM_CLASSES = 5

print('Importing the data')

# import data
lstData = dp.flstReadData(strPathData)
lstLabels = dp.flstReadData(strPathLabels, True)

# convert data to numpy arrays
source_data = np.array(lstData)
source_labels = np.array(lstLabels)

# normalize data
train_x = tf.cast()

# convert labels to one hot
train_y = tf.one_hot(source_labels, depth = INT_NUM_CLASSES)

print('Data import finished')
print('Converting to tensors')

# create tensor datasets
train_x = tf.data.Dataset.from_tensor_slices(source_data)
train_y = tf.data.Dataset.from_tensor_slices(source_labels)
print('Conversion to tensors finished for the data')

# define a function to normalize datasets
def normalize(nValue):
    nValue = tf.cast(nValue, tf.float32) / 127.0
    return nValue

# normalize the data
train_x = train_x.map(normalize)

# build a keras model
model = keras.Sequential([
    keras.layers.Dense(units = 100, activation = 'relu'),
    keras.layers.Dense(units = 88, activation = 'relu'),
    keras.layers.Dense(units = 79, activation = 'relu'),
    keras.layers.Dense(units = 75, activation = 'relu'),
    keras.layers.Dense(units = 75, activation = 'relu'),
    keras.layers.Dense(units = 75, activation = 'relu'),
    keras.layers.Dense(units = 75, activation = 'relu'),
    keras.layers.Dense(units = 75, activation = 'relu'),
    keras.layers.Dense(units = INT_NUM_CLASSES, activation = 'softmax')
])

# compile the neural network
model.compile(
    optimizer = 'adam',
    loss = tf.losses.CategoricalCrossentropy(from_logits = True),
    metrics = ['accuracy']
)

trained = model.fit(

)
