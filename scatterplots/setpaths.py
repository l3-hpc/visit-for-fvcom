#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os
import sys

#The directory where the mi_XXXX.nc files are located.  The slash at the end of the directory name is required.
EPA_directory = "/Users/lllowe/R_apps/LM_data/epa_2015/"
#The directory to write images to.  The slash at the end of the directory name is required.
IMGS_DIR = "/Users/lllowe/Transparent/Images-2015/Layer=1/"
#Is this an EPA run or a NOAA (Mark's) run
WHICH_DATA = "EPA"
#Which year is this data from, 2010 or 2015?
WHICH_YEAR = "2015"
# Name of run
# Choose a string - no spaces! - to identify the run.  
# It will be added to the name of the images.
# You can leave it empty by using two double quotes with no space.
RUN_NAME = "Run12"
## Which Layers: Goes from 1 to 19
which_layers = [1]

#Which mi file to start 
MI_START = 6
# How many mi files are available?
#This is the end of the range, not mi files in loop
#i.e. loop from MI_START to NUM_MI_FILES
NUM_MI_FILES = 13
# Just plot the first timestep of every mi file? 
# If not, it will do every single timestep of every file
do_first_in_file = False
##Do you want to *not* print every timestep?
# If skip=4, then you will print every 4th timestep
# Choose '1' to print every timestep
skip = 24

#--  Shouldn't need to modify past here ----------
#Sets the stations according to year
#Assumes you have this tarball...
# get working directory, it will not put a "/"
THIS_DIR = os.getcwd()

if(WHICH_YEAR == "2015"):
    STATIONS_PATH = THIS_DIR + "/stations/2015/"
elif(WHICH_YEAR=="2010"):
    STATIONS_PATH = THIS_DIR + "/stations/2010/"
else:
    print("Error, Date set to",WHICH_YEAR)
    sys.exit()    

if(WHICH_YEAR == "2015"):
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
elif(WHICH_YEAR == "2010"):
    measured_dates = [
    "03162010",
    "04052010",
    "04272010",
    "05032010",
    "05182010",
    "06042010",
    "06142010",
    "07012010",
    "07262010",
    "08032010",
    "08172010",
    "09092010",
    "09282010",
    "10182010",
    "11012010",
    "12032010"
    ]
else:
    print("Error, Date set to",WHICH_YEAR)
    sys.exit()

#This is probably 'mi_', but can be anything where the FVCOM output is for example
## [file_prefix_epa][4 integers padded by zeros].nc
file_prefix_epa = "mi_"
file_prefix_mark = "mi_"

#----- Do not modify unless developing code --------
#These are based on previous definitions, do not modify
base_EPA_database = EPA_directory + file_prefix_epa

#Check that all the directories exist
if not os.path.exists(EPA_directory):
    sys.exit("The directory " + EPA_directory + " does not exist.  Check definition of EPA_directory in setpaths.py. Exiting.")

#Create a directory for images if one doesn't exist.
#Note, existing files will be overwritten
if not os.path.exists(IMGS_DIR):
    os.makedirs(IMGS_DIR)

def set_EPA_path():
    return base_EPA_database

def set_image_path():
    return IMGS_DIR

def set_stations_path():
    return STATIONS_PATH

## Name of run
# Choose a string - no spaces! - to identify the run.  
# It will be added to the name of the images.
def set_RUN_NAME():
    return RUN_NAME

## number of mi_ files
## todo:  set according to what is in the directory
def set_MI_START():
    return MI_START

## number of mi_ files
## todo:  set according to what is in the directory
def set_NUM_MI_FILES():
    return NUM_MI_FILES

## for interactive 
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

## set var
def set_measured_dates():
    return measured_dates

## set layers
def set_which_layers():
    return which_layers

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
