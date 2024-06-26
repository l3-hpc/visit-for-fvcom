#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
##macOS paths on local machine

import os
import sys
import re
import numpy as np
import datetime
import calendar


#sys.path.append("/Users/lisalowe/visit-for-fvcom")

#This defines the plot parameters
import getfilenames

#Which layers
which_layers = [4]

# Set the run name to label the images
mifiles = getfilenames.set_which_mifiles()
sfiles  = getfilenames.set_which_sfiles()

numfiles = len(sfiles)
numfiles = numfiles
print("Processing",numfiles,"files")

#istart and end, you can change it
istart = 0
iend = numfiles 
#iend = 10
#istart = 0 
#iend = 10 


#The directory where the mi_XXXX.nc files are located.  The slash at the end of the directory name is required.
#EPA_directory = "/Users/lllowe/MacbookProArchiveMay2022/ORD/CURRENT_TEST/output.0/"
#EPA_directory = "/Users/lllowe/Images/new_plots/"
EPA_directory = "/Users/lllowe/R_apps/LM_data/epa_2015/dates_output/"
Station_directory = "/Users/lllowe/JamesPaper/RforLM/stations/2015/"

#The directory to write images to.  The slash at the end of the directory name is required.
IMGS_DIR = "/Users/lllowe/JamesPaper/Images-2015/turbo/Layer=4/"

#Check that all the directories exist
if not os.path.exists(EPA_directory):
    sys.exit("The directory " + EPA_directory + " does not exist.  Check definition of EPA_directory in setpaths.py. Exiting.")

#Create a directory for images if one doesn't exist.
#Note, existing files will be overwritten
if not os.path.exists(IMGS_DIR):
    os.makedirs(IMGS_DIR)

#don't make another annotation
notime = 0
#for file_prefix_epa in sfiles:
for i in range(istart,iend):
    EPA_database = EPA_directory + mifiles[i]
    print("Model file:",mifiles[i])
    #IMGS_NAME = file_prefix_epa + "_Layer=" + str(LAYER)
    STATIONS_NAME = Station_directory + sfiles[i] 
    print("Station file:",sfiles[i])

    for x in which_layers:
        
        LAYER = x
        url = mifiles[i]
        url = re.sub('\.nc','',url) 
        IMGS_NAME = url + "_Layer=" + str(LAYER)
        #print(LAYER)
        print(IMGS_NAME) 
        #sys.exit()
        #Open file
        OpenDatabase(EPA_database,0)

        t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
        if(notime == 0):
            text2D_timestamp = CreateAnnotationObject("Text2D")
            notime = 1
        text2D_timestamp.position = (0.78,0.9)
        text2D_timestamp.height = 0.020
        m = GetMetaData(EPA_database)
        istate = 0
        tcur = m.times[istate]*86400.  + t_start
        ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%m-%d-%Y %H:%M')
        timestamp = ts
        text2D_timestamp.text = timestamp

        #Get metadata for database
        m = GetMetaData(EPA_database)
   
        #Annotations on 2D plot
        AnnotationAtts = AnnotationAttributes()
        AnnotationAtts.userInfoFlag = 0
        AnnotationAtts.databaseInfoFlag = 0
        AnnotationAtts.axes3D.triadFlag = 0
        AnnotationAtts.legendInfoFlag = 0
        AnnotationAtts.axes2D.visible = 0
        AnnotationAtts.axes2D.xAxis.title.visible = 0
        AnnotationAtts.axes2D.yAxis.title.visible = 0
        AnnotationAtts.axes2D.xAxis.label.visible = 0
        AnnotationAtts.axes2D.yAxis.label.visible = 0
        AnnotationAtts.backgroundColor = (153, 153, 153, 255)
        AnnotationAtts.foregroundColor = (0, 0, 0, 255)
        AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
        AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.Off
        SetAnnotationAttributes(AnnotationAtts)
        #Finished setting annotation
 
        
        #Add pseudocolor plot and set attributes
        PLOT_VAR = "TP"
        AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
        SetActivePlots(0)
        #Atts
        PseudocolorAtts = PseudocolorAttributes()
        PseudocolorAtts.minFlag = 1
        PseudocolorAtts.maxFlag = 1
        PseudocolorAtts.colorTableName = "turbo"
        PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
        PseudocolorAtts.skewFactor = 1e-05
        PseudocolorAtts.min = 0.001
        PseudocolorAtts.max = 0.03
        PseudocolorAtts.legendFlag = 0
        SetPlotOptions(PseudocolorAtts)
        #SetAtts
        DrawPlots()
        
        #Just one layer
        TurnMaterialsOff()
        layer_string = "Layer " + str(LAYER)
        TurnMaterialsOn(layer_string)
        DrawPlots() 
        
        #Project to 2D
        AddOperator("Project", 1)
        DrawPlots()
        
        #Resize plot and window
        View2DAtts = View2DAttributes()
        View2DAtts.windowCoords = (521942, 566839, 4.75634e+06, 4.79812e+06)
        View2DAtts.viewportCoords = (0, 1, 0, 1) 
        View2DAtts.fullFrameActivationMode = View2DAtts.On  # On, Off, Auto
        View2DAtts.fullFrameAutoThreshold = 100
        View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
        View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
        View2DAtts.windowValid = 1
        SetView2D(View2DAtts)
        # End spontaneous state
        
        #Add shoreline
        AddPlot("Subset", "Bathymetry_Mesh", 1, 1)
        SetActivePlots(1)
        SubsetAtts = SubsetAttributes()
        SubsetAtts.colorType = SubsetAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
        SubsetAtts.legendFlag = 0
        SubsetAtts.lineWidth = 2
        SubsetAtts.singleColor = (0, 0, 0, 255)
        SubsetAtts.subsetNames = ("Whole mesh (Bathymetry_Mesh)")
        SubsetAtts.opacity = 1
        SubsetAtts.wireframe = 1
        SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
        SubsetAtts.pointSizePixels = 2
        SetPlotOptions(SubsetAtts)
        DrawPlots()
        
        #Add bathymetry
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
        
        ##Add measured data points
        #set file open defaults
        plainTextOpenOptions = GetDefaultFileOpenOptions("PlainText")
        plainTextOpenOptions['First row has variable names'] = 1
        plainTextOpenOptions['Lines to skip at beginning of file'] = 0
        plainTextOpenOptions['Column for X coordinate (or -1 for none)'] = 0
        plainTextOpenOptions['Column for Y coordinate (or -1 for none)'] = 1
        plainTextOpenOptions['Column for Z coordinate (or -1 for none)'] = 2
        SetDefaultFileOpenOptions("PlainText", plainTextOpenOptions)
        
        ##Add river points
        #open file, add plot
        OpenDatabase("localhost:/Users/lllowe/ORD/MarkR/points.txt", 0)
        AddPlot("Scatter", "Point", 1, 1)
        ScatterAtts = ScatterAttributes()
        ScatterAtts.var1 = "x"
        ScatterAtts.var1Role = ScatterAtts.Coordinate0  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
        ScatterAtts.var1Scaling = ScatterAtts.Linear  # Linear, Log, Skew
        ScatterAtts.var2Role = ScatterAtts.Coordinate1  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
        ScatterAtts.var2 = "y"
        ScatterAtts.var2Scaling = ScatterAtts.Linear  # Linear, Log, Skew
        ScatterAtts.var3Role = ScatterAtts.NONE  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
        ScatterAtts.var3 = "default"
        ScatterAtts.var4Role = ScatterAtts.Color  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
        ScatterAtts.var4 = "Point"
        ScatterAtts.pointSize = 1000
        ScatterAtts.pointSizePixels = 1
        ScatterAtts.pointType = ScatterAtts.Octahedron  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
        ScatterAtts.scaleCube = 0
        ScatterAtts.colorType = ScatterAtts.ColorBySingleColor  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
        ScatterAtts.singleColor = (0, 0, 255, 255)
        ScatterAtts.legendFlag = 0
        SetPlotOptions(ScatterAtts)
        DrawPlots() 

        #open file, add plot
        OpenDatabase(STATIONS_NAME, 0)
        AddPlot("Scatter", "TP", 1, 1)
        ScatterAtts = ScatterAttributes()
        ScatterAtts.var1 = "X"
        ScatterAtts.var1Role = ScatterAtts.Coordinate0  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
        ScatterAtts.var1Scaling = ScatterAtts.Linear  # Linear, Log, Skew
        ScatterAtts.var2Role = ScatterAtts.Coordinate1  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
        ScatterAtts.var2 = "Y"
        ScatterAtts.var2Scaling = ScatterAtts.Linear  # Linear, Log, Skew
        ScatterAtts.var3Role = ScatterAtts.NONE  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
        ScatterAtts.var3 = "default"
        ScatterAtts.var4Role = ScatterAtts.Color  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
        ScatterAtts.var4 = "TP"
        ScatterAtts.var4MinFlag = 1
        ScatterAtts.var4MaxFlag = 1
        ScatterAtts.var4Min = 0.001
        ScatterAtts.var4Max = 0.03
        ScatterAtts.var4Scaling = ScatterAtts.Linear  # Linear, Log, Skew
        ScatterAtts.var4SkewFactor = 1e-05
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

        
        #Mile marker
        #If in UTM 1mile=1609
        ActivateDatabase(EPA_database)
        AddPlot("Contour", "y", 1, 1)
        SetActivePlots(5)
        DrawPlots()
        ContourAtts = ContourAttributes()
        ContourAtts.colorType = ContourAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
        ContourAtts.legendFlag = 0
        ContourAtts.lineWidth = 5
        ContourAtts.singleColor = (0, 0, 0, 255)
        ContourAtts.contourValue = (4.76036e+06)
        ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
        ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
        ContourAtts.wireframe = 0
        SetPlotOptions(ContourAtts)
        
        AddOperator("Box", 0)
        BoxAtts = BoxAttributes()
        BoxAtts.amount = BoxAtts.Some  # Some, All
        BoxAtts.minx = 554423
        BoxAtts.maxx = 556032
        BoxAtts.miny = 4.74736e+06
        BoxAtts.maxy = 4.76736e+06
        BoxAtts.minz = -1
        BoxAtts.maxz = 1
        SetOperatorOptions(BoxAtts, 1, 0)
        DrawPlots()
        
        #AddImage
        #image = CreateAnnotationObject("Image") 
        #image.image = "/Users/lllowe/ORD/MarkR/Legend.png"
        #image.position = (0.05, 0.5)
        
        SaveWindowAtts = SaveWindowAttributes()
        SaveWindowAtts.outputToCurrentDirectory = 0
        SaveWindowAtts.outputDirectory = IMGS_DIR 
        SaveWindowAtts.fileName = IMGS_NAME 
        SaveWindowAtts.family = 0
        SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
        SaveWindowAtts.width = 1024
        SaveWindowAtts.height = 1024
        SaveWindowAtts.screenCapture = 0
        SaveWindowAtts.saveTiled = 0
        SaveWindowAtts.quality = 80
        SaveWindowAtts.progressive = 0
        SaveWindowAtts.binary = 0
        SaveWindowAtts.stereo = 0
        SaveWindowAtts.compression = SaveWindowAtts.NONE  # NONE, PackBits, Jpeg, Deflate, LZW
        SaveWindowAtts.forceMerge = 0
        SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
        SaveWindowAtts.pixelData = 1
        SaveWindowAtts.opts.types = ()
        SaveWindowAtts.opts.help = ""
        SetSaveWindowAttributes(SaveWindowAtts)
        SaveWindow()
        
        DeleteAllPlots()
        ClearCacheForAllEngines()
    
sys.exit()
        
        
#695700 of mi_0006.nc
#countors 
#original vs zonal
    
    
#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

#record macro
#q<register><commands>q
#So: q a down firstchar insert tab escape q
#Then to use, @@ or 100@@
