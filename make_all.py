import sys

#import custom paths
Source("setpaths.py")

#set min/max for colormap
MIN_TP_PERCENT_CHANGE = -10
MAX_TP_PERCENT_CHANGE = 10 

###Do not modify from here####################
# line 42: start time of simulation needs to be changed accordingly.
import datetime
import calendar

#Define start date
#time:units = "days since 1858-11-17 00:00:00" ;
#       time:format = "modified julian day (MJD)" ;
t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
slider = CreateAnnotationObject("TimeSlider")
slider.height = 0.07
slider.position = (0.03, 0.93)

##Disable Pipeline Caching to decrease memory consumption
SetPipelineCachingMode(0) # Disable caching

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

#Add the plots
AddPlot("Pseudocolor", "TP_percent_change", 1, 1)
DrawPlots()
SetActivePlots(0)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.minFlag = 1
PseudocolorAtts.min = MIN_TP_PERCENT_CHANGE
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = MAX_TP_PERCENT_CHANGE 
PseudocolorAtts.colorTableName = "caleblack"
SetPlotOptions(PseudocolorAtts)

AnnotationAtts = AnnotationAttributes()
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.databaseInfoFlag = 0
SetAnnotationAttributes(AnnotationAtts)

SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = IMGS_DIR 
SaveWindowAtts.fileName = IMGS_NAME 
SaveWindowAtts.family = 1
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
SetSaveWindowAttributes(SaveWindowAtts)

m = GetMetaData(EPA_database)
for state in range(TimeSliderGetNStates()):
  SetTimeSliderState(state)
  tcur = m.times[state]*86400.  + t_start
  ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%Y-%m-%d %H:%M:%S')
  timestamp = "Time: " + ts + " GMT"
  slider.text =  timestamp
  SaveWindow()

sys.exit()
