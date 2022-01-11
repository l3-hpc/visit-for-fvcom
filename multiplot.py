#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys  #For the Source command"
import matplotlib.image
import numpy as np

#Source("setpaths.py")
#Put full path for Mac:
#Source("/Users/lisalowe/visit-for-fvcom/setpaths.py")
import setpaths
#The above will define IMGS_DIR 

IMGS_DIR = "/Users/lisalowe/All_Images/"


image_suffix = [ 
"_01-01-2010_00-00-00.png",
"_01-31-2010_00-00-00.png",
"_03-02-2010_00-00-00.png",
"_04-01-2010_00-00-00.png",
"_05-01-2010_00-00-00.png",
"_05-31-2010_00-00-00.png",
"_06-30-2010_00-00-00.png",
"_07-30-2010_00-00-00.png",
"_08-29-2010_00-00-00.png",
"_09-28-2010_00-00-00.png",
"_10-28-2010_00-00-00.png",
"_11-27-2010_00-00-00.png",
"_12-27-2010_00-00-00.png"
]

for img in image_suffix:

    img1 = matplotlib.image.imread(IMGS_DIR + 'TP_EPA'+ img)
    img2 = matplotlib.image.imread(IMGS_DIR + 'TP_Mark'+ img)
    img3 = matplotlib.image.imread(IMGS_DIR + 'TP_diff'+ img)
    img4 = matplotlib.image.imread(IMGS_DIR + 'TP_percent_change'+ img)

    row1 = np.concatenate((img1, img2), axis=1)
    row2 = np.concatenate((img3, img4), axis=1)
    new_image = np.concatenate((row1, row2))

    matplotlib.image.imsave(IMGS_DIR + 'new'+img, new_image)






