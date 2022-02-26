Here you can cut/paste in the cli or command window.

At least on my Mac, I need to define the python path so it can see 'setpaths'.  Probably I can do this before I'm in VisIt.  Anyway:
```
import sys
sys.path.append("/Users/lisalowe/visit-for-fvcom")
```

Now run the 'setup_interactive.py' script.  Do not use 'cli' option, and put it in the background with `&`.
```
visit -s setup_interactive.py &
```

Everything is loaded.  You can use the GUI as usual, or cut/paste different plot into the cli.

Open the cli from VisIt:  Controls:Launch CLI

To start from scratch, delete the existing plots:
```
DeleteAllPlots()
```

Open the cli from VisIt:  Controls:Launch CLI

Options for plots:

Pseudocolor 3D Plot:
```
create_pseudocolor_3Dplot(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA",MIN_TP,MAX_TP)
```

2D slice as percent of the y axis:
```
create_pseudocolor_2Dslice(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA",MIN_TP,MAX_TP)
```

2D transect, starts with the points defined in setparams:
```
create_pseudocolor_2Dtransect(TITLE_TP_EPA,UNITS_TP_EPA,"TP_EPA",MIN_TP,MAX_TP,FROM_X,FROM_Y,TO_X,TO_Y)
```

To layer a mesh over the plot, do
```
AddPlot("Mesh", "SigmaLayer_Mesh", 1, 1)
DrawPlots()
```

The script locks the time in view in the first plot, so each new cloned window will inherit the 'locked' propery.  To clone the window, do
```
CloneWindow()
DrawPlots()
```

