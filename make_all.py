#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

#Note, this won't work for mi_subset yet

#Does the exit command
import sys


#save the session, make sure settings are same
##SaveSession("savethe.session")
RestoreSession("/rsstu/users/l/lllowe/ord/visit-for-fvcom/savethe.session",0)


#import custom paths
#The 'Source' didn't work in a regular python script, don't know if it is VisIt specific or Python 3 issue
Source("setpaths.py")

#How many mi files are available?
#Change this to look at the path and calculate
NUM_MI_FILES = 13

#set min/max for colormap
#For both TP_EPA and TP_Mark
MIN_TP = 0.00
MAX_TP = 0.02
#Difference
MIN_TP_diff = -0.002
MAX_TP_diff = 0.002
#Percent change
MIN_TP_PERCENT_CHANGE = -30
MAX_TP_PERCENT_CHANGE = 30
#Titles
TITLE_TP_EPA = "TP_EPA"
TITLE_TP_Mark = "TP_Mark"
TITLE_TP_diff = "TP_diff"
TITLE_TP_percent_change = "TP_Change"
#UNITS
UNITS_TP_EPA = "(mg/L)"
UNITS_TP_Mark = "(mg/L)"
UNITS_TP_diff = "(mg/L)"
UNITS_TP_percent_change = "(%)"

###Do not modify from here####################
# line 42: start time of simulation needs to be changed accordingly.
import datetime
import calendar

#Define start date
#time:units = "days since 1858-11-17 00:00:00" ;
#       time:format = "modified julian day (MJD)" ;
t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
slider = CreateAnnotationObject("TimeSlider")
slider.height = 0.05
slider.width = 0.3
slider.position = (0.6, 0.5)

#Set location of Title
#Title text will be redefined for each plot
title = CreateAnnotationObject("Text2D")
title.position = (0.04, 0.96)
title.height = 0.018
title.text = "UNDEFINED" 
#Title text will be redefined for each plot
text2D_units = CreateAnnotationObject("Text2D")
text2D_units.position = (0.05, 0.90)
text2D_units.height = 0.015
text2D_units.text = "UNDEFINED"

#Month, Day, Year part
text2D_timestamp = CreateAnnotationObject("Text2D")
text2D_timestamp.position = (0.45, 0.96)
text2D_timestamp.height = 0.02
text2D_timestamp.text = "UNDEFINED"

#GMT part
#text2D_GMT = CreateAnnotationObject("Text2D")
#text2D_GMT.position = (0.04, 0.5)
#text2D_GMT.height = 0.02
#text2D_GMT.text = "UNDEFINED"


##Disable Pipeline Caching to decrease memory consumption
SetPipelineCachingMode(0) # Disable caching

#DO LOOP 
#Python end range is not included:  this is loop from 1 to 13
#TODO...set range...how to do this if outputs don't line up?
for x in range(1,NUM_MI_FILES+1):
    mi_ID = x
    ##Lisa macOS paths, works to save 4 png files
    EPA_database = base_EPA_database + str(mi_ID).zfill(4) + ".nc"
    MARK_database = base_MARK_database + str(mi_ID).zfill(4) + ".nc"
#TODO check if it works on Windows
    conn_string = base_conn_string  + str(mi_ID).zfill(4) + ".nc[0]id:TP>, <SigmaLayer_Mesh>)"
    #The IMGS_NAME is set below
    #Now it is set to overwrite existing files
    #IMGS_NAME = base_IMGS_NAME + str(mi_ID).zfill(4) + "."


    #Open Databases - the second argument is optional with a default of zero (initial time)
    OpenDatabase(EPA_database,0)
    OpenDatabase(MARK_database,0)

    #CreateDatabaseCorrelation("name",(db1,db2),X), here X=2 is a time correlation
    CreateDatabaseCorrelation("Correlation01",(EPA_database,MARK_database),2)

    #Use conn_cmfe function to put EPA's TP variable onto Mark's grid and call it "TP_EPA"
    DefineScalarExpression("TP_EPA",conn_string)

    #Define additional variables
    DefineScalarExpression("TP_Mark", "PO4 + 0.016*(Detritus+Phytoplankton+Zooplankton)")
    DefineScalarExpression("TP_diff", "TP_Mark - TP_EPA")
    DefineScalarExpression("TP_percent_change", "(TP_EPA - TP_Mark)/abs(TP_Mark)*100")

    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #get rid of x-y-x axis thing in the bottom left
    AnnotationAtts.axes3D.triadFlag = 0
    SetAnnotationAttributes(AnnotationAtts)

#    Get rid of TP title and units from Legend
    #GetAnnotationObjectNames
    #legend = GetAnnotationObjectNames(a[4])
    #legend.drawTitle=0

    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = IMGS_DIR 
    #Sets the name below
    ###SaveWindowAtts.fileName = IMGS_NAME
    #Setting family to zero means it will overwrite existing files 
    SaveWindowAtts.family = 0
    #Set aspect ratio
    SaveWindowAtts.resConstraint = 1 #NoConstraint
    #SaveWindowAtts.width = 700
    #SaveWindowAtts.height = 600
    SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
    SetSaveWindowAttributes(SaveWindowAtts)
    
    m = GetMetaData(EPA_database)
    for state in range(TimeSliderGetNStates()):
      SetTimeSliderState(state)
      tcur = m.times[state]*86400.  + t_start
      ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%m-%d-%Y %H:%M:%S')
      FILE_TS = datetime.datetime.utcfromtimestamp(tcur).strftime('%m-%d-%Y_%H-%M-%S')
#      timestamp = "Time: " + ts + " GMT"
      timestamp = ts + " "
      slider.text =  timestamp
      slider.visible=0
      title.text = TITLE_TP_percent_change
      text2D_units.text = UNITS_TP_percent_change
      text2D_timestamp.text = timestamp 
      AddPlot("Pseudocolor", "TP_percent_change", 1, 1)
      a = GetAnnotationObjectNames()
      legend = GetAnnotationObject(a[4])
      legend.drawTitle=0
      legend.managePosition=0
      legend.position = (0.055,0.85)
      legend.yScale = 1.0

      DrawPlots()
      SetActivePlots(0)
      PseudocolorAtts = PseudocolorAttributes()
      PseudocolorAtts.minFlag = 1
      PseudocolorAtts.maxFlag = 1
      PseudocolorAtts.colorTableName = "caleblack"
      PseudocolorAtts.min = MIN_TP_PERCENT_CHANGE
      PseudocolorAtts.max = MAX_TP_PERCENT_CHANGE
      SetPlotOptions(PseudocolorAtts)
      SaveWindowAtts.fileName = "TP_percent_change_" + FILE_TS
      SetSaveWindowAttributes(SaveWindowAtts)
      SaveWindow()

      DeleteAllPlots()
      slider.visible=0
      title.text = TITLE_TP_diff
      text2D_units.text = UNITS_TP_diff
      text2D_timestamp.text = timestamp 
      AddPlot("Pseudocolor", "TP_diff", 1, 1)
      a = GetAnnotationObjectNames()
      legend = GetAnnotationObject(a[4])
      legend.drawTitle=0
      legend.managePosition=0
      legend.position = (0.055,0.85)
      legend.yScale = 1

      DrawPlots()
      SetActivePlots(0)
      PseudocolorAtts = PseudocolorAttributes()
      PseudocolorAtts.minFlag = 1
      PseudocolorAtts.maxFlag = 1
      PseudocolorAtts.min = MIN_TP_diff
      PseudocolorAtts.max = MAX_TP_diff
      SetPlotOptions(PseudocolorAtts)
      SaveWindowAtts.fileName = "TP_diff_" + FILE_TS
      SetSaveWindowAttributes(SaveWindowAtts)
      SaveWindow()

      DeleteAllPlots()
      slider.visible=0
      title.text = TITLE_TP_EPA
      text2D_units.text = UNITS_TP_EPA
      text2D_timestamp.text = timestamp
      AddPlot("Pseudocolor", "TP_EPA", 1, 1)
      a = GetAnnotationObjectNames()
      legend = GetAnnotationObject(a[4])
      legend.drawTitle=0
      legend.managePosition=0
      legend.position = (0.055,0.85)
      legend.yScale = 1

      DrawPlots()
      SetActivePlots(0)
      PseudocolorAtts = PseudocolorAttributes()
      PseudocolorAtts.minFlag = 1
      PseudocolorAtts.maxFlag = 1
      PseudocolorAtts.min = MIN_TP
      PseudocolorAtts.max = MAX_TP
      SetPlotOptions(PseudocolorAtts)
      SaveWindowAtts.fileName = "TP_EPA_" + FILE_TS
      SetSaveWindowAttributes(SaveWindowAtts)
      SaveWindow()

      DeleteAllPlots()
      slider.visible=0
      title.text = TITLE_TP_Mark
      text2D_units.text = UNITS_TP_Mark
      text2D_timestamp.text = timestamp 
      AddPlot("Pseudocolor", "TP_Mark", 1, 1)
      a = GetAnnotationObjectNames()
      legend = GetAnnotationObject(a[4])
      legend.drawTitle=0
      legend.managePosition=0
      legend.position = (0.055,0.85)
      legend.yScale = 1

      DrawPlots()
      SetActivePlots(0)
      PseudocolorAtts = PseudocolorAttributes()
      PseudocolorAtts.minFlag = 1
      PseudocolorAtts.maxFlag = 1
      PseudocolorAtts.min = MIN_TP
      PseudocolorAtts.max = MAX_TP
      SetPlotOptions(PseudocolorAtts)
      SaveWindowAtts.fileName = "TP_Mark_" + FILE_TS
      SetSaveWindowAttributes(SaveWindowAtts)
      SaveWindow()
#     Using this break command results in only creating a plot
#      with the first timestep of each mi_000X file
      break
    
    #DeleteAllPlots()
    #If debugging, uncomment break
    break
    #Clear the database, not to bog down memory
    #ClearCacheForAllEngines()                                    

#ENDDO loop

#sys.exit()

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
