#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os
import sys  #For the Source command"
import matplotlib.image
import numpy as np
#These are ours
import setpaths
import setparams

# Set the run name to label the images
RUN_NAME = setparams.set_RUN_NAME()
#print(RUN_NAME)

#Defines where the images are located
IMGS_DIR = setpaths.set_image_path()
do_3Dplot = setparams.set_do3Dplot()
do_2Dslice = setparams.set_do2Dslice()
do_2Dtransect = setparams.set_do2Dtransect()
plotnames = []
#TP_EPA_LAYER=1_T
if(do_3Dplot):
    plotnames.append("_LAYER=1_")
if(do_2Dslice):
    plotnames.append("_slice_")
if(do_2Dtransect):
    plotnames.append("_transect_")

OUT_DIR = IMGS_DIR + "multi-layer/"
#Create a directory for images if one doesn't exist.
#Note, existing files will be overwritten
if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)


for img in range(2199):
    #print(img)
    #print(pname)
    img1 = matplotlib.image.imread(IMGS_DIR + 'SYMLINKS/' + 'TP_EPA'+ '_LAYER=1_' + RUN_NAME + "." + str(img).zfill(4) + ".png")
    img2 = matplotlib.image.imread(IMGS_DIR + 'SYMLINKS/' + 'TP_COMPARE'+ '_LAYER=1_' + RUN_NAME + "." + str(img).zfill(4) + ".png")
    img3 = matplotlib.image.imread(IMGS_DIR + 'SYMLINKS/' + 'TP_EPA'+ '_LAYER=19_' + RUN_NAME +  "." + str(img).zfill(4) + ".png")
    img4 = matplotlib.image.imread(IMGS_DIR + 'SYMLINKS/' + 'TP_COMPARE'+ '_LAYER=19_' + RUN_NAME +  "." + str(img).zfill(4) + ".png")
    #x = 1
    #print(IMGS_DIR + 'SYMLINKS/' + 'TP_COMPARE'+ '_LAYER=19_' + RUN_NAME +  "." + str(img).zfill(4) + ".png")
    row1 = np.concatenate((img1, img2), axis=1)
    row2 = np.concatenate((img3, img4), axis=1)
    new_image = np.concatenate((row1, row2))

    matplotlib.image.imsave(OUT_DIR + RUN_NAME + "." + str(img).zfill(4)+".png", new_image)
    #print(OUT_DIR + RUN_NAME + "." + str(img).zfill(4) + ".png")

