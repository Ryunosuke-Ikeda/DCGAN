
from PIL import Image
import os, glob
import numpy as np

image_size= 64

photos_dir = "/Users/ryunosuke/Desktop/python/GAN_torch/human_tri/jpeg" 

files = glob.glob(photos_dir + "/*.jpg")


for i, file in enumerate(files):   
    image = Image.open(file)
    image = image.convert("RGB")
    image = image.resize((image_size, image_size))
    image.save("/Users/ryunosuke/Desktop/python/GAN_torch/resizeall/jpg/{}.jpg".format(i))
    


    

