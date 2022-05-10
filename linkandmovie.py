#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os
import sys  
#These are ours
import setpaths
import setparams

# Set the run name to label the images
RUN_NAME = setparams.set_RUN_NAME()
#print(RUN_NAME)

#Defines where the images are located
IMGS_DIR = setpaths.set_image_path()

## Create a dummy directory for sym-links
LINKS_DIR = IMGS_DIR + "SYMLINKS/"
if not os.path.exists(LINKS_DIR):
    os.makedirs(LINKS_DIR)

#Defines which plots are made 
do_3Dplot = setparams.set_do3Dplot()
do_2Dslice = setparams.set_do2Dslice()
do_2Dtransect = setparams.set_do2Dtransect()
layers = setparams.set_which_layers()

# Are you comparing two runs? 
do_compare =  True

#Create a list of plot titles
plotnames = []
if(do_3Dplot):
    for layer in layers:
        plotnames.append("TP_EPA_LAYER="+str(layer) + "_" + RUN_NAME)
        if(do_compare):
            plotnames.append("TP_COMPARE_LAYER="+str(layer) + "_" + RUN_NAME)
            plotnames.append("TP_DIFF_LAYER="+str(layer) + "_" + RUN_NAME)
            plotnames.append("TP_PERCENT_CHANGE_LAYER="+str(layer) + "_" + RUN_NAME)

if(do_2Dslice):
    plotnames.append("TP_EPA_slice_" + RUN_NAME)
    if(do_compare):
        plotnames.append("TP_COMPARE_slice_" + RUN_NAME)
        plotnames.append("TP_DIFF_slice_" + RUN_NAME)
        plotnames.append("TP_PERCENT_CHANGE_slice_" + RUN_NAME)


if(do_2Dtransect):
    plotnames.append("TP_EPA_transect_" + RUN_NAME)
    if(do_compare):
        plotnames.append("TP_COMPARE_transect_" + RUN_NAME)
        plotnames.append("TP_DIFF_transect_" + RUN_NAME)
        plotnames.append("TP_PERCENT_CHANGE_transect_" + RUN_NAME)


#Display the list of images in the IMGS_DIR directory in reverse time order and
# redirect the output to a text file
for pname in plotnames:
    print(pname)
    command_string = "ls -rt " + IMGS_DIR + " | grep " + pname + " > " + pname +".txt"
    #print(command_string)
    os.system(command_string)

#The ffmpeg expects a regular expression and a formatted number to make the movie.
#  This part of the code creates symbolic links to satisfy ffmpeg without changing
#   the filename or making a copy of the file.
#TODO:  check for and remove existing links
index = 0
for pname in plotnames:
    file_name = pname + ".txt"
    with open(file_name,'r') as data_file:
        for line in data_file:
            data = line.split('.')
            original_file = line.strip()
            linked_file = LINKS_DIR + data[0] + "." + str(index).zfill(4) + ".png"
            linking_string = "ln -s " + IMGS_DIR + original_file + " " + linked_file
            os.system(linking_string)
            #print(linking_string)
            index+=1
        numframes = index-1
        index = 0
        print(numframes) 
        #-r is frame rate, how many images per second.  Increase to make the movie run faster.
        ffmpeg_string = "ffmpeg -r 15 -f image2 -s 1920x1080 -start_number 0 -i " + LINKS_DIR + pname + ".%04d.png -vframes " + str(numframes) + " -vcodec libx264 -crf 25  -pix_fmt yuv420p " + IMGS_DIR + pname + ".mp4"
        print(ffmpeg_string)
        os.system(ffmpeg_string)
