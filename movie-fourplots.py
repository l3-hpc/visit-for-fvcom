#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os
import sys  
#These are ours
#import setpaths
#import setparams

ffmpeg_string = "ffmpeg -r 45 -f image2 -s 1920x1080 -start_number 0 -i /rsstu/users/l/lllowe/ord/JAMES-PRESENTATION/multi/TPSOvsNPZM2005GrandTransect.%04d.png -vframes 2191 -vcodec libx264 -crf 25  -pix_fmt yuv420p /rsstu/users/l/lllowe/ord/JAMES-PRESENTATION/multi/TPSOvsNPZM2005GrandTransect.mp4"
print(ffmpeg_string)
os.system(ffmpeg_string)

