import tensorflow as tf
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#normalize/scaling data
x_train = tf.keras.utilis.normalize(x_train, axis=1)
x_test = tf.keras.utilis.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add = (tf.keras.layers.Flatten())
model.add = (tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add = (tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add = (tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(oprtimizer="adam",
                loss="sparse_categorical_crossenthropy",
                metrics = ["accuracy"]
                )
model.fit(x_train, y_train, epochs = 3)
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)
import matplotlib.pyplot as plt
plt.imshow(x_train[0]) #shows the data to feed to our neuron
plt.show(x_train[0], cmp = plt.cm.binary)#shows the number
print(x_train[0])#shows the multidemensional array of the data  