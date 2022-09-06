#PEP-8 style guide says each line should be 79 characters or less.............|
#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

#For exit command
import sys 

#To calculate normal vector for defining transect
import numpy as np

#sys.path.append("/Users/lisalowe/visit-for-fvcom/scatterplots")

#This is user defined setpaths.py in the current working directory
import setpaths

# Set the run name to label the images
RUN_NAME = setpaths.set_RUN_NAME()

# Calls setpaths.py to define where the files are located
base_EPA_database = setpaths.set_EPA_path()
#Define where the images should be printed out
#If the images exist already, they will be overwritten
IMGS_DIR = setpaths.set_image_path()
#Directory with measured data
STATIONS_DIR = setpaths.set_stations_path()

#How many mi files are available?
#TODO Change this to look at the path and calculate
NUM_MI_FILES = setpaths.set_NUM_MI_FILES()
MI_START = setpaths.set_MI_START()

# Just plot the first timestep of every mi file?
# If not, it will do every single timestep of every file
do_first_in_file = setpaths.set_do_first_in_file()
#Instead of doing every single timestep of every file,
# skip some of them
skip_states = setpaths.set_skip()

#Which layers to plot
layers = setpaths.set_which_layers()

#Which dates have measurements
measured_dates = setpaths.set_measured_dates()

#This creates a bird's eye view of the plot.  It is called 3D, but now
# since we've added 'Layer', it is not quite 3D...
def create_pseudocolor_3Dplot(PLOT_VAR,FILE_TS,LAYER,DOTS,SDATE):
    remove_annotation = True
    if(remove_annotation):
        text2D_timestamp.text =  ""

    #Add pseudocolor plot and set attributes
    AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
    SetActivePlots(0)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.colorTableName = "turbo"
    PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
    PseudocolorAtts.min = 0.00      
    PseudocolorAtts.max = 0.02
    SetPlotOptions(PseudocolorAtts)
    DrawPlots()

    #Begin defining annotation properties (attributes)
    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #get rid of x-y-x axis thing in the bottom left
    AnnotationAtts.axes3D.triadFlag = 0
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

    #Format the legend
    plotName = GetPlotList().GetPlots(0).plotName
    legend = GetAnnotationObject(plotName)
#turn off legend
    legend.active = 0
    legend.managePosition = 0
    legend.position = (0.8, 0.7)
    legend.xScale = 1
    legend.yScale = 1
    legend.textColor = (255, 255, 255, 255)
    legend.useForegroundForTextColor = 1
    legend.drawBoundingBox = 0
    legend.boundingBoxColor = (0, 0, 0, 50)
    legend.numberFormat = "%1.2f"
    legend.fontHeight = 0.015
    legend.drawTitle = 0
    legend.drawMinMax = 0
    legend.orientation = legend.VerticalRight  # VerticalRight, VerticalLeft, HorizontalTop, HorizontalBottom
    legend.controlTicks = 1
    legend.numTicks = 5
    legend.minMaxInclusive = 1
    legend.drawLabels = legend.Labels

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

    #Add 'bathymetry', which is model depth contours
    AddPlot("Contour", "h", 1, 1)
    SetActivePlots(2)
    ContourAtts = ContourAttributes()
    ContourAtts.colorType = ContourAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    ContourAtts.legendFlag = 0
    ContourAtts.lineWidth = 1
    ContourAtts.singleColor = (0, 0, 0, 255)
    ContourAtts.contourValue = (10, 20, 30, 50)
    ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
    ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
    ContourAtts.wireframe = 1
    SetPlotOptions(ContourAtts)
    DrawPlots()

    #open file, add plot
    if(DOTS):
        CSMI_NAME = STATIONS_DIR + "csmi_date_" + SDATE + ".txt"
        CSMI_2 = STATIONS_DIR + "csmi2_date_" + SDATE + ".txt"
        POT_NAME = STATIONS_DIR + "pot_date_" + SDATE + ".txt"
        POT_2 = STATIONS_DIR + "pot2_date_" + SDATE + ".txt"

        with open(POT_NAME, 'r') as fp:
            numlines = len(fp.readlines())
        if numlines > 1:
            #Actual data
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
            ScatterAtts.var4Min = 0.00
            ScatterAtts.var4Max = 0.02
            ScatterAtts.var4Scaling = ScatterAtts.Linear  # Linear, Log, Skew
            ScatterAtts.var4SkewFactor = 0.1
            ScatterAtts.pointSize = 950 
            ScatterAtts.pointSizePixels = 1
            ScatterAtts.pointType = ScatterAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
            ScatterAtts.scaleCube = 0
            ScatterAtts.colorType = ScatterAtts.ColorByColorTable  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
            ScatterAtts.colorTableName = "turbo"
            ScatterAtts.invertColorTable = 0
            ScatterAtts.legendFlag = 0
            SetPlotOptions(ScatterAtts)
            DrawPlots()
            #Circles
            OpenDatabase(POT_2, 0)
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
            ScatterAtts.var4Min = 0.00
            ScatterAtts.var4Max = 0.02
            ScatterAtts.var4Scaling = ScatterAtts.Linear  # Linear, Log, Skew
            ScatterAtts.var4SkewFactor = 0.1
            ScatterAtts.pointSize = 965 
            ScatterAtts.pointSizePixels = 1
            ScatterAtts.pointType = ScatterAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
            ScatterAtts.scaleCube = 0
            ScatterAtts.colorType = ScatterAtts.ColorBySingleColor  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
            ScatterAtts.singleColor = (0, 0, 0, 255)
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
            ScatterAtts.var4Min = 0.00
            ScatterAtts.var4Max = 0.02
            ScatterAtts.var4Scaling = ScatterAtts.Linear  # Linear, Log, Skew
            ScatterAtts.var4SkewFactor = 0.1
            ScatterAtts.pointSize = 950 
            ScatterAtts.pointSizePixels = 1
            ScatterAtts.pointType = ScatterAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
            ScatterAtts.scaleCube = 0
            ScatterAtts.colorType = ScatterAtts.ColorByColorTable  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
            ScatterAtts.colorTableName = "turbo"
            ScatterAtts.invertColorTable = 0
            ScatterAtts.legendFlag = 0
            SetPlotOptions(ScatterAtts)
            DrawPlots()
            #Circles
            OpenDatabase(CSMI_2, 0)
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
            ScatterAtts.var4Min = 0.00
            ScatterAtts.var4Max = 0.02
            ScatterAtts.var4Scaling = ScatterAtts.Linear  # Linear, Log, Skew
            ScatterAtts.var4SkewFactor = 0.1
            ScatterAtts.pointSize = 965 
            ScatterAtts.pointSizePixels = 1
            ScatterAtts.pointType = ScatterAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
            ScatterAtts.scaleCube = 0
            ScatterAtts.colorType = ScatterAtts.ColorBySingleColor  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
            ScatterAtts.singleColor = (255, 255, 255, 255)
            ScatterAtts.legendFlag = 0
            SetPlotOptions(ScatterAtts)
            DrawPlots()

    #Zoom in
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
    
    #Adjust lighting so spheres are flat
    light0 = LightAttributes()
    light0.enabledFlag = 1
    light0.type = light0.Ambient  # Ambient, Object, Camera
    light0.direction = (0, 0, -1)
    light0.color = (255, 255, 255, 255)
    light0.brightness = 1
    SetLight(0, light0)
    
    #Save the image
    SaveWindowAtts.fileName = PLOT_VAR + "_LAYER=" + str(LAYER) + FILE_TS
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
   
    #Turn all the layers back on for next plots to work
    #TurnMaterialsOn()
    #End create_3D...

    if(DOTS):
        with open(POT_NAME, 'r') as fp:
            numlines = len(fp.readlines())
        if numlines > 1:
            #Close stations file
            SetActivePlots(2)
            DeleteActivePlots()
            CloseDatabase(POT_NAME)
            #Close circles file
            SetActivePlots(2)
            DeleteActivePlots()
            CloseDatabase(POT_2)

        with open(CSMI_NAME, 'r') as fp:
            numlines = len(fp.readlines())
        if numlines > 1:
            #Close stations file
            SetActivePlots(2)
            DeleteActivePlots()
            CloseDatabase(CSMI_NAME)
            #Close circles file
            SetActivePlots(2)
            DeleteActivePlots()
            CloseDatabase(CSMI_2)
 

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

#Month-Day-Year Hour:Minute:Second 
text2D_timestamp = CreateAnnotationObject("Text2D")
text2D_timestamp.position = (0.8, 0.95)
text2D_timestamp.height = 0.015
text2D_timestamp.text = ""

##Disable Pipeline Caching to decrease memory consumption
SetPipelineCachingMode(0) # Disable caching

#DO LOOP 
#Python end range is not included:  this is loop from 1 to 13
#TODO...set range...how to do this if outputs don't line up?
for x in range(MI_START,NUM_MI_FILES+1):
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
    SaveWindowAtts.width = 2048
    SaveWindowAtts.height = 2048

    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = IMGS_DIR 
    #Sets the name below
    ###SaveWindowAtts.fileName = IMGS_NAME
    #Setting family to zero means it will overwrite existing files 
    SaveWindowAtts.family = 0
    #Save pixelData alpha channel (hopefully) to get transparent background
    SaveWindowAtts.pixelData = 3

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
        #define create_pseudocolor_3Dplot(variable, name of image, which layer, plot stations?, timestamp):
        for LAYER in layers:
            create_pseudocolor_3Dplot("TP_EPA",FILE_TS,LAYER,DOTS,ts_station)
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
