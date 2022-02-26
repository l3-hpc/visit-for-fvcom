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
if(do_3Dplot):
    plotnames.append("_")
if(do_2Dslice):
    plotnames.append("_slice_")
if(do_2Dslice):
    plotnames.append("_transect_")



image_suffix = [ 
".01-01-2010_00-00-00.png",
".01-31-2010_00-00-00.png",
".03-02-2010_00-00-00.png",
".04-01-2010_00-00-00.png",
".05-01-2010_00-00-00.png",
".05-31-2010_00-00-00.png",
".06-30-2010_00-00-00.png",
".07-30-2010_00-00-00.png",
".08-29-2010_00-00-00.png",
".09-28-2010_00-00-00.png",
".10-28-2010_00-00-00.png",
".11-27-2010_00-00-00.png",
".12-27-2010_00-00-00.png"
]

for img in image_suffix:
    #print(img)
    for pname in plotnames:
        #print(pname)
        img1 = matplotlib.image.imread(IMGS_DIR + 'TP_EPA'+ pname + RUN_NAME + img)
        img2 = matplotlib.image.imread(IMGS_DIR + 'TP_COMPARE'+ pname + RUN_NAME + img)
        img3 = matplotlib.image.imread(IMGS_DIR + 'TP_diff'+ pname + RUN_NAME + img)
        img4 = matplotlib.image.imread(IMGS_DIR + 'TP_percent_change'+ pname + RUN_NAME + img)

        row1 = np.concatenate((img1, img2), axis=1)
        row2 = np.concatenate((img3, img4), axis=1)
        new_image = np.concatenate((row1, row2))

        matplotlib.image.imsave(IMGS_DIR + 'new' + pname + RUN_NAME + img, new_image)


