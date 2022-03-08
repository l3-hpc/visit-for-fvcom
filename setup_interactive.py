#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

#For exit command
import sys 
sys.path.append("/Users/lisalowe/visit-for-fvcom")

#To calculate normal vector for defining transect
import numpy as np

#Time slider
import datetime
import calendar

def UpdateTimestamp(arg):
    global lastState
    global t_start
    currentState = arg.timeSliderCurrentStates[0]
    if currentState != lastState:
        try:
            m = GetMetaData(arg.activeSource)
            # time:format = "modified julian day (MJD)", so multiply by seconds in a day
            tcur = m.times[currentState]*86400.  + t_start
            ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%Y-%m-%d %H:%M:%S')
            timestamp = "Time: " + ts + " GMT"
            annot_obj = GetAnnotationObject("TimeSlider1") # find out names by GetAnnotationObjectNames()
            annot_obj.text =  timestamp
            annot_obj.position = (0.03, 0.94)
            annot_obj.height = 0.05
            annot_obj.fontBold = 1
            lastState = currentState
        except:
            return

def onSetTimeSliderState0():
    UpdateTimestamp(GetWindowInformation())

def onSetTimeSliderState1(timeState):
    UpdateTimestamp(GetWindowInformation())

def onWindowInformation(arg):
    UpdateTimestamp(arg)

#time:units = "days since 1858-11-17 00:00:00" ;
#       time:format = "modified julian day (MJD)" ;
t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
lastState = -1
RegisterCallback("SetTimeSliderStateRPC", onSetTimeSliderState1)
RegisterCallback("TimeSliderNextStateRPC", onSetTimeSliderState0)
RegisterCallback("TimeSliderPreviousStateRPC", onSetTimeSliderState0)
RegisterCallback("WindowInformation", onWindowInformation)



#This is user defined setpaths.py in the current working directory
import setpaths
#This defines the plot parameters
import setparams

# Set the run name to label the images
RUN_NAME = setparams.set_RUN_NAME()

# Calls setpaths.py to define where the files are located
base_EPA_database = setpaths.set_EPA_path()

# If you will compare 2 data sets
do_compare = setparams.set_do_compare
if(do_compare):
    base_COMPARE_database = setpaths.set_COMPARE_path()
    base_conn_string = setpaths.set_conn_string()
    #Will you compare against Mark's data, with NDZP?
    do_MDR = setparams.set_do_MDR()

#Calls setpaths.py to define where the images are located
IMGS_DIR = setpaths.set_image_path()

#Which MI file to look at
mi_ID_init = setparams.set_MI_ID_INIT()


# Just plot the first timestep of every mi file?
# If not, it will do every single timestep of every file
do_first_in_file = setparams.set_do_first_in_file()

#Which plots to do
do_3Dplot = setparams.set_do3Dplot()
do_2Dslice = setparams.set_do2Dslice()
do_2Dtransect = setparams.set_do2Dtransect()
#set min/max for colormap
#For both TP_EPA and TP_COMPARE
MIN_TP = setparams.set_MIN_TP()
MAX_TP = setparams.set_MAX_TP()
#Title
TITLE_TP_EPA = setparams.set_TITLE_TP_EPA()
#UNITS
UNITS_TP_EPA = setparams.set_UNITS_TP_EPA()

if(do_compare):
    MIN_TP_DIFF = setparams.set_MIN_TP_DIFF()
    MAX_TP_DIFF = setparams.set_MAX_TP_DIFF()
    #Percent change
    MIN_TP_PERCENT_CHANGE = setparams.set_MIN_TP_PERCENT_CHANGE()
    MAX_TP_PERCENT_CHANGE = setparams.set_MAX_TP_PERCENT_CHANGE()
    #Titles
    TITLE_TP_COMPARE = setparams.set_TITLE_TP_COMPARE()
    TITLE_TP_DIFF = setparams.set_TITLE_TP_DIFF()
    TITLE_TP_PERCENT_CHANGE = setparams.set_TITLE_TP_PERCENT_CHANGE()
    #UNITS
    UNITS_TP_COMPARE = setparams.set_UNITS_TP_COMPARE()
    UNITS_TP_DIFF = setparams.set_UNITS_TP_DIFF()
    UNITS_TP_PERCENT_CHANGE = setparams.set_UNITS_TP_PERCENT_CHANGE()


#For transects
if (do_2Dtransect):
   FROM_X = setparams.set_FROM_X() 
   FROM_Y = setparams.set_FROM_Y()
   TO_X = setparams.set_TO_X()
   TO_Y = setparams.set_TO_Y()


def create_pseudocolor_3Dplot(TITLE,UNITS,PLOT_VAR,MIN,MAX):
    title.text = TITLE
    text2D_units.text = UNITS
    AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
    #a = GetAnnotationObjectNames()
    #legend = GetAnnotationObject(a[4])
    #legend.drawTitle=0
    #legend.managePosition=0
    #legend.position = (0.055,0.85)
    #legend.yScale = 1.0

    #Axes are on
    AnnotationAtts = AnnotationAttributes()
    AnnotationAtts.databaseInfoFlag = 0
    AnnotationAtts.axes2D.visible = 1
    AnnotationAtts.axes2D.xAxis.title.visible = 1
    SetAnnotationAttributes(AnnotationAtts)

    DrawPlots()
    SetActivePlots(0)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.colorTableName = "caleblack"
    PseudocolorAtts.min = MIN
    PseudocolorAtts.max = MAX
    SetPlotOptions(PseudocolorAtts)

def create_pseudocolor_2Dslice(TITLE,UNITS,PLOT_VAR,MIN,MAX):
    title.text = TITLE
    text2D_units.text = UNITS
    AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
    AddOperator("Transform",1)
    TransformAtts = TransformAttributes()
    TransformAtts.scaleZ = 1000
    SetOperatorOptions(TransformAtts, 0, 1)
    AddOperator("Slice", 1)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Percent
    SliceAtts.originPercent = 35
    SliceAtts.project2d = 1
    SetOperatorOptions(SliceAtts, 1, 1)
    #a = GetAnnotationObjectNames()
    #legend = GetAnnotationObject(a[4])
    #legend.drawTitle=0
    #legend.managePosition=0
    #legend.position = (0.055,0.85)
    #legend.yScale = 1.0

    ##Just for 2D
    #Axes are on
    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #get rid of x-y-x axis thing in the bottom left
    AnnotationAtts.axes3D.triadFlag = 0
    #Turn on 2D axes
    AnnotationAtts.axes2D.visible = 1
    ##x-axis labeling is fine for slices 
    AnnotationAtts.axes2D.xAxis.title.visible = 1
    AnnotationAtts.axes2D.xAxis.label.visible = 1
    #For y-axis, we want depth, but VisIt relabels it
    AnnotationAtts.axes2D.yAxis.title.visible = 0
    SetAnnotationAttributes(AnnotationAtts)

    DrawPlots()
    SetActivePlots(0)
    SetViewExtentsType("actual")
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.colorTableName = "caleblack"
    PseudocolorAtts.min = MIN
    PseudocolorAtts.max = MAX
    SetPlotOptions(PseudocolorAtts)

def create_pseudocolor_2Dtransect(TITLE,UNITS,PLOT_VAR,MIN,MAX,FROM_X,FROM_Y,TO_X,TO_Y):
    #Calculate arbitrary normal vector from plane
    p1 = np.array([FROM_X,FROM_Y,0])
    p2 = np.array([TO_X, TO_Y, 0])
    p3 = np.array([TO_X, TO_Y, -1000])
    X = np.array([p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2]])
    Y = np.array([p3[0]-p1[0],p3[1]-p1[1],p3[2]-p1[2]])
    myvec = np.cross(X,Y)
    norm_myvec = myvec/np.linalg.norm(myvec)
    #set up plot
    title.text = TITLE
    text2D_units.text = UNITS
    AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
    AddOperator("Transform",1)
    TransformAtts = TransformAttributes()
    TransformAtts.scaleZ = 1000
    SetOperatorOptions(TransformAtts, 0, 1)
    #Select Box
    AddOperator("Box", 1)
    BoxAtts = BoxAttributes()
    BoxAtts.amount = BoxAtts.Some  # Some, All
    BoxAtts.minx = min(p1[0],p2[0])  
    BoxAtts.maxx = max(p1[0],p2[0]) 
    BoxAtts.miny = min(p1[1],p2[1])
    BoxAtts.maxy = max(p1[1],p2[1]) 
    BoxAtts.minz = -250000
    BoxAtts.maxz = 0
    BoxAtts.inverse = 0
    SetOperatorOptions(BoxAtts, 2, 1)
    #Slice
    AddOperator("Slice", 1)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Point  # Point, Intercept, Percent, Zone, Node
    SliceAtts.originPoint = (p1[0], p1[1], p1[2])
    SliceAtts.originIntercept = 0
    SliceAtts.originPercent = 0
    SliceAtts.originZone = 0
    SliceAtts.originNode = 0
    SliceAtts.normal = (norm_myvec[0], norm_myvec[1], norm_myvec[2])
    SliceAtts.axisType = SliceAtts.Arbitrary  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
    SliceAtts.upAxis = (0, 0, 1)
    SliceAtts.project2d = 1
    SliceAtts.interactive = 1
    SliceAtts.flip = 0
    SliceAtts.originZoneDomain = 0
    SliceAtts.originNodeDomain = 0
    SliceAtts.meshName = "Bathymetry_Mesh"
    SliceAtts.theta = 0
    SliceAtts.phi = 0
    SetOperatorOptions(SliceAtts, 1, 1)
    #Annotations
    #a = GetAnnotationObjectNames()
    #legend = GetAnnotationObject(a[4])
    #legend.drawTitle=0
    #legend.managePosition=0
    #legend.position = (0.055,0.85)
    #legend.yScale = 1.0

    ##Just for 2D
    #Axes are on
    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #get rid of x-y-x axis thing in the bottom left
    AnnotationAtts.axes3D.triadFlag = 0
    #Turn on 2D axes
    AnnotationAtts.axes2D.visible = 1
    ##x-axis labeling is fine for slices 
    AnnotationAtts.axes2D.xAxis.title.visible = 1
    AnnotationAtts.axes2D.xAxis.label.visible = 1
    #For y-axis, we want depth, but VisIt relabels it
    AnnotationAtts.axes2D.yAxis.title.visible = 0
    SetAnnotationAttributes(AnnotationAtts)

    DrawPlots()
    SetViewExtentsType("actual")
    SetActivePlots(0)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.colorTableName = "caleblack"
    PseudocolorAtts.min = MIN
    PseudocolorAtts.max = MAX
    SetPlotOptions(PseudocolorAtts)

def transect_against_3D(TITLE,UNITS,PLOT_VAR,MIN,MAX,FROM_X,FROM_Y,TO_X,TO_Y):
    #Calculate arbitrary normal vector from plane
    p1 = np.array([FROM_X,FROM_Y,0])
    p2 = np.array([TO_X, TO_Y, 0])
    p3 = np.array([TO_X, TO_Y, -1000])
    X = np.array([p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2]])
    Y = np.array([p3[0]-p1[0],p3[1]-p1[1],p3[2]-p1[2]])
    myvec = np.cross(X,Y)
    norm_myvec = myvec/np.linalg.norm(myvec)

    #set up plot titles
    title.text = TITLE
    text2D_units.text = UNITS

    #Add plot, set min/max and colormap
    AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
    DrawPlots()
    SetActivePlots(0)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.colorTableName = "caleblack"
    PseudocolorAtts.min = MIN
    PseudocolorAtts.max = MAX
    SetPlotOptions(PseudocolorAtts)

    #Scale Z by 1000 so depth is visible
    AddOperator("Transform",1)
    TransformAtts = TransformAttributes()
    TransformAtts.doRotate = 0
    TransformAtts.rotateOrigin = (0, 0, 0)
    TransformAtts.rotateAxis = (0, 0, 1)
    TransformAtts.rotateAmount = 0
    TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
    TransformAtts.doScale = 1
    TransformAtts.scaleOrigin = (0, 0, 0)
    TransformAtts.scaleX = 1
    TransformAtts.scaleY = 1
    TransformAtts.scaleZ = 1000
    SetOperatorOptions(TransformAtts, 0, 1)
    DrawPlots()

    #Add Mesh Plot with the same attributes
    AddPlot("Mesh", "SigmaLayer_Mesh", 1, 1)
    DrawPlots()

    #This makes the background black
    InvertBackgroundColor()

    #Change the color and opacity of mesh
    SetActivePlots(1)
    MeshAtts = MeshAttributes()
    MeshAtts.legendFlag = 1
    MeshAtts.lineWidth = 0
    MeshAtts.meshColor = (128, 128, 128, 255)
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
    MeshAtts.opacity = 0.333333
    SetPlotOptions(MeshAtts)

    #Select Box, hopefully to just the Active Plots
    SetActivePlots((0, 1))
    SetActivePlots(0)
    AddOperator("Box", 0)
    BoxAtts = BoxAttributes()
    BoxAtts.amount = BoxAtts.Some  # Some, All
    BoxAtts.minx = min(p1[0],p2[0])
    BoxAtts.maxx = max(p1[0],p2[0])
    BoxAtts.miny = min(p1[1],p2[1])
    BoxAtts.maxy = max(p1[1],p2[1])
    BoxAtts.minz = -250000
    BoxAtts.maxz = 0
    BoxAtts.inverse = 0
    SetOperatorOptions(BoxAtts, 1, 0)
    DrawPlots()

    #Add slicing, do NOT project to 2D
    AddOperator("Slice", 0)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Point  # Point, Intercept, Percent, Zone, Node
    SliceAtts.originPoint = (p1[0], p1[1], p1[2])
    SliceAtts.originIntercept = 0
    SliceAtts.originPercent = 0
    SliceAtts.originZone = 0
    SliceAtts.originNode = 0
    SliceAtts.normal = (norm_myvec[0], norm_myvec[1], norm_myvec[2])
    SliceAtts.axisType = SliceAtts.Arbitrary  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
    SliceAtts.upAxis = (0, 0, 1)
    #do not project to 2d
    SliceAtts.project2d = 0
    SliceAtts.interactive = 1
    SliceAtts.flip = 0
    SliceAtts.originZoneDomain = 0
    SliceAtts.originNodeDomain = 0
    SliceAtts.meshName = "Bathymetry_Mesh"
    SliceAtts.theta = 0
    SliceAtts.phi = 0
    #I need to look up what that means
    SetOperatorOptions(SliceAtts, 2, 0)
    DrawPlots()


#Time slider
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

#Set one mi file
mi_ID = mi_ID_init 

##Lisa macOS paths, works to save 4 png files
EPA_database = base_EPA_database + str(mi_ID).zfill(4) + ".nc"
COMPARE_database = base_COMPARE_database + str(mi_ID).zfill(4) + ".nc"
#TODO check if it works on Windows
conn_string = base_conn_string  + str(mi_ID).zfill(4) + ".nc[0]id:TP>, <SigmaLayer_Mesh>)"
#The IMGS_NAME is set below
#Now it is set to overwrite existing files
#IMGS_NAME = base_IMGS_NAME + str(mi_ID).zfill(4) + "."

#Open Databases - the second argument is optional with a default of zero (initial time)
OpenDatabase(EPA_database,0)
OpenDatabase(COMPARE_database,0)

#CreateDatabaseCorrelation("name",(db1,db2),X), here X=2 is a time correlation
CreateDatabaseCorrelation("Correlation01",(EPA_database,COMPARE_database),2)

#Use conn_cmfe function to put EPA's TP variable onto Mark's grid and call it "TP_EPA"
DefineScalarExpression("TP_EPA",conn_string)

#Define the variables for comparing.  For Mark's model, TP consists of NDPZ.
if (do_MDR):
    DefineScalarExpression("TP_COMPARE", "PO4 + 0.016*(Detritus+Phytoplankton+Zooplankton)")
else:
    DefineScalarExpression("TP_COMPARE", "TP")
#Define difference and percent change
DefineScalarExpression("TP_DIFF", "TP_COMPARE - TP_EPA")
DefineScalarExpression("TP_PERCENT_CHANGE", "(TP_EPA - TP_COMPARE)/abs(TP_COMPARE)*100")

AnnotationAtts = AnnotationAttributes()
#Don't print out username and name of database
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.databaseInfoFlag = 0
#get rid of x-y-x axis thing in the bottom left
AnnotationAtts.axes3D.triadFlag = 0
SetAnnotationAttributes(AnnotationAtts)

ToggleLockTime()
ToggleLockViewMode()

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
