# import modules and functions
import numpy as np
import tensorflow as tf
from tensorflow import keras
import data_preparation as dp

# set paths
strPathGeneral = 'C:/Users/IVAN.ZUSTIAK/Documents/repositories/emea_oth_nn_separator/data/output/'
strPathData = strPathGeneral + 'sample_data.txt'
strPathLabels = strPathGeneral + 'sample_labels.txt'

# set number of classes to assign in the datasets
INT_NUM_CLASSES = 5

# set the size of the data subsets
DATA_SIZE_TRAIN = 0.9

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
# model = keras.Sequential([
#     keras.layers.Reshape(target_shape = (100,), input_shape = (100, )),
#     keras.layers.Dense(units = 100, activation = 'relu'),
#     keras.layers.Dense(units = 160, activation = 'relu'),
#     keras.layers.Dense(units = 128, activation = 'relu'),
#     keras.layers.Dense(units = 64, activation = 'relu'),
#     keras.layers.Dense(units = 128, activation = 'relu'),
#     keras.layers.Dense(units = 96, activation = 'relu'),
#     keras.layers.Dense(units = 48, activation = 'relu'),
#     keras.layers.Dense(units = 16, activation = 'relu'),
#     keras.layers.Dense(units = INT_NUM_CLASSES, activation = 'softmax')
# ])

# build a different model
model = keras.Sequential([
    keras.layers.Conv1D(32, kernel_size = 32, padding = 'SAME', input_shape = (100, 1)),
    keras.layers.MaxPool1D(2),
    keras.layers.Conv1D(32, kernel_size = 16, padding = 'SAME'),
    keras.layers.MaxPool1D(2),
    keras.layers.Conv1D(32, kernel_size = 5, padding = 'SAME'),
    keras.layers.MaxPool1D(2),
    keras.layers.Conv1D(8, kernel_size = 5),
    keras.layers.MaxPool1D(2),
    keras.layers.Flatten(),
    keras.layers.Dense(32, activation = 'relu'),
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(64, activation = 'relu'),
    keras.layers.Dense(64, activation = 'relu'),
    keras.layers.Dense(32, activation = 'relu'),
    keras.layers.Dense(24, activation = 'relu'),
    keras.layers.Dense(10, activation = 'relu'),
    keras.layers.Dense(INT_NUM_CLASSES, activation = 'softmax')
])

# compile the neural network
model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['categorical_accuracy']
)

# train the model
# trained = model.fit(
#     train_x,
#     train_y,
#     epochs = 80,
#     batch_size = 128,
#     validation_data = test_data
# )

trained = model.fit(
    train_x,
    train_y,
    epochs = 25,
    batch_size = 128,
    validation_data = test_data
)
