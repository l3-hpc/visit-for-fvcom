#Makes one row of 4 images

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys  #For the Source command"
import matplotlib.image
import numpy as np
import setpaths

#read from setpaths.py
IMGS_DIR = setpaths.set_image_path()


image_suffix = [ 
"_transect_01-01-2010_00-00-00.png",
"_transect_01-31-2010_00-00-00.png",
"_transect_03-02-2010_00-00-00.png",
"_transect_04-01-2010_00-00-00.png",
"_transect_05-01-2010_00-00-00.png",
"_transect_05-31-2010_00-00-00.png",
"_transect_06-30-2010_00-00-00.png",
"_transect_07-30-2010_00-00-00.png",
"_transect_08-29-2010_00-00-00.png",
"_transect_09-28-2010_00-00-00.png",
"_transect_10-28-2010_00-00-00.png",
"_transect_11-27-2010_00-00-00.png",
"_transect_12-27-2010_00-00-00.png"
]

for img in image_suffix:
    img1 = matplotlib.image.imread(IMGS_DIR + 'TP_EPA'+ img)
    img2 = matplotlib.image.imread(IMGS_DIR + 'TP_Mark'+ img)
    img3 = matplotlib.image.imread(IMGS_DIR + 'TP_diff'+ img)
    img4 = matplotlib.image.imread(IMGS_DIR + 'TP_percent_change'+ img)
    row1 = np.concatenate((img1, img2, img3, img4), axis=1)
    matplotlib.image.imsave(IMGS_DIR + 'new'+img, row1)
