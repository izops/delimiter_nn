# import modules and functions
import numpy as np
import tensorflow as tf
from tensorflow import keras
from random import shuffle
import data_preparation as dp

# set paths
strPathData = 'data/output/sample_data.txt'
strPathLabels = 'data/output/sample_labels.txt'
strPathCheckpoints = 'trained_model/epoch_{epoch:02d}'

# set number of classes to assign in the datasets
INT_NUM_CLASSES = 3

# set the size of the data subsets
DATA_SIZE_TRAIN = 0.85

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

# shuffle training data
lstNewOrder = list(range(data_train.shape[0]))
shuffle(lstNewOrder)
data_train = data_train[lstNewOrder, :]
labels_train = labels_train[lstNewOrder, ]

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

# define a keras model structure
model = keras.Sequential([
    keras.layers.Conv1D(64, kernel_size = 8, padding = 'SAME', input_shape = (100, 1)),
    keras.layers.Conv1D(64, kernel_size = 8, padding = 'SAME'),
    keras.layers.MaxPool1D(2),
    keras.layers.Dropout(0.7),
    keras.layers.BatchNormalization(),
    keras.layers.Conv1D(128, kernel_size = 4, padding = 'SAME'),
    keras.layers.Conv1D(128, kernel_size = 4, padding = 'SAME'),
    keras.layers.MaxPool1D(2),
    keras.layers.Dropout(0.3),
    keras.layers.BatchNormalization(),
    keras.layers.Conv1D(256, kernel_size = 2, padding = 'SAME'),
    keras.layers.Conv1D(256, kernel_size = 2, padding = 'SAME'),
    keras.layers.Flatten(),
    keras.layers.Dense(256, activation = 'relu'),
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(32, activation = 'relu'),
    keras.layers.Dense(3, activation = 'softmax')
])

# compile the neural network
model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['categorical_accuracy']
)

# define learning rate schedule function
def lr_schedule(epoch, lr):
    # set new learning rate default value
    new_learning = lr

    # change learning rate depending on the epoch
    if epoch > 0 and epoch < 10:
        new_learning = new_learning * 0.99
    elif epoch >= 10:
        new_learning = new_learning * 0.85

    return new_learning

# define learning rate schedule callback
scheduler_callback = tf.keras.callbacks.LearningRateScheduler(
    lr_schedule,
    verbose = 1
)

# define callback for saving the model
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath = strPathCheckpoints,
    save_freq = 'epoch',
    monitor = 'val_categorical_accuracy',
    mode = 'max',
    verbose = 1
)

# define callback for reducing learning rate on plateau
plateau_callback = tf.keras.callbacks.ReduceLROnPlateau(
    monitor = 'val_categorical_accuracy',
    factor = 0.2,
    patience = 3,
    mode = 'max',
    min_delta = 0.001,
    min_lr = 0.00001,
    verbose = 1
)

# define callback for early stopping
stopping_callback = tf.keras.callbacks.EarlyStopping(
    monitor = 'val_categorical_accuracy',
    min_delta = 0.001,
    patience = 5,
    mode = 'max',
    restore_best_weights = False,
    verbose = 1
)

# train the model
CNN_history = model.fit(
	train_x,
	train_y,
	epochs = 30,
	batch_size = 128,
    validation_data = (test_x, test_y),
    callbacks = [
        checkpoint_callback,
        plateau_callback,
        stopping_callback,
        scheduler_callback
    ]
)

# save the model history
np.save('train_history.npy', CNN_history.history)
