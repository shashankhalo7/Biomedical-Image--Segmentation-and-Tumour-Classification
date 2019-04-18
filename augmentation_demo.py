## This is the augmentation_demo.py file

##importing all the packages
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
ap.add_argument("-o", "--output", required=True, help="path to the output directory")
ap.add_argument("-p", "--prefix", type=str,  default="image", help="output filename prefix")
args = vars(ap.parse_args())

print("[INFO] loading example image ....")
image = load_img(args["image"])
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

aug = ImageDataGenerator(rotation_range=50, width_shift_range=0.1, height_shift_range=0.1, brightness_range=(1, 1.3), shear_range=0.2,
                         horizontal_flip=True, vertical_flip=True, fill_mode="reflect")

total = 0

print("[INFO] generating images ....")
imageGen = aug.flow(image, batch_size=1, save_to_dir=args["output"],
           save_prefix=args["prefix"], save_format="jpg")

for images in imageGen:
    total += 1

    if total==40:
        break
