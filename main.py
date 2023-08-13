from ast import arguments
from email import parser
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import argparse
import tensorflow_hub as hub
import keras
from tensorflow.keras import optimizers


print(tf.__version__)

DEFAULT_DIR="/home/bryan/Documents/GITHUB/PlantCV/data/mini_dataset"


batch_size = 10
img_height = 224
img_width = 224

parser=argparse.ArgumentParser()
parser.add_argument("--data-dir",default=DEFAULT_DIR)
args=parser.parse_args()



train_ds = tf.keras.utils.image_dataset_from_directory(
  args.data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
  args.data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)



normalization_layer = tf.keras.layers.Rescaling(1./255)
train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))

model = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5",
                  trainable=True)])
model.build([None, img_height, img_width, 3])  # Batch input shape.


AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


optimizer=optimizers.Adam(lr=0.005)
model.compile(
  optimizer=optimizer,
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])


#Training step
checkpoint_path = "weights/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1,
                                                 save_freq=1)


model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=3,callbacks=[cp_callback]
)
