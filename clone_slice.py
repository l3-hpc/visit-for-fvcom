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
