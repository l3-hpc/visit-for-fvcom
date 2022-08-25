#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
##macOS paths on local machine
import os
import sys
import re
import numpy as np
import datetime
import calendar


#Which layers
which_layers = [1]

# Set the run name to label the images
mifiles = ["date_0717201512.nc"] 
sfiles  = ["date_07172015.txt"] 

#The directory where the nc and txt files are located.  The slash at the end of the directory name is required.
EPA_directory = "/Users/lllowe/visit-for-fvcom/"
Station_directory = "/Users/lllowe/visit-for-fvcom/"
Shapefile_directory = "Users/lllowe/visit-for-fvcom/"

#This is cut/paste from the original loop using 'i'
i = 0
EPA_database = EPA_directory + mifiles[i] 
#IMGS_NAME = file_prefix_epa + "_Layer=" + str(LAYER)
STATIONS_NAME = Station_directory + sfiles[i] 
CSMI_NAME = Station_directory + "csmi_" + sfiles[i]


LAYER = 1
url = mifiles[i]
#string reformatting thing
url = re.sub('\.nc','',url) 
IMGS_NAME = url + "_Layer=" + str(LAYER)
#print(LAYER)
print(IMGS_NAME) 

#Open file
OpenDatabase(EPA_database,0)

#Creates date/time stamp based on .nc file metadata
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
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.axes3D.visible = 0
#Black background
AnnotationAtts.backgroundColor = (0, 0, 0, 255)
#White foreground
AnnotationAtts.foregroundColor = (255, 255, 255, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
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
#If you change the colormap, change it in Scatter to be the same
PseudocolorAtts.skewFactor = 0.1
PseudocolorAtts.min = 0.002
PseudocolorAtts.max = 0.035
PseudocolorAtts.colorTableName = "turbo"
PseudocolorAtts.scaling = PseudocolorAtts.Skew  # Linear, Log, Skew
PseudocolorAtts.legendFlag = 1
SetPlotOptions(PseudocolorAtts)
#SetAtts
DrawPlots()

#Format the legend
plotName = GetPlotList().GetPlots(0).plotName
legend = GetAnnotationObject(plotName)
legend.managePosition = 0
legend.position = (0.7,0.65)
legend.drawTitle=0
legend.drawMinMax = 0
legend.numberFormat = "%1.3f"


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


#Add 'shoreline', which is just model border
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

##Add measured data points
#set file open defaults
plainTextOpenOptions = GetDefaultFileOpenOptions("PlainText")
plainTextOpenOptions['First row has variable names'] = 1
plainTextOpenOptions['Lines to skip at beginning of file'] = 0
plainTextOpenOptions['Column for X coordinate (or -1 for none)'] = 0
plainTextOpenOptions['Column for Y coordinate (or -1 for none)'] = 1
plainTextOpenOptions['Column for Z coordinate (or -1 for none)'] = 2
SetDefaultFileOpenOptions("PlainText", plainTextOpenOptions)

#River shapefile from Tom H.
OpenDatabase(Shapefile_directory + "Shapefiles/NHD_Sel_MI_Rivers_UTM16.shp", 0)
AddPlot("Mesh", "polylineZ", 1, 1)
DrawPlots()
#Make the lines thicker (lineWidth=5) and blue mesh color
MeshAtts = MeshAttributes()
MeshAtts.legendFlag = 0
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

#It resets the view after the shape file thing, so recenter
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

#open file, add plot
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
#If you change the colormap, change it in Pseudo to be the same
ScatterAtts.var4Min = 0.002
ScatterAtts.var4Max = 0.035
ScatterAtts.var4Scaling = ScatterAtts.Skew  # Linear, Log, Skew
ScatterAtts.var4SkewFactor = 0.1
#Change size of marker here
ScatterAtts.pointSize = 600
ScatterAtts.pointSizePixels = 1
#Change type of marker here
ScatterAtts.pointType = ScatterAtts.Sphere  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
ScatterAtts.scaleCube = 0
ScatterAtts.colorType = ScatterAtts.ColorByColorTable  # ColorByForegroundColor, ColorBySingleColor, ColorByColorTable
ScatterAtts.colorTableName = "turbo"
ScatterAtts.invertColorTable = 0
ScatterAtts.legendFlag = 0
SetPlotOptions(ScatterAtts)
DrawPlots()


#Save
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
