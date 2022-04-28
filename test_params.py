#PEP-8 style guide says each line should be 79 characters or less.............|
#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

#For exit command
import sys 

#To calculate normal vector for defining transect
import numpy as np

#This is user defined setpaths.py in the current working directory
import setpaths
#This defines the plot parameters
import setparams

# Set the run name to label the images
RUN_NAME = setparams.set_RUN_NAME()

# Calls setpaths.py to define where the files are located
base_EPA_database = setpaths.set_EPA_path()

# If you will compare 2 data sets
do_compare = setparams.set_do_compare()
if(do_compare):
    base_COMPARE_database = setpaths.set_COMPARE_path()
    base_conn_string = setpaths.set_conn_string()
    #Will you compare against Mark's data, with NDZP?
    do_MDR = setparams.set_do_MDR()


#Calls setpaths.py to define where the images are located
IMGS_DIR = setpaths.set_image_path()

#How many mi files are available?
#Change this to look at the path and calculate
NUM_MI_FILES = setparams.set_NUM_MI_FILES()

# Just plot the first timestep of every mi file?
# If not, it will do every single timestep of every file
do_first_in_file = setparams.set_do_first_in_file()

#Which plots to do
do_3Dplot = setparams.set_do3Dplot()
do_2Dslice = setparams.set_do2Dslice()
do_2Dtransect = setparams.set_do2Dtransect()


#Add mesh?
add_mesh = True

#set min/max for colormap
#For both TP_EPA and TP_COMPARE
MIN_TP = setparams.set_MIN_TP()
MAX_TP = setparams.set_MAX_TP()
#Title
TITLE_TP_EPA = setparams.set_TITLE_TP_EPA()
#UNITS
UNITS_TP_EPA = setparams.set_UNITS_TP_EPA()

if(do_compare):
    MIN_TP_DIFF = setparams.set_MIN_TP_DIFF()
    MAX_TP_DIFF = setparams.set_MAX_TP_DIFF()
    #Percent change
    MIN_TP_PERCENT_CHANGE = setparams.set_MIN_TP_PERCENT_CHANGE()
    MAX_TP_PERCENT_CHANGE = setparams.set_MAX_TP_PERCENT_CHANGE()
    #Titles
    TITLE_TP_COMPARE = setparams.set_TITLE_TP_COMPARE()
    TITLE_TP_DIFF = setparams.set_TITLE_TP_DIFF()
    TITLE_TP_PERCENT_CHANGE = setparams.set_TITLE_TP_PERCENT_CHANGE()
    #UNITS
    UNITS_TP_COMPARE = setparams.set_UNITS_TP_COMPARE()
    UNITS_TP_DIFF = setparams.set_UNITS_TP_DIFF()
    UNITS_TP_PERCENT_CHANGE = setparams.set_UNITS_TP_PERCENT_CHANGE()


#For transects
if (do_2Dtransect):
    FROM_X = setparams.set_FROM_X() 
    FROM_Y = setparams.set_FROM_Y()
    TO_X = setparams.set_TO_X()
    TO_Y = setparams.set_TO_Y()

print("do_compare")
print(do_compare)
print(type(do_compare))

