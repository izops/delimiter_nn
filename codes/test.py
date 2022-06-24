import tensorflow as tf
print('read in the trained model')
new_model = tf.keras.models.load_model('trained_model/cnn')
print('model imported')
