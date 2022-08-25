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

#Which layers
which_layers = [1]

# Set the run name to label the images
mifiles = ["date_0718201520.nc"] 
sfiles  = ["date_07182015.txt"] 

#The directory where the mi_XXXX.nc files are located.  The slash at the end of the directory name is required.
#EPA_directory = "/Users/lllowe/MacbookProArchiveMay2022/ORD/CURRENT_TEST/output.0/"
#EPA_directory = "/Users/lllowe/Images/new_plots/"
EPA_directory = "/Users/lllowe/R_apps/LM_data/epa_2015/dates_output/"
Station_directory = "/Users/lllowe/r-for-fvcom/stations/2015/"

i = 0
EPA_database = EPA_directory + mifiles[i] 
#IMGS_NAME = file_prefix_epa + "_Layer=" + str(LAYER)
CSMI_NAME = Station_directory + "csmi_" + sfiles[i]


LAYER = 1
url = mifiles[i]
url = re.sub('\.nc','',url) 
IMGS_NAME = url + "_Layer=" + str(LAYER)
#print(LAYER)
print(IMGS_NAME) 
#sys.exit()
#Open file
OpenDatabase(EPA_database,0)

t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
text2D_timestamp = CreateAnnotationObject("Text2D")
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
AnnotationAtts.backgroundColor = (0, 0, 0, 255)
AnnotationAtts.foregroundColor = (255, 255, 255, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.Off
AnnotationAtts.axes2D.lineWidth = 100
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
PseudocolorAtts.scaling = PseudocolorAtts.Skew  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1e-05
PseudocolorAtts.min = 0.001
PseudocolorAtts.max = 0.1
PseudocolorAtts.legendFlag = 1
SetPlotOptions(PseudocolorAtts)
#SetAtts
DrawPlots()

#Just one layer
TurnMaterialsOff()
layer_string = "Layer " + str(LAYER)
TurnMaterialsOn(layer_string)
DrawPlots() 

#
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
ScatterAtts.var3Role = ScatterAtts.Coordinate2  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
ScatterAtts.var3 = "z"
ScatterAtts.var4Role = ScatterAtts.Color  # Coordinate0, Coordinate1, Coordinate2, Color, NONE
ScatterAtts.var4 = "Point"
ScatterAtts.pointSize = 1000
ScatterAtts.pointSizePixels = 1
ScatterAtts.pointType = ScatterAtts.Axis  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
ScatterAtts.scaleCube = 0
ScatterAtts.colorType = ScatterAtts.ColorByForegroundColor  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
ScatterAtts.singleColor = (0, 0, 0, 255)
ScatterAtts.legendFlag = 0
SetPlotOptions(ScatterAtts)
DrawPlots() 

OpenDatabase("localhost:/Users/lllowe/JamesPaper/Shapefiles/NHD_Sel_MI_Rivers_UTM16.shp", 0)
AddPlot("Mesh", "polylineZ", 1, 1)
DrawPlots()

MeshAtts = MeshAttributes()
MeshAtts.legendFlag = 1
MeshAtts.lineWidth = 5
MeshAtts.meshColor = (0, 0, 255, 255)
MeshAtts.meshColorSource = MeshAtts.MeshCustom  # Foreground, MeshCustom, MeshRandom
MeshAtts.opaqueColorSource = MeshAtts.Background  # Background, OpaqueCustom, OpaqueRandom
MeshAtts.opaqueMode = MeshAtts.Auto  # Auto, On, Off
MeshAtts.pointSize = 0.05
MeshAtts.opaqueColor = (255, 255, 255, 255)
MeshAtts.smoothingLevel = MeshAtts.NONE  # NONE, Fast, High
MeshAtts.pointSizeVarEnabled = 0
MeshAtts.pointSizeVar = "default"
MeshAtts.pointType = MeshAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
MeshAtts.showInternal = 0
MeshAtts.pointSizePixels = 2
MeshAtts.opacity = 1
SetPlotOptions(MeshAtts)

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
ScatterAtts.var4Min = 0.001
ScatterAtts.var4Max = 0.1
ScatterAtts.var4Scaling = ScatterAtts.Skew  # Linear, Log, Skew
ScatterAtts.var4SkewFactor = 1e-05
ScatterAtts.pointSize = 800
ScatterAtts.pointSizePixels = 1
ScatterAtts.pointType = ScatterAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
ScatterAtts.scaleCube = 0
ScatterAtts.colorType = ScatterAtts.ColorByColorTable  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
ScatterAtts.colorTableName = "turbo"
ScatterAtts.invertColorTable = 0
ScatterAtts.legendFlag = 0
SetPlotOptions(ScatterAtts)
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

