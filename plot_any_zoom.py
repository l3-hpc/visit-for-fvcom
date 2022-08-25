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

# Will you compare 2 data sets?
do_compare = setparams.set_do_compare()
if(do_compare):
    base_COMPARE_database = setpaths.set_COMPARE_path()
    base_conn_string = setpaths.set_conn_string()
    #Will you compare against Mark's data, with NDZP?
    do_MDR = setparams.set_do_MDR()

# Do you want to remove annotations?
remove_annotation = setparams.set_remove_annotation()

#Define where the images should be printed out
#If the images exist already, they will be overwritten
IMGS_DIR = setpaths.set_image_path()

#How many mi files are available?
#TODO Change this to look at the path and calculate
NUM_MI_FILES = setparams.set_NUM_MI_FILES()

# Just plot the first timestep of every mi file?
# If not, it will do every single timestep of every file
do_first_in_file = setparams.set_do_first_in_file()
#Instead of doing every single timestep of every file,
# skip some of them
skip_states = setparams.set_skip()

#Which plots to do
do_3Dplot = setparams.set_do3Dplot()
do_2Dslice = setparams.set_do2Dslice()
do_2Dtransect = setparams.set_do2Dtransect()

#Which layers to plot
layers = setparams.set_which_layers()

#Add mesh?
#TODO:  make a parameter
add_mesh = True

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

if(do_compare):
    #Colormaps for comparision datasets
    MIN_TP_DIFF = setparams.set_MIN_TP_DIFF()
    MAX_TP_DIFF = setparams.set_MAX_TP_DIFF()
    MIN_TP_PERCENT_CHANGE = setparams.set_MIN_TP_PERCENT_CHANGE()
    MAX_TP_PERCENT_CHANGE = setparams.set_MAX_TP_PERCENT_CHANGE()
    #Variable name for annotating the comparison dataset 
    TITLE_TP_COMPARE = setparams.set_TITLE_TP_COMPARE()
    TITLE_TP_DIFF = setparams.set_TITLE_TP_DIFF()
    TITLE_TP_PERCENT_CHANGE = setparams.set_TITLE_TP_PERCENT_CHANGE()
    #Unit name for annotating comparison dataset 
    UNITS_TP_COMPARE = setparams.set_UNITS_TP_COMPARE()
    UNITS_TP_DIFF = setparams.set_UNITS_TP_DIFF()
    UNITS_TP_PERCENT_CHANGE = setparams.set_UNITS_TP_PERCENT_CHANGE()


#For transects
if (do_2Dtransect):
    FROM_X = setparams.set_FROM_X() 
    FROM_Y = setparams.set_FROM_Y()
    TO_X = setparams.set_TO_X()
    TO_Y = setparams.set_TO_Y()

#This creates a bird's eye view of the plot.  It is called 3D, but now
# since we've added 'Layer', it is not quite 3D...
def create_pseudocolor_3Dplot(TITLE,UNITS,PLOT_VAR,MIN,MAX,FILE_TS,LAYER,SKEW):
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
        PseudocolorAtts.max = 0.035
    else:
        PseudocolorAtts.scaling = PseudocolorAtts.Linear
        PseudocolorAtts.min = MIN
        PseudocolorAtts.max = MAX
    SetPlotOptions(PseudocolorAtts)
    #Comment out since showing triangles overwhelms the plot
    # if(add_mesh):
    #     AddPlot("Mesh", "SigmaLayer_Mesh", 1, 1)
    DrawPlots()

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

#Comment out since showing triangles overwhelms the plot
#    if(add_mesh):
#        AddPlot("Mesh", "SigmaLayer_Mesh", 1, 1)

    #Choose which layer will be shown
    #- First, turn all of them off
    TurnMaterialsOff()
    #Names of layers are actually a string...
    # might have to confirm this always works 
    layer_string = "Layer " + str(LAYER)
    TurnMaterialsOn(layer_string)
    DrawPlots()
    #End layer choosing

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


def create_pseudocolor_2Dslice(TITLE,UNITS,PLOT_VAR,MIN,MAX,FILE_TS,SKEW):
    #Variable name and units, with option to leave blank 
    if(remove_annotation):
        title.text = ""
        text2D_units.text =  ""
        text2D_timestamp.text =  ""
    else:
        title.text = TITLE
        text2D_units.text = UNITS
        text2D_timestamp.text = timestamp
    #Add pseudocolor plot and set attributes
    AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.colorTableName = "turbo"
    if(SKEW):
        PseudocolorAtts.scaling = PseudocolorAtts.Skew  # Linear, Log, Skew
        PseudocolorAtts.skewFactor = 0.1 
        PseudocolorAtts.min = 0.002
        PseudocolorAtts.max = 0.035
    else:
        PseudocolorAtts.scaling = PseudocolorAtts.Linear
        PseudocolorAtts.min = MIN
        PseudocolorAtts.max = MAX
    SetPlotOptions(PseudocolorAtts)
    #Scale Z by 1000
    AddOperator("Transform",1)
    TransformAtts = TransformAttributes()
    TransformAtts.scaleZ = 1000
    SetOperatorOptions(TransformAtts, 0, 1)
    #Add 2d slice, now hardcoded for 35percent of grid 
    AddOperator("Slice", 1)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Percent
    SliceAtts.originPercent = 35
    SliceAtts.project2d = 1
    SetOperatorOptions(SliceAtts, 1, 1)
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
    SetAnnotationAttributes(AnnotationAtts)
    DrawPlots()
    SetActivePlots(0)
    SetViewExtentsType("actual")
    #Add mesh, which is sigma layers
    if(add_mesh):
        AddPlot("Mesh", "SigmaLayer_Mesh", 1, 1)
        DrawPlots()
    #Save the image
    SaveWindowAtts.fileName = PLOT_VAR + "_" + "slice" + FILE_TS
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

def create_pseudocolor_2Dtransect(TITLE,UNITS,PLOT_VAR,MIN,MAX,FILE_TS,
                                  FROM_X,FROM_Y,TO_X,TO_Y,SKEW):
    #Calculate arbitrary normal vector from plane
    p1 = np.array([FROM_X,FROM_Y,0])
    p2 = np.array([TO_X, TO_Y, 0])
    p3 = np.array([TO_X, TO_Y, -1000])
    X = np.array([p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2]])
    Y = np.array([p3[0]-p1[0],p3[1]-p1[1],p3[2]-p1[2]])
    myvec = np.cross(X,Y)
    norm_myvec = myvec/np.linalg.norm(myvec)

    #Variable name and units, with option to leave blank
    if(remove_annotation):
        title.text = ""
        text2D_units.text =  ""
        text2D_timestamp.text =  ""
    else:
        title.text = TITLE
        text2D_units.text = UNITS
        text2D_timestamp.text = timestamp

    #Add pseudocolor plot and set attributes
    AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.colorTableName = "turbo"
    #SKEW colormap allows a wider range to be shown
    #TODO: set min/max/factor for skew in setparams 
    if(SKEW):
        PseudocolorAtts.scaling = PseudocolorAtts.Skew  # Linear, Log, Skew
        PseudocolorAtts.skewFactor = 0.1 
        PseudocolorAtts.min = 0.002
        PseudocolorAtts.max = 0.035
    else:
        PseudocolorAtts.scaling = PseudocolorAtts.Linear
        PseudocolorAtts.min = MIN
        PseudocolorAtts.max = MAX
    SetPlotOptions(PseudocolorAtts)

    #In order to see depth, Scale Z by 1000
    AddOperator("Transform",1)
    TransformAtts = TransformAttributes()
    TransformAtts.scaleZ = 1000
    SetOperatorOptions(TransformAtts, 0, 1)
    #Select the Box operator to limit range of 'diagonal slice'
    # to the start and end of the transect
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
    #SliceAtts.(Point, Intercept, Percent, Zone, or Node)
    SliceAtts.originType = SliceAtts.Point
    SliceAtts.originPoint = (p1[0], p1[1], p1[2])
    SliceAtts.originIntercept = 0
    SliceAtts.originPercent = 0
    SliceAtts.originZone = 0
    SliceAtts.originNode = 0
    SliceAtts.normal = (norm_myvec[0], norm_myvec[1], norm_myvec[2])
    #SliceAtts.(XAxis, YAxis, ZAxis, Arbitrary, or ThetaPhi)
    SliceAtts.axisType = SliceAtts.Arbitrary 
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

    # Start setting the annotation attributes
    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #get rid of x-y-x axis thing in the bottom left
    AnnotationAtts.axes3D.triadFlag = 0
    #Turn on 2D axes
    AnnotationAtts.axes2D.visible = 1
    ##Turn off x-axis because it doesn't mean anything for transects
    AnnotationAtts.axes2D.xAxis.title.visible = 0
    AnnotationAtts.axes2D.xAxis.label.visible = 0
    #For y-axis, we want depth, but VisIt relabels it
    AnnotationAtts.axes2D.yAxis.title.visible = 0
    AnnotationAtts.axes2D.yAxis.title.units = "meters"
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
    SetAnnotationAttributes(AnnotationAtts)
    #Finished setting annotation

    #Overlay mesh, shows sigma layers
    if(add_mesh):
        AddPlot("Mesh", "SigmaLayer_Mesh", 1, 1)
        DrawPlots()
    #Zoom in, set min/max to extent, 'actual' extent of data shown
    SetViewExtentsType("actual")
    SetActivePlots(0)
    DrawPlots()
    SaveWindowAtts.fileName = PLOT_VAR + "_" + "transect" + FILE_TS
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()


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
title.text = "UNDEFINED" 
#Title text will be redefined for each plot
text2D_units = CreateAnnotationObject("Text2D")
text2D_units.position = (0.05, 0.90)
text2D_units.height = 0.015
text2D_units.text = "UNDEFINED"

#Month-Day-Year Hour:Minute:Second 
text2D_timestamp = CreateAnnotationObject("Text2D")
text2D_timestamp.position = (0.45, 0.95)
text2D_timestamp.height = 0.015
text2D_timestamp.text = "UNDEFINED"

##Disable Pipeline Caching to decrease memory consumption
SetPipelineCachingMode(0) # Disable caching

#DO LOOP 
#Python end range is not included:  this is loop from 1 to 13
#TODO...set range...how to do this if outputs don't line up?
for x in range(1,NUM_MI_FILES+1):
    mi_ID = x
    ##Lisa macOS paths, works to save 4 png files
    EPA_database = base_EPA_database + str(mi_ID).zfill(4) + ".nc"
    if(do_compare):
        COMPARE_database = base_COMPARE_database + str(mi_ID).zfill(4) + ".nc"
#TODO check if it works on Windows
        conn_string = (base_conn_string  + str(mi_ID).zfill(4) 
                   + ".nc[0]id:TP>, <SigmaLayer_Mesh>)")
    #The IMGS_NAME is set below
    #Now it is set to overwrite existing files

    #Open Databases - the second argument is optional with a default of zero 
    #Where zero = initial time
    OpenDatabase(EPA_database,0)
    if(do_compare):
        OpenDatabase(COMPARE_database,0)
        #CreateDatabaseCorrelation("name",(db1,db2),X) 
        # Here, X=2 is a time correlation
        CreateDatabaseCorrelation("Correlation01",(EPA_database,COMPARE_database),2)

        #Use conn_cmfe function to put EPA's TP variable onto Mark's grid 
        # and call it "TP_EPA"
        DefineScalarExpression("TP_EPA",conn_string)

        #Define the variables for comparing.  For Mark's model, TP consists of NDPZ.
        if (do_MDR):
           DefineScalarExpression("TP_COMPARE", "PO4 + 0.016*(Detritus+Phytoplankton+Zooplankton)")
        else:
           DefineScalarExpression("TP_COMPARE", "TP")
        #Define difference and percent change
        DefineScalarExpression("TP_DIFF", "TP_COMPARE - TP_EPA")
        DefineScalarExpression("TP_PERCENT_CHANGE", "(TP_EPA - TP_COMPARE)/abs(TP_COMPARE)*100")
    else:
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


        if(do_3Dplot): 
            #def create_pseudocolor_3Dplot(TITLE,UNITS,PLOT_VAR,MIN,MAX,FILE_TS):
            for LAYER in layers:
                create_pseudocolor_3Dplot(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA", 
                    MIN_TP,MAX_TP,FILE_TS,LAYER,SKEW)
                DeleteAllPlots()
                if(do_compare):
                    create_pseudocolor_3Dplot(TITLE_TP_COMPARE,UNITS_TP_COMPARE,"TP_COMPARE", MIN_TP,MAX_TP,FILE_TS,LAYER,SKEW)
                    DeleteAllPlots() 
                    create_pseudocolor_3Dplot(TITLE_TP_PERCENT_CHANGE,UNITS_TP_PERCENT_CHANGE,"TP_PERCENT_CHANGE", MIN_TP_PERCENT_CHANGE,MAX_TP_PERCENT_CHANGE,FILE_TS,LAYER,False)
                    DeleteAllPlots()
                    create_pseudocolor_3Dplot(TITLE_TP_DIFF,UNITS_TP_DIFF,"TP_DIFF",MIN_TP_DIFF,MAX_TP_DIFF,FILE_TS,LAYER,False)
                    DeleteAllPlots()

        if(do_2Dslice):
            #def create_pseudocolor_2Dslice(TITLE,UNITS,PLOT_VAR,MIN,MAX,FILE_TS):
            create_pseudocolor_2Dslice(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA",MIN_TP,MAX_TP,FILE_TS,SKEW)
            DeleteAllPlots()
            if(do_compare):
                create_pseudocolor_2Dslice(TITLE_TP_COMPARE,UNITS_TP_COMPARE,"TP_COMPARE", MIN_TP,MAX_TP,FILE_TS,SKEW)
                DeleteAllPlots()
                create_pseudocolor_2Dslice(TITLE_TP_PERCENT_CHANGE,UNITS_TP_PERCENT_CHANGE,"TP_PERCENT_CHANGE", MIN_TP_PERCENT_CHANGE,MAX_TP_PERCENT_CHANGE,FILE_TS,False)
                DeleteAllPlots()
                create_pseudocolor_2Dslice(TITLE_TP_DIFF,UNITS_TP_DIFF,"TP_DIFF",MIN_TP_DIFF,MAX_TP_DIFF,FILE_TS,False)
                DeleteAllPlots()

        if(do_2Dtransect):
            #def create_pseudocolor_2Dtransect(TITLE,UNITS,PLOT_VAR,MIN,MAX,FILE_TS):
            create_pseudocolor_2Dtransect(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA", MIN_TP,MAX_TP,FILE_TS,FROM_X,FROM_Y,TO_X,TO_Y,SKEW)
            DeleteAllPlots()
            if(do_compare):
                create_pseudocolor_2Dtransect(TITLE_TP_COMPARE,UNITS_TP_COMPARE,"TP_COMPARE", MIN_TP,MAX_TP,FILE_TS,FROM_X,FROM_Y,TO_X,TO_Y,SKEW)
                DeleteAllPlots()
                create_pseudocolor_2Dtransect(TITLE_TP_PERCENT_CHANGE,UNITS_TP_PERCENT_CHANGE,"TP_PERCENT_CHANGE", MIN_TP_PERCENT_CHANGE,MAX_TP_PERCENT_CHANGE,FILE_TS,FROM_X,FROM_Y,TO_X,TO_Y,False)
                DeleteAllPlots()
                create_pseudocolor_2Dtransect(TITLE_TP_DIFF,UNITS_TP_DIFF,"TP_DIFF",MIN_TP_DIFF,MAX_TP_DIFF, FILE_TS,FROM_X,FROM_Y,TO_X,TO_Y,False)
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
