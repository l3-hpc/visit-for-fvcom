Here you can cut/paste in the cli or command window.

The new script that sets up VisIt for an interactive session is `setup_interactive.py`.  Before running, you need to comment out or modify the following.  
```
import sys
sys.path.append("/Users/lisalowe/visit-for-fvcom")
```
At least on my Mac, I need to define the python path so it can see 'setpaths'.  Probably I can do this before I'm in VisIt if I set the environment properly.   

From the terminal, run the 'setup_interactive.py' script.  Do not use 'cli' option, and put it in the background with `&`.
```
visit -s setup_interactive.py &
```

Everything is loaded according to the parameters that would have been used in a batch script.  You can use the GUI as usual, or cut/paste different plot into the cli.

Once the GUI opens, open the cli from VisIt:  Controls:Launch CLI

Options for plots:

Pseudocolor 3D Plot, shows 'birds eye view' of the whole lake:
```
create_pseudocolor_3Dplot(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA",MIN_TP,MAX_TP)
```

2D slice as percent of the y axis, currently with fixed slicing plane:
```
create_pseudocolor_2Dslice(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA",MIN_TP,MAX_TP)
```

2D transect, starts with the points defined in setparams:
```
create_pseudocolor_2Dtransect(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA",MIN_TP,MAX_TP,FROM_X,FROM_Y,TO_X,TO_Y)
```

To create a transect using different points from the GUI without starting over, just redefine the two points and redraw the transect.  First, delete the existing plot.
```
FROM_X = 561848.5
FROM_Y = 4756940.5
TO_X = 548466.63
TO_Y = 4793653.0
create_pseudocolor_2Dtransect(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA",MIN_TP,MAX_TP,FROM_X,FROM_Y,TO_X,TO_Y)
```

To layer a mesh over the plot, do
```
AddPlot("Mesh", "SigmaLayer_Mesh", 1, 1)
DrawPlots()
```

To make the 3D plot of the whole grid that shows the transect, do:
```
transect_against_3D(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA",MIN_TP,MAX_TP,FROM_X,FROM_Y,TO_X,TO_Y)
```

The script locks the time in view in the first plot, so each new cloned window will inherit the 'locked' propery.  To clone the window, do
```
CloneWindow()
DrawPlots()
```

To clone a window with the 3D mesh plus transect, and show it next to the 2D, do:
```
#The Mesh is the second plot
#(Python starts at zero)
SetActivePlots(1)
#Delete the mesh
DeleteActivePlots()
DrawPlots()
#Reset active plot
SetActivePlots(0)
#Slice attributes
SliceAtts = SliceAttributes()
#Project to 2D
SliceAtts.project2d = 1
SetOperatorOptions(SliceAtts, 2, 1)
#Zoom in on full extent
SetViewExtentsType(1)
```


To start from scratch, delete the existing plots:
```
DeleteAllPlots()
```
