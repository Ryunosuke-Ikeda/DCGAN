
from PIL import Image
import os, glob
import numpy as np

image_size= 64

#元データの場所
photos_dir = "############" 

#作ったデータの保存場所
reshape_dir="###########"

files = glob.glob(photos_dir + "/*.jpg")


for i, file in enumerate(files):   
    image = Image.open(file)
    image = image.convert("RGB")
    image = image.resize((image_size, image_size))
    image.save("{]{}.jpg".format(reshape_dir,i))
    


    

