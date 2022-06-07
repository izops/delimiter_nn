# test the keras tutorial
import tensorflow as tf
from tensorflow import keras

(x_train, y_train), (x_val, y_val) = keras.datasets.fashion_mnist.load_data()

print(type(x_train[0]))

# def preprocess(x, y):
#   x = tf.cast(x, tf.float32) / 255.0
#   y = tf.cast(y, tf.int64)
#
#   return x, y
#
# def create_dataset(xs, ys, n_classes=10):
#   ys = tf.one_hot(ys, depth=n_classes)
#   return tf.data.Dataset.from_tensor_slices((xs, ys)) \
#     .map(preprocess) \
#     .shuffle(len(ys)) \
#     .batch(128)
#
#
# train_dataset = create_dataset(x_train, y_train)
# val_dataset = create_dataset(x_val, y_val)
#
# intCount = 0
#
# for i in x_train:
#     print(type(i))
#
#     if intCount == 0:
#         break
#     else:
#         intCount += 1
