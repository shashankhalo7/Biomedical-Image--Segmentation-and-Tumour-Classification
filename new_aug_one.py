from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np

prefix = "000001"

print("[INFO] loading example image ....")

image = load_img("C:/Users/PRIYANSHU SHARMA/Desktop/PRIYANSHU/IIITDM/000001.png")
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

images = load_img("C:/Users/PRIYANSHU SHARMA/Desktop/PRIYANSHU/IIITDM/gt_000001.png")
images = img_to_array(images)
images = np.expand_dims(images, axis=0)

data_gen_args = dict(rotation_range=50, width_shift_range=0.1, height_shift_range=0.1, brightness_range=(1, 1.3), shear_range=0.2,
                         horizontal_flip=True, vertical_flip=True, fill_mode="reflect")

aug = ImageDataGenerator(**data_gen_args)
mask = ImageDataGenerator(**data_gen_args)

total = 0
seed = 1

print("[INFO] generating images ....")

aug.fit(image, augment=True, seed=seed)
mask.fit(images, augment=True, seed=seed)


output = "C:/Users/PRIYANSHU SHARMA/Desktop/PRIYANSHU/IIITDM/Output"

imageGen = aug.flow(image, batch_size=1, save_to_dir=output,
           save_prefix=prefix, save_format="jpg", seed=seed)

for imagess in imageGen:
    total += 1

    if total==40:
        break

total = 0
output = "C:/Users/PRIYANSHU SHARMA/Desktop/PRIYANSHU/IIITDM/GT_Output"

imageGen = mask.flow(images, batch_size=1, save_to_dir=output,
           save_prefix=prefix, save_format="jpg", seed=seed)

for imagess in imageGen:
    total += 1

    if total==40:
        break

