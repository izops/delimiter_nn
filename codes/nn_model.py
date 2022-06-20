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

# set the size of the data subsets
DATA_SIZE_TRAIN = 0.7

print('Importing the data')

# import data
lstData = dp.flstReadData(strPathData)
lstLabels = dp.flstReadData(strPathLabels, True)

# set the length of the train data
intLengthTrain = int(DATA_SIZE_TRAIN * len(lstData))

# split the data to train and test
lstDataTrain = lstData[:intLengthTrain]
lstDataTest = lstData[intLengthTrain:]

# split the labels data to train and test
lstLabelsTrain = lstLabels[:intLengthTrain]
lstLabelsTest = lstLabels[intLengthTrain:]

# convert data to numpy arrays
data_train = np.array(lstDataTrain)
data_test = np.array(lstDataTest)
labels_train = np.array(lstLabelsTrain)
labels_test = np.array(lstLabelsTest)

# normalize the data
train_x = data_train / 127.0
test_x = data_test / 127.0
labels_train = labels_train / 1.0
labels_test = labels_test / 1.0
# convert labels to one hot
train_y = tf.one_hot(labels_train, depth = INT_NUM_CLASSES)
test_y = tf.one_hot(labels_test, depth = INT_NUM_CLASSES)

print('Data import finished')
print('Converting to tensors')

# create tensor datasets
train_data = tf.data.Dataset.from_tensor_slices((train_x, train_y)).batch(16)
test_data = tf.data.Dataset.from_tensor_slices((test_x, test_y)).batch(16)
print('Conversion to tensors finished')

# build a keras model
model = keras.Sequential([
    keras.layers.Reshape(target_shape = (100,), input_shape = (100, )),
    keras.layers.Dense(units = 100, activation = 'relu'),
    keras.layers.Dense(units = 88, activation = 'relu'),
    keras.layers.Dense(units = 79, activation = 'relu'),
    keras.layers.Dense(units = INT_NUM_CLASSES, activation = 'softmax')
])

# compile the neural network
model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['categorical_accuracy']
)

# train the model
trained = model.fit(
    train_x,
    train_y,
    epochs = 40,
    steps_per_epoch = 2500,
    validation_data = test_data,
    validation_steps = 2
)
