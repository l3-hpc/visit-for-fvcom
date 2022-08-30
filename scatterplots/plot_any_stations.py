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

# Do you want to remove annotations?
remove_annotation = setparams.set_remove_annotation()

#Define where the images should be printed out
#If the images exist already, they will be overwritten
IMGS_DIR = setpaths.set_image_path()

#How many mi files are available?
#TODO Change this to look at the path and calculate
NUM_MI_FILES = setparams.set_NUM_MI_FILES()

STATIONS_DIR = setpaths.set_stations_path()
SHAPEFILES_DIR = setpaths.set_shapefiles_path()

# Just plot the first timestep of every mi file?
# If not, it will do every single timestep of every file
do_first_in_file = setparams.set_do_first_in_file()
#Instead of doing every single timestep of every file,
# skip some of them
skip_states = setparams.set_skip()

#Which layers to plot
layers = setparams.set_which_layers()

#Which dates have measurements
measured_dates = setparams.set_measured_dates()

#Set min/max for colormap
#For both TP_EPA and TP_COMPARE
MIN_TP = setparams.set_MIN_TP()
MAX_TP = setparams.set_MAX_TP()
#Set a skew colormap?
SKEW = setparams.set_skew()
#Variable name and units for annotating the main dataset
#Will also be used for the comparison dataset
TITLE_TP_EPA = setparams.set_TITLE_TP_EPA()
UNITS_TP_EPA = setparams.set_UNITS_TP_EPA()

#This creates a bird's eye view of the plot.  It is called 3D, but now
# since we've added 'Layer', it is not quite 3D...
def create_pseudocolor_3Dplot(TITLE,UNITS,PLOT_VAR,MIN,MAX,FILE_TS,LAYER,SKEW,DOTS,SDATE):
    #Variable name and units, with option to leave blank 
    if(remove_annotation):
        title.text = ""
        text2D_units.text =  ""
        text2D_timestamp.text =  ""
    else:
        title.text = TITLE + " Layer = " +str(LAYER)
        text2D_units.text = UNITS
        text2D_timestamp.text = timestamp

    #Add pseudocolor plot and set attributes
    AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
    SetActivePlots(0)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.colorTableName = "turbo"
    if(SKEW):
        PseudocolorAtts.scaling = PseudocolorAtts.Skew  # Linear, Log, Skew
        PseudocolorAtts.skewFactor = 0.1 
        PseudocolorAtts.min = 0.002      
        PseudocolorAtts.max = 0.02
    else:
        PseudocolorAtts.scaling = PseudocolorAtts.Linear
        PseudocolorAtts.min = MIN
        PseudocolorAtts.max = MAX
        PseudocolorAtts.colorTableName = "caleblack"
    SetPlotOptions(PseudocolorAtts)
    #Comment out since showing triangles overwhelms the plot
    # if(add_mesh):
    #     AddPlot("Mesh", "SigmaLayer_Mesh", 1, 1)
    DrawPlots()

    #Format the legend
    plotName = GetPlotList().GetPlots(0).plotName
    legend = GetAnnotationObject(plotName)
    legend.managePosition = 0
    legend.position = (0.7,0.65)
    legend.drawTitle=0
    legend.drawMinMax = 0
    legend.numberFormat = "%1.3f"

    #Begin defining annotation properties (attributes)
    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #get rid of x-y-x axis thing in the bottom left
    AnnotationAtts.axes3D.triadFlag = 0
    AnnotationAtts.axes2D.visible = 1
    AnnotationAtts.axes2D.xAxis.title.visible = 1
    #Turn off annotations to make plots less busy when
    # placed on the same page
    if(remove_annotation):
       AnnotationAtts.legendInfoFlag = 0
       AnnotationAtts.timeInfoFlag = 0
       AnnotationAtts.axes2D.visible = 0
       AnnotationAtts.axes2D.xAxis.title.visible = 0
       AnnotationAtts.axes2D.yAxis.title.visible = 0
       AnnotationAtts.axes2D.xAxis.label.visible = 0
       AnnotationAtts.axes2D.yAxis.label.visible = 0
       AnnotationAtts.axes3D.visible = 0
    #Black background
    AnnotationAtts.backgroundColor = (0, 0, 0, 255)
    AnnotationAtts.foregroundColor = (255, 255, 255, 255)
    AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
    #Officially set attributes
    SetAnnotationAttributes(AnnotationAtts)
    #End changes to annotation

    #Choose which layer will be shown
    #- First, turn all of them off
    TurnMaterialsOff()
    #Names of layers are actually a string...
    # might have to confirm this always works 
    layer_string = "Layer " + str(LAYER)
    TurnMaterialsOn(layer_string)
    DrawPlots()
    #End layer choosing


    ##Add measured data points
    #set file open defaults
    plainTextOpenOptions = GetDefaultFileOpenOptions("PlainText")
    plainTextOpenOptions['First row has variable names'] = 1
    plainTextOpenOptions['Lines to skip at beginning of file'] = 0
    plainTextOpenOptions['Column for X coordinate (or -1 for none)'] = 0
    plainTextOpenOptions['Column for Y coordinate (or -1 for none)'] = 1
    plainTextOpenOptions['Column for Z coordinate (or -1 for none)'] = 2
    SetDefaultFileOpenOptions("PlainText", plainTextOpenOptions)

    #open file, add plot
    #open file, add plot
    if(DOTS):
        CSMI_NAME = STATIONS_DIR + "csmi_date_" + SDATE + ".txt"
        POT_NAME = STATIONS_DIR + "pot_date_" + SDATE + ".txt"
        with open(POT_NAME, 'r') as fp:
            numlines = len(fp.readlines())
        if numlines > 1:
            OpenDatabase(POT_NAME, 0)
            AddPlot("Scatter", "TP", 1, 1)
            ScatterAtts = ScatterAttributes()
            ScatterAtts.var1 = "X"
            ScatterAtts.var1Role = ScatterAtts.Coordinate0  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
            ScatterAtts.var1Scaling = ScatterAtts.Linear  # Linear, Log, Skew
            ScatterAtts.var2Role = ScatterAtts.Coordinate1  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
            ScatterAtts.var2 = "Y"
            ScatterAtts.var2Scaling = ScatterAtts.Linear  # Linear, Log, Skew
            ScatterAtts.var3Role = ScatterAtts.Coordinate2  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
            ScatterAtts.var3 = "Z"
            ScatterAtts.var4Role = ScatterAtts.Color  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
            ScatterAtts.var4 = "TP"
            ScatterAtts.var4MinFlag = 1
            ScatterAtts.var4MaxFlag = 1
            ScatterAtts.var4Min = 0.002
            ScatterAtts.var4Max = 0.02
            ScatterAtts.var4Scaling = ScatterAtts.Skew  # Linear, Log, Skew
            ScatterAtts.var4SkewFactor = 0.1
            ScatterAtts.pointSize = 900
            ScatterAtts.pointSizePixels = 1
            ScatterAtts.pointType = ScatterAtts.Icosahedron  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
            ScatterAtts.scaleCube = 0
            ScatterAtts.colorType = ScatterAtts.ColorByColorTable  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
            ScatterAtts.colorTableName = "turbo"
            ScatterAtts.invertColorTable = 0
            ScatterAtts.legendFlag = 0
            SetPlotOptions(ScatterAtts)
            DrawPlots()
        #open file, add plot
        #open file, add plot
        with open(CSMI_NAME, 'r') as fp:
            numlines = len(fp.readlines())
        if numlines > 1:
            OpenDatabase(CSMI_NAME, 0)
            AddPlot("Scatter", "TP", 1, 1)
            ScatterAtts = ScatterAttributes()
            ScatterAtts.var1 = "X"
            ScatterAtts.var1Role = ScatterAtts.Coordinate0  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
            ScatterAtts.var1Scaling = ScatterAtts.Linear  # Linear, Log, Skew
            ScatterAtts.var2Role = ScatterAtts.Coordinate1  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
            ScatterAtts.var2 = "Y"
            ScatterAtts.var2Scaling = ScatterAtts.Linear  # Linear, Log, Skew
            ScatterAtts.var3Role = ScatterAtts.Coordinate2  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
            ScatterAtts.var3 = "Z"
            ScatterAtts.var4Role = ScatterAtts.Color  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
            ScatterAtts.var4 = "TP"
            ScatterAtts.var4MinFlag = 1
            ScatterAtts.var4MaxFlag = 1
            ScatterAtts.var4Min = 0.002
            ScatterAtts.var4Max = 0.02
            ScatterAtts.var4Scaling = ScatterAtts.Skew  # Linear, Log, Skew
            ScatterAtts.var4SkewFactor = 0.1
            ScatterAtts.pointSize = 900
            ScatterAtts.pointSizePixels = 1
            ScatterAtts.pointType = ScatterAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
            ScatterAtts.scaleCube = 0
            ScatterAtts.colorType = ScatterAtts.ColorByColorTable  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
            ScatterAtts.colorTableName = "turbo"
            ScatterAtts.invertColorTable = 0
            ScatterAtts.legendFlag = 0
            SetPlotOptions(ScatterAtts)
            DrawPlots()

    
    #Zoom in to GR area
    # Begin spontaneous state
    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (0, 0, 1)
    View3DAtts.focus = (546981, 4.8567e+06, -135.085)
    View3DAtts.viewUp = (0, 1, 0)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 279685
    View3DAtts.nearPlane = -559370
    View3DAtts.farPlane = 559370
    View3DAtts.imagePan = (-0.00968456, 0.142186)
    View3DAtts.imageZoom = 11.3436
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (546981, 4.8567e+06, -135.085)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)
    # End spontaneous state
    
    #Save the image
    SaveWindowAtts.fileName = PLOT_VAR + "_LAYER=" + str(LAYER) + FILE_TS
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
   
    #Turn all the layers back on for next plots to work
    TurnMaterialsOn()
    #End create_3D...

    if(DOTS):
        with open(POT_NAME, 'r') as fp:
            numlines = len(fp.readlines())
        if numlines > 1:
            #Close stations file
            SetActivePlots(1)
            DeleteActivePlots()
            CloseDatabase(POT_NAME)
        with open(CSMI_NAME, 'r') as fp:
            numlines = len(fp.readlines())
        if numlines > 1:
            #Close stations file
            SetActivePlots(1)
            DeleteActivePlots()
            CloseDatabase(CSMI_NAME) 


###-- All of the above was just defining the 'functions' -------------
##    Below is the start of the loop that actually calls the functions

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
title.position = (0.045, 0.94)
title.height = 0.018
title.text = "" 
#Title text will be redefined for each plot
text2D_units = CreateAnnotationObject("Text2D")
text2D_units.position = (0.05, 0.90)
text2D_units.height = 0.015
text2D_units.text = ""

#Month-Day-Year Hour:Minute:Second 
text2D_timestamp = CreateAnnotationObject("Text2D")
text2D_timestamp.position = (0.45, 0.95)
text2D_timestamp.height = 0.015
text2D_timestamp.text = ""

##Disable Pipeline Caching to decrease memory consumption
SetPipelineCachingMode(0) # Disable caching

#DO LOOP 
#Python end range is not included:  this is loop from 1 to 13
#TODO...set range...how to do this if outputs don't line up?
for x in range(1,NUM_MI_FILES+1):
    mi_ID = x
    ##Lisa macOS paths, works to save 4 png files
    EPA_database = base_EPA_database + str(mi_ID).zfill(4) + ".nc"
    #The IMGS_NAME is set below
    #Now it is set to overwrite existing files

    #Open Databases - the second argument is optional with a default of zero 
    #Where zero = initial time
    OpenDatabase(EPA_database,0)
    #Script expects 'TP_EPA', even when not comparing it still needs to be defined
    DefineScalarExpression("TP_EPA", "TP")

    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = IMGS_DIR 
    #Sets the name below
    ###SaveWindowAtts.fileName = IMGS_NAME
    #Setting family to zero means it will overwrite existing files 
    SaveWindowAtts.family = 0
    #Set aspect ratio
    #SaveWindowAtts.resConstraint = 1 #NoConstraint
    #SaveWindowAtts.width = 700
    #SaveWindowAtts.height = 600
    ##Options are: BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, 
    ##  POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
    SaveWindowAtts.format = SaveWindowAtts.PNG
    SetSaveWindowAttributes(SaveWindowAtts)
    
    m = GetMetaData(EPA_database)
    totalstates = TimeSliderGetNStates()
    loopstates = int(totalstates/skip_states)
    istate = 0
    for state in range(loopstates):
        SetTimeSliderState(istate)
        tcur = m.times[istate]*86400.  + t_start
        ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%m-%d-%Y %H:%M:%S')
        FILE_TS = "_" + RUN_NAME + "." + datetime.datetime.utcfromtimestamp(tcur).strftime('%m-%d-%Y_%H-%M-%S')
#      timestamp = "Time: " + ts + " GMT"
        timestamp = ts + " "
        slider.text =  timestamp
        slider.visible=0
        ts_station = datetime.datetime.utcfromtimestamp(tcur).strftime('%m%d%Y')
        DOTS = False
        if(ts_station in measured_dates):
            DOTS = True    
        #def create_pseudocolor_3Dplot(TITLE,UNITS,PLOT_VAR,MIN,MAX,FILE_TS):
        for LAYER in layers:
            create_pseudocolor_3Dplot(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA", 
                MIN_TP,MAX_TP,FILE_TS,LAYER,SKEW,DOTS,ts_station)
            DeleteAllPlots()

#Comment this out when debugging if you want VisIt to leave the Window open
#      DeleteAllPlots()

#     Using this break command results in only creating a plot
#      with the first timestep of each mi_000X file
        if(do_first_in_file):
            break
        else:
            istate += skip_states    
    
    DeleteAllPlots()
    #If debugging, uncomment break
    #break
    #Clear the database, not to bog down memory
    ClearCacheForAllEngines()                                    

#ENDDO loop

#Comment this out to leave VisIT CLI open after script is complete
sys.exit()

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
