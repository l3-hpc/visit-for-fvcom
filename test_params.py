#PEP-8 style guide says each line should be 79 characters or less.............|
#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

#For exit command
import sys 

#To calculate normal vector for defining transect
#import numpy as np

#This is user defined setpaths.py in the current working directory
import setpaths
#This defines the plot parameters
import setparams


def test_param(name_of_param,the_param):
    output_test = name_of_param + " is " + str(the_param) + " and type is " + str(type(the_param))
    return output_test 

# Set the run name to label the images
RUN_NAME = setparams.set_RUN_NAME()

# Calls setpaths.py to define where the files are located
base_EPA_database = setpaths.set_EPA_path()

# If you will compare 2 data sets
do_compare = setparams.set_do_compare()

#Will you compare against Mark's data, with NDZP?
base_COMPARE_database = setpaths.set_COMPARE_path()
base_conn_string = setpaths.set_conn_string()

#for testing, always to that
do_MDR = setparams.set_do_MDR()

#Calls setpaths.py to define where the images are located
IMGS_DIR = setpaths.set_image_path()

#How many mi files are available?
#Change this to look at the path and calculate
NUM_MI_FILES = setparams.set_NUM_MI_FILES()

#For interactive...not used in plot_any
MI_ID_INIT = setparams.set_MI_ID_INIT()

# Just plot the first timestep of every mi file?
# If not, it will do every single timestep of every file
do_first_in_file = setparams.set_do_first_in_file()

#Which plots to do
do_3Dplot = setparams.set_do3Dplot()
do_2Dslice = setparams.set_do2Dslice()
do_2Dtransect = setparams.set_do2Dtransect()

#Add mesh?
add_mesh = True

#Print without Annotation
remove_annotation = setparams.set_remove_annotation()

#set min/max for colormap
#For both TP_EPA and TP_COMPARE
MIN_TP = setparams.set_MIN_TP()
MAX_TP = setparams.set_MAX_TP()
#Title
TITLE_TP_EPA = setparams.set_TITLE_TP_EPA()
#UNITS
UNITS_TP_EPA = setparams.set_UNITS_TP_EPA()

# testing, always do...if(do_compare):
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

#How many layers for pseudocolor
layers = setparams.set_which_layers()

#Do you want to not print out every timestep?  Skip how many?
#Put '1' to do every timestep
skip = setparams.set_skip()

#For transects
# testing, always do...if (do_2Dtransect):
FROM_X = setparams.set_FROM_X() 
FROM_Y = setparams.set_FROM_Y()
TO_X = setparams.set_TO_X()
TO_Y = setparams.set_TO_Y()

#print(test_param("",))
print(test_param("RUN_NAME",RUN_NAME ))
print(test_param("NUM_MI_FILES",NUM_MI_FILES))
print(test_param("MI_ID_INIT",MI_ID_INIT))
print(test_param("do_first_in_file",do_first_in_file))
print(test_param("do_compare",do_compare))
print(test_param("do_MDR",do_MDR))
print(test_param("do_3Dplot",do_3Dplot))
print(test_param("do_2Dslice",do_2Dslice))
print(test_param("do_2Dtransect",do_2Dtransect))
print(test_param("FROM_X",FROM_X))
print(test_param("FROM_Y",FROM_Y))
print(test_param("TO_X",TO_X))
print(test_param("TO_Y",TO_Y))
print(test_param("MIN_TP",MIN_TP))
print(test_param("MAX_TP",MAX_TP))
print(test_param("TITLE_TP_EPA",TITLE_TP_EPA))
print(test_param("UNITS_TP_EPA",UNITS_TP_EPA))
print(test_param("MIN_TP_DIFF",MIN_TP_DIFF))
print(test_param("MAX_TP_DIFF",MAX_TP_DIFF))
print(test_param("TITLE_TP_COMPARE",TITLE_TP_COMPARE))
print(test_param("TITLE_TP_DIFF",TITLE_TP_DIFF))
print(test_param("TITLE_TP_PERCENT_CHANGE",TITLE_TP_PERCENT_CHANGE))
print(test_param("UNITS_TP_COMPARE",UNITS_TP_COMPARE))
print(test_param("UNITS_TP_DIFF",UNITS_TP_DIFF))
print(test_param("UNITS_TP_PERCENT_CHANGE",UNITS_TP_PERCENT_CHANGE))
print(test_param("base_COMPARE_database",base_COMPARE_database))
print(test_param("base_conn_string",base_conn_string))
print(test_param("layers",layers))
print(test_param("skip",skip))
print(test_param("remove_annotation",remove_annotation))
#print(test_param("",))
#print(test_param("",))
#print(test_param("",))
#print(test_param("",))
#print(test_param("",))
#print(test_param("",))
#print(test_param("",))
#print(test_param("",))
#print(test_param("",))
#print(test_param("",))
