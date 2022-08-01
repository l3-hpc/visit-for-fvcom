#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
##macOS paths on local machine

import os
import sys
import datetime
import calendar

#The directory where the mi_XXXX.nc files are located.  The slash at the end of the directory name is required.
#EPA_directory = "/Users/lllowe/MacbookProArchiveMay2022/ORD/CURRENT_TEST/output.0/"
EPA_directory = "/Users/lllowe/Images/new_plots/"

#The directory to write images to.  The slash at the end of the directory name is required.
IMGS_DIR = "/Users/lllowe/Images/triangles"

#mifile name
file_prefix_epa = "mi_"
base_EPA_database = EPA_directory + file_prefix_epa

#Check that all the directories exist
if not os.path.exists(EPA_directory):
    sys.exit("The directory " + EPA_directory + " does not exist.  Check definition of EPA_directory in setpaths.py. Exiting.")

#Create a directory for images if one doesn't exist.
#Note, existing files will be overwritten
if not os.path.exists(IMGS_DIR):
    os.makedirs(IMGS_DIR)

#Define start date
#time:units = "days since 1858-11-17 00:00:00" ;
#       time:format = "modified julian day (MJD)" ;
t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())

#Month-Day-Year Hour:Minute:Second 
text2D_timestamp = CreateAnnotationObject("Text2D")
text2D_timestamp.position = (0.8, 0.85)
text2D_timestamp.height = 0.02
text2D_timestamp.fontBold = 1
text2D_timestamp.text = "UNDEFINED"

#Which file
mi_ID = 6
EPA_database = base_EPA_database + str(mi_ID).zfill(4) + ".nc"

#Open file
OpenDatabase(EPA_database,0)

SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = IMGS_DIR
#Sets the name below
###SaveWindowAtts.fileName = IMGS_NAME
#Setting family to zero means it will overwrite existing files 
#SaveWindowAtts.family = 0
#Set aspect ratio
#SaveWindowAtts.resConstraint = 1 #NoConstraint
#SaveWindowAtts.width = 700
#SaveWindowAtts.height = 600
##Options are: BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, 
##  POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
SaveWindowAtts.format = SaveWindowAtts.PNG
SetSaveWindowAttributes(SaveWindowAtts)

#Get metadata for database
m = GetMetaData(EPA_database)
#Just 1 time point
#I don't know if this worked
#707760
#should be '06-14-2010'
#istate = 0 
istate = 200
SetTimeSliderState(istate)
tcur = m.times[istate]*86400.  + t_start
ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%m-%d-%Y %H:%M:%S')
FILE_TS = "_" + "test" + "." + datetime.datetime.utcfromtimestamp(tcur).strftime('%m-%d-%Y_%H-%M-%S')
timestamp = ts + " "
ts2 = datetime.datetime.utcfromtimestamp(tcur).strftime('%m-%d-%Y')
#text2D_timestamp.text = timestamp 
text2D_timestamp.text = ts2 

#Annotations
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.legendInfoFlag = 1
#Finished setting annotation

#Add pseudocolor plot and set attributes
PLOT_VAR = "TP"
AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
SetActivePlots(0)
#Atts
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.minFlag = 1
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.colorTableName = "caleblack"
PseudocolorAtts.scaling = PseudocolorAtts.Skew  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1e-05
PseudocolorAtts.min = 0.001
PseudocolorAtts.max = 0.1
PseudocolorAtts.legendFlag = 0
SetPlotOptions(PseudocolorAtts)
#SetAtts
DrawPlots()

#Just one layer
TurnMaterialsOff()
LAYER=1
layer_string = "Layer " + str(LAYER)
TurnMaterialsOn(layer_string)
DrawPlots() 

#Project to 2D
AddOperator("Project", 1)
DrawPlots()

#Annotations on 2D plot
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.xAxis.title.visible = 0
AnnotationAtts.axes2D.yAxis.title.visible = 0
AnnotationAtts.axes2D.xAxis.label.visible = 0
AnnotationAtts.axes2D.yAxis.label.visible = 0
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.Off
AnnotationAtts.axes2D.lineWidth = 100 
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial
AnnotationAtts.gradientColor1 = (128, 0, 0, 255)
AnnotationAtts.gradientColor2 = (153, 153, 153, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Gradient
SetAnnotationAttributes(AnnotationAtts)
#Finished setting annotation

#Resize plot and window
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (516628, 572910, 4.75191e+06, 4.79606e+06)
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
#open file, add plot
OpenDatabase("localhost:/Users/lllowe/ORD/MarkR/musk.txt", 0)
AddPlot("Scatter", "TP", 1, 1)
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
ScatterAtts.var4 = "TP"
ScatterAtts.var4MinFlag = 1
ScatterAtts.var4MaxFlag = 1
ScatterAtts.var4Min = 0.001
ScatterAtts.var4Max = 0.1
ScatterAtts.var4Scaling = ScatterAtts.Skew  # Linear, Log, Skew
ScatterAtts.var4SkewFactor = 1e-05
ScatterAtts.pointSize = 700
ScatterAtts.pointSizePixels = 1
ScatterAtts.pointType = ScatterAtts.Icosahedron  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
ScatterAtts.scaleCube = 0
ScatterAtts.colorType = ScatterAtts.ColorByColorTable  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
ScatterAtts.colorTableName = "caleblack"
ScatterAtts.invertColorTable = 0
ScatterAtts.legendFlag = 0
SetPlotOptions(ScatterAtts)
DrawPlots()

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
ScatterAtts.pointSize = 500
ScatterAtts.pointSizePixels = 1
ScatterAtts.pointType = ScatterAtts.Icosahedron  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
ScatterAtts.scaleCube = 0
ScatterAtts.colorType = ScatterAtts.ColorBySingleColor  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
ScatterAtts.singleColor = (128, 0, 128, 255)
ScatterAtts.legendFlag = 0
SetPlotOptions(ScatterAtts)
DrawPlots() 

#Mile marker
#If in UTM 1mile=1609
ActivateDatabase("localhost:/Users/lllowe/MacbookProArchiveMay2022/ORD/CURRENT_TEST/output.0/mi_0006.nc")
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
image = CreateAnnotationObject("Image") 
image.image = "/Users/lllowe/ORD/MarkR/Legend.png"
image.position = (0.05, 0.5)

#695700 of mi_0006.nc
#countors 
#original vs zonal


#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
