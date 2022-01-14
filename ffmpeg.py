#THIS DOES NOT WORK...

#TESTING random ideas on how to do this


#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys  #does exit command
from setpaths import set_paths  #we wrote python file setpaths.py 

#import custom paths
IMGS_DIR = set_paths("imagedir")

os.system("ffmpeg -r 5 -f image2 -s 1920x1080 -start_number 0 -i m10to10%04d.png -vframes 201 -vcodec libx264 -crf 25  -pix_fmt yuv420p m10to10_200.mp4")

#THIS is not even close to working, please ignore
