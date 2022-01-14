#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

def create_pseudocolor_plot(TITLE,UNITS,PLOT_VAR,MIN,MAX,FILE_TS):
    title.text = TITLE
    text2D_units.text = UNITS
    text2D_timestamp.text = timestamp
    AddPlot("Pseudocolor", PLOT_VAR, 1, 1)
    a = GetAnnotationObjectNames()
    legend = GetAnnotationObject(a[4])
    legend.drawTitle=0
    legend.managePosition=0
    legend.position = (0.055,0.85)
    legend.yScale = 1.0
    DrawPlots()
    SetActivePlots(0)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.colorTableName = "caleblack"
    PseudocolorAtts.min = MIN
    PseudocolorAtts.max = MAX
    SetPlotOptions(PseudocolorAtts)
    SaveWindowAtts.fileName = PLOT_VAR + "_" + FILE_TS
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
