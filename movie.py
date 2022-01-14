#THIS DOES NOT WORK...

#TESTING random ideas on how to do this


#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys  #For the Source command"
import numpy
#
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

img = [
"TP_percent_change_01-01-2010_00-00-00.png",
"TP_percent_change_01-31-2010_00-00-00.png",
"TP_percent_change_03-02-2010_00-00-00.png",
"TP_percent_change_04-01-2010_00-00-00.png",
"TP_percent_change_05-01-2010_00-00-00.png",
"TP_percent_change_05-31-2010_00-00-00.png",
"TP_percent_change_06-30-2010_00-00-00.png",
"TP_percent_change_07-30-2010_00-00-00.png",
"TP_percent_change_08-29-2010_00-00-00.png",
"TP_percent_change_09-28-2010_00-00-00.png",
"TP_percent_change_10-28-2010_00-00-00.png",
"TP_percent_change_11-27-2010_00-00-00.png",
"TP_percent_change_12-27-2010_00-00-00.png"
]

frames = [] # for storing the generated images
fig = plt.figure()
for i in range(6):
    frames.append([plt.imshow(img[i],animated=True)])

ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True,
                                repeat_delay=1000)
ani.save('movie.mp4')
#plt.show()

#THIS DOESN'T WORK YET
