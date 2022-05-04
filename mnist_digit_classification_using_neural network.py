

#Importing the Dependencies


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from google.colab.patches import cv2_imshow
from PIL import Image
import tensorflow as tf
tf.random.set_seed(3)
from tensorflow import keras
from keras.datasets import mnist
from tensorflow.math import confusion_matrix

"""Loading the MNIST data from keras.datasets"""

(X_train, Y_train), (X_test, Y_test) =  mnist.load_data()

type(X_train)

# shape of the numpy arrays
print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)

"""Training data = 60,000 Images

Test data = 10,000 Images

Image dimension  --> 28 x 28

Grayscale Image  --> 1 channel
"""

# printing the 10th image

print(X_train[10])

print(X_train[10].shape)

# displaying the image

plt.imshow(X_train[25])
plt.show()

# print the corresponding label
print(Y_train[25])

"""Image Lables"""

print(Y_train.shape, Y_test.shape)

# unique values in Y_train
print(np.unique(Y_train))

# unique values in Y_test
print(np.unique(Y_test))

"""We can use these labels as such or we can also apply One Hot Encoding

All the images have the same dimensions in this dataset, If not, we have to resize all the images to a common dimension
"""

# scaling the values

X_train = X_train/255
X_test = X_test/255

# printing the 10th image

print(X_train[10])

"""Building the Neural Network"""

# setting up the layers of the Neural  Network

model = keras.Sequential([
                          keras.layers.Flatten(input_shape=(28,28)),
                          keras.layers.Dense(50, activation='relu'),
                          keras.layers.Dense(50, activation='relu'),
                          keras.layers.Dense(10, activation='sigmoid')
])

# compiling the Neural Network

model.compile(optimizer='adam',
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

# training the Neural Network

model.fit(X_train, Y_train, epochs=10)

"""Training data accuracy = 98.9%

**Accuracy on Test data:**
"""

loss, accuracy = model.evaluate(X_test, Y_test)
print(accuracy)

"""Test data accuracy = 97.1%"""

print(X_test.shape)

# first data point in X_test
plt.imshow(X_test[0])
plt.show()

print(Y_test[0])

Y_pred = model.predict(X_test)

print(Y_pred.shape)

print(Y_pred[0])

"""model.predict() gives the prediction probability of each class for that data point"""

# converting the prediction probabilities to class label

label_for_first_test_image = np.argmax(Y_pred[0])
print(label_for_first_test_image)

# converting the prediction probabilities to class label for all test data points
Y_pred_labels = [np.argmax(i) for i in Y_pred]
print(Y_pred_labels)

"""Y_test  -->  True labels

Y_pred_labels  -->  Predicted Labels

Confusin Matrix
"""

conf_mat = confusion_matrix(Y_test, Y_pred_labels)

print(conf_mat)

plt.figure(figsize=(15,7))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.ylabel('True Labels')
plt.xlabel('Predicted Labels')

"""Building a Predictive System

Prediction image link: https://camo.githubusercontent.com/3d9666a8f0c5658667292b74ca19295827c2b22a0e903db283998ae213e6f6e1/68747470733a2f2f646174616d61646e6573732e6769746875622e696f2f6173736574732f696d616765732f74665f66696c655f666565642f4d4e4953545f64696769742e706e67
"""

input_image_path = '/content/MNIST_digit.png'

input_image = cv2.imread(input_image_path)

type(input_image)

print(input_image)

cv2_imshow(input_image)

input_image.shape

grayscale = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

grayscale.shape

input_image_resize = cv2.resize(grayscale, (28, 28))

input_image_resize.shape

cv2_imshow(input_image_resize)

input_image_resize = input_image_resize/255

type(input_image_resize)

image_reshaped = np.reshape(input_image_resize, [1,28,28])

input_prediction = model.predict(image_reshaped)
print(input_prediction)

input_pred_label = np.argmax(input_prediction)

print(input_pred_label)

"""**Predictive System**"""

input_image_path = input('Path of the image to be predicted: ')

input_image = cv2.imread(input_image_path)

cv2_imshow(input_image)

grayscale = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

input_image_resize = cv2.resize(grayscale, (28, 28))

input_image_resize = input_image_resize/255

image_reshaped = np.reshape(input_image_resize, [1,28,28])

input_prediction = model.predict(image_reshaped)

input_pred_label = np.argmax(input_prediction)

print('The Handwritten Digit is recognised as ', input_pred_label)

