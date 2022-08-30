#Python style, PEP 8
#https://www.python.org/dev/peps/pep-0008/

#File setparams.py
#Set the plot paramters
import sys

#-------- User Modified Section ------
#which variable to plot
#which_vars = ["DOC","DIA","GRE","ZOO","LOC","ROC","SRP","DOP","LOP","ROP","NH4","NO3","DON","LON","RON","SA","SU","DO2","TR"]

# Name of run
# Choose a string - no spaces! - to identify the run.  
# It will be added to the name of the images.
# You can leave it empty by using two double quotes with no space.
RUN_NAME = "Run12"

# How many mi files are available?
#TODO: Change this to look at the path and calculate
NUM_MI_FILES = 13 

# For setting up an interactive session, which MI file to look at.
# This will be ignored in a regular batch run
MI_ID_INIT = 11 

##These are all 'True or False'
# Just plot the first timestep of every mi file? 
# If not, it will do every single timestep of every file
do_first_in_file = False 

##Do you want to *not* print every timestep?
# If skip=4, then you will print every 4th timestep
# Choose '1' to print every timestep
skip = 24 

measured_dates = [
"03242015",
"04012015",
"04062015",
"04142015",
"05112015",
"06012015",
"06022015",
"06152015",
"06292015",
"07012015",
"07172015",
"07182015",
"07212015",
"07222015",
"08032015",
"08052015",
"08182015",
"09012015",
"09022015",
"09212015",
"10052015",
"10062015",
"10222015",
"11032015",
"12072015"
]



# Remove annotation?
remove_annotation = False 

## Which Layers: Goes from 1 to 19
#TODO: put in error checking
which_layers = [1]

## --- End True/False statements


#--- Plot parameters
##---  If only doing 1 plot:
# Set min/max for colormap
# This will be used in comparison plots as well
#MIN_TP = 0.00007
#MAX_TP = 0.0001
#For skew

#WONT WORK RIGHT NOW (hardcoded
MIN_TP = 0.002
MAX_TP = 0.035

#Use skew colormap for regular (non 'diff') plots?
skew = True

##--  Titles
TITLE_TP_EPA = "" 
UNITS_TP_EPA = "" 


#----- Do not modify ------------

##--- Error checking


## Name of run
# Choose a string - no spaces! - to identify the run.  
# It will be added to the name of the images.
def set_RUN_NAME(): 
    return RUN_NAME

## number of mi_ files
## todo:  set according to what is in the directory
def set_NUM_MI_FILES():
    return NUM_MI_FILES

## number of mi_ files
## todo:  set according to what is in the directory
def set_MI_ID_INIT():
    return MI_ID_INIT

# Just plot the first timestep of every mi file?
# If not, it will do every single timestep of every file
def set_do_first_in_file():
    return do_first_in_file

##Do you want to *not* print every timestep?
# If skip=4, then you will print every 4th timestep
# Choose '1' to print every timestep
def set_skip():
    return skip

## set min/max for colormap
### TP colormap
def set_MIN_TP():
    return MIN_TP 
def set_MAX_TP():
    return MAX_TP 
### Use Skew colormap for TP
def set_skew():
    return skew

## set titles
### TP
def set_TITLE_TP_EPA():
    return TITLE_TP_EPA 

## set titles
### TP
def set_UNITS_TP_EPA():
    return UNITS_TP_EPA

## set var
#def set_which_vars():
#    return which_vars 

def set_measured_dates():
    return measured_dates 


## set layers
def set_which_layers():
    return which_layers
## Annotation
def set_remove_annotation():
    return remove_annotation 
