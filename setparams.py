#Python style, PEP 8
#https://www.python.org/dev/peps/pep-0008/

#File setparams.py
#Set the plot paramters
import sys

#-------- User Modified Section ------
# Name of run
# Choose a string - no spaces! - to identify the run.  
# It will be added to the name of the images.
# You can leave it empty by using two double quotes with no space.
RUN_NAME = "TPSOvsNPZM2005GrandTransect"

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
skip = 1

# Are you comparing two runs? 
do_compare =  True 

# Is the comparison dataset from Mark
# If so, TP will be defined in terms of NDZP
do_MDR = True 

#--- Which plot(s)?
## 3D pseudocolor plot
do_3Dplot = True  
## 2D pseudocolor slice
do_2Dslice = False 
## 2D transect
do_2Dtransect = True

# Remove annotation?
remove_annotation = False 

## Which Layers: Goes from 1 to 19
#TODO: put in error checking
which_layers = [1,19]

## --- End True/False statements


#--- Pick points for transect
## If you won't do a transect, just ignore - it won't try to use the values
FROM_X = 560998.31
FROM_Y = 4767358.50
TO_X = 539195.69
TO_Y = 4765827.50

#--- Plot parameters
##---  If only doing 1 plot:
# Set min/max for colormap
# This will be used in comparison plots as well
MIN_TP = 0.002
MAX_TP = 0.01
#For skew
#MIN_TP = 0.001
#MAX_TP = 0.1

#Use skew colormap for regular (non 'diff') plots?
skew = True

##--  Titles
TITLE_TP_EPA = "TP_EPA"
UNITS_TP_EPA = "(mg/L)"
##--- If doing comparison plots 
## If you won't do a comparison, just ignore - it won't try to use the values
##-- Set min/max for colormaps
## Difference colormap
MIN_TP_DIFF = -0.002
MAX_TP_DIFF = 0.002
## Percent change colormap
MIN_TP_PERCENT_CHANGE = -20
MAX_TP_PERCENT_CHANGE = 20
##-- Titles
TITLE_TP_COMPARE = "TP_MARK"
TITLE_TP_DIFF = "TP_diff"
TITLE_TP_PERCENT_CHANGE = "TP_Change"
##-- UNITS
UNITS_TP_COMPARE = "(mg/L)"
UNITS_TP_DIFF = "(mg/L)"
UNITS_TP_PERCENT_CHANGE = "(%)"


#----- Do not modify ------------

##--- Error checking

## Plot types: Pick at least 1
if (do_3Dplot+do_2Dslice+do_2Dtransect) < 1:
    sys.exit("Pick at least 1 plot in setparams.py.\n")


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

# Are you comparing two runs? 
def set_do_compare():
    return do_compare

# Is the comparison dataset from Mark
# If so, TP will be defined in terms of NDZP
def set_do_MDR():
    return do_MDR

## Set which plot types using flags (0 or 1, do them or not)
def set_do3Dplot():
    return do_3Dplot
def set_do2Dslice():
    return do_2Dslice
def set_do2Dtransect():
    return do_2Dtransect

#----  Set points for transect
def set_FROM_X():
    return FROM_X
def set_FROM_Y():
    return FROM_Y
def set_TO_X():
    return TO_X
def set_TO_Y():
    return TO_Y

## set min/max for colormap
## for both TP_EPA and TP_COMPARE
### TP colormap
def set_MIN_TP():
    return MIN_TP 
def set_MAX_TP():
    return MAX_TP 
### Use Skew colormap for TP
def set_skew():
    return skew

### TP difference colormap
def set_MIN_TP_DIFF():
    return MIN_TP_DIFF
def set_MAX_TP_DIFF():
    return MAX_TP_DIFF
### TP percent change colormap
def set_MIN_TP_PERCENT_CHANGE():
    return MIN_TP_PERCENT_CHANGE
def set_MAX_TP_PERCENT_CHANGE():
    return MAX_TP_PERCENT_CHANGE

## set titles
### TP
def set_TITLE_TP_EPA():
    return TITLE_TP_EPA 
def set_TITLE_TP_COMPARE():
    return TITLE_TP_COMPARE
def set_TITLE_TP_DIFF():
    return TITLE_TP_DIFF
def set_TITLE_TP_PERCENT_CHANGE():
    return TITLE_TP_PERCENT_CHANGE

## set titles
### TP
def set_UNITS_TP_EPA():
    return UNITS_TP_EPA
def set_UNITS_TP_COMPARE():
    return UNITS_TP_COMPARE
def set_UNITS_TP_DIFF():
    return UNITS_TP_DIFF
def set_UNITS_TP_PERCENT_CHANGE():
    return UNITS_TP_PERCENT_CHANGE

## set layers
def set_which_layers():
    return which_layers
## Annotation
def set_remove_annotation():
    return remove_annotation 
