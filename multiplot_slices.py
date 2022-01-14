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
"_slice_01-01-2010_00-00-00.png",
"_slice_01-31-2010_00-00-00.png",
"_slice_03-02-2010_00-00-00.png",
"_slice_04-01-2010_00-00-00.png",
"_slice_05-01-2010_00-00-00.png",
"_slice_05-31-2010_00-00-00.png",
"_slice_06-30-2010_00-00-00.png",
"_slice_07-30-2010_00-00-00.png",
"_slice_08-29-2010_00-00-00.png",
"_slice_09-28-2010_00-00-00.png",
"_slice_10-28-2010_00-00-00.png",
"_slice_11-27-2010_00-00-00.png",
"_slice_12-27-2010_00-00-00.png"
]

for img in image_suffix:
    img1 = matplotlib.image.imread(IMGS_DIR + 'TP_EPA'+ img)
    img2 = matplotlib.image.imread(IMGS_DIR + 'TP_Mark'+ img)
    img3 = matplotlib.image.imread(IMGS_DIR + 'TP_diff'+ img)
    img4 = matplotlib.image.imread(IMGS_DIR + 'TP_percent_change'+ img)
    row1 = np.concatenate((img1, img2, img3, img4), axis=1)
    matplotlib.image.imsave(IMGS_DIR + 'new'+img, row1)
