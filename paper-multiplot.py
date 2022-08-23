#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os
import sys  #For the Source command"
import matplotlib.image
import numpy as np
import re

#This defines the plot parameters
import getfilenames
mifiles = getfilenames.set_which_mifiles()

#Which layers
which_layers = [1,3,4,5]

#Defines where the images are located
IMGS_DIR = "/Users/lllowe/JamesPaper/Images-2015/"

OUT_DIR = IMGS_DIR + "multi/"
#Create a directory for images if one doesn't exist.
#Note, existing files will be overwritten
if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

for img in range(174):
    #print(img)
    url = mifiles[img]
    url = re.sub('\.nc','',url)
    img1 = matplotlib.image.imread(IMGS_DIR + "LAYER=1/" + url + "_Layer=1.png")
    img2 = matplotlib.image.imread(IMGS_DIR + "LAYER=3/" + url + "_Layer=3.png")
    img3 = matplotlib.image.imread(IMGS_DIR + "LAYER=4/" + url + "_Layer=4.png")
    img4 = matplotlib.image.imread(IMGS_DIR + "LAYER=5/" + url + "_Layer=5.png")
    row1 = np.concatenate((img1, img2), axis=1)
    row2 = np.concatenate((img3, img4), axis=1)
    new_image = np.concatenate((row1, row2))
    matplotlib.image.imsave(OUT_DIR + url +".png", new_image)

