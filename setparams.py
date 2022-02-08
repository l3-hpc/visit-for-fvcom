#File setparams.py
#Set the plot paramters
import sys

#-------- User Modified Section ------
# How many mi files are available?
# Change this to look at the path and calculate
NUM_MI_FILES = 13

# Just plot the first timestep of every mi file?
# If not, it will do every single timestep of every file
do_first_in_file = 1

#----  Which plot(s)?
## 3D pseudocolor plot
do_3Dplot = 1
## 2D pseudocolor slice
do_2Dslice = 1
## 2D transect
do_2Dtransect = 1
## Error check: Pick at least 1
if (do_3Dplot+do_2Dslice+do_2Dtransect) < 1:
    sys.exit("Pick at least 1 plot in setparams.py.\n")

#----  Pick points for transect
## If you won't do a transect, just ignore - it won't try to use the values
FROM_X = 561848.5
FROM_Y = 4756940.5
TO_X = 548466.63
TO_Y = 4793653.0

#--- set min/max for colormap
## For both TP_EPA and TP_Mark
MIN_TP = 0.00
MAX_TP = 0.02
## Difference colormap
MIN_TP_diff = -0.002
MAX_TP_diff = 0.002
## Percent change colormap
MIN_TP_PERCENT_CHANGE = -30
MAX_TP_PERCENT_CHANGE = 30

#--  Titles
TITLE_TP_EPA = "TP_EPA"
TITLE_TP_Mark = "TP_Mark"
TITLE_TP_diff = "TP_diff"
TITLE_TP_percent_change = "TP_Change"
#--  UNITS
UNITS_TP_EPA = "(mg/L)"
UNITS_TP_Mark = "(mg/L)"
UNITS_TP_diff = "(mg/L)"
UNITS_TP_percent_change = "(%)"


#----- Do not modify ------------
## number of mi_ files
## todo:  set according to what is in the directory
def set_NUM_MI_FILES():
    return NUM_MI_FILES

# Just plot the first timestep of every mi file?
# If not, it will do every single timestep of every file
def set_do_first_in_file():
    return do_first_in_file

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
## for both TP_EPA and TP_Mark
### TP colormap
def set_MIN_TP():
    return MIN_TP 
def set_MAX_TP():
    return MAX_TP 
### TP difference colormap
def set_MIN_TP_diff():
    return MIN_TP_diff
def set_MAX_TP_diff():
    return MAX_TP_diff
### TP percent change colormap
def set_MIN_TP_PERCENT_CHANGE():
    return MIN_TP_PERCENT_CHANGE
def set_MAX_TP_PERCENT_CHANGE():
    return MAX_TP_PERCENT_CHANGE

## set titles
### TP
def set_TITLE_TP_EPA():
    return TITLE_TP_EPA 
def set_TITLE_TP_Mark():
    return TITLE_TP_Mark
def set_TITLE_TP_diff():
    return TITLE_TP_diff
def set_TITLE_TP_percent_change():
    return TITLE_TP_percent_change

## set titles
### TP
def set_UNITS_TP_EPA():
    return UNITS_TP_EPA
def set_UNITS_TP_Mark():
    return UNITS_TP_Mark
def set_UNITS_TP_diff():
    return UNITS_TP_diff
def set_UNITS_TP_percent_change():
    return UNITS_TP_percent_change

