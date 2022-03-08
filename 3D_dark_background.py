OpenDatabase("localhost:/Users/lisalowe/ORD/CURRENT_TEST/output.0/mi_0006.nc", 0)
AddPlot("Pseudocolor", "TP", 1, 1)
DrawPlots()
SetActivePlots(0)

#Set color min/max
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
PseudocolorAtts.minFlag = 1
PseudocolorAtts.min = 0.002
PseudocolorAtts.useBelowMinColor = 0
PseudocolorAtts.belowMinColor = (0, 0, 0, 255)
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = 0.01
PseudocolorAtts.useAboveMaxColor = 0
PseudocolorAtts.aboveMaxColor = (0, 0, 0, 255)
PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "Default"
PseudocolorAtts.invertColorTable = 0
SetPlotOptions(PseudocolorAtts)

#Transform operator, to see depth, scale z by 1000
AddOperator("Transform", 1)
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

#Add Box operator, hopefully to just the Active Plots
SetActivePlots((0, 1))
SetActivePlots(0)

AddOperator("Box", 0)
BoxAtts = BoxAttributes()
BoxAtts.amount = BoxAtts.Some  # Some, All
BoxAtts.minx = 548467
BoxAtts.maxx = 561848
BoxAtts.miny = 4.75694e+06
BoxAtts.maxy = 4.79365e+06
BoxAtts.minz = -250000
BoxAtts.maxz = 0
BoxAtts.inverse = 0
SetOperatorOptions(BoxAtts, 1, 0)
DrawPlots()


#Add slicing
AddOperator("Slice", 0)
SetActivePlots(0)
SliceAtts = SliceAttributes()
SliceAtts.originType = SliceAtts.Point  # Point, Intercept, Percent, Zone, Node
SliceAtts.originPoint = (561848, 4.75694e+06, 0)
SliceAtts.originIntercept = 0
SliceAtts.originPercent = 0
SliceAtts.originZone = 0
SliceAtts.originNode = 0
SliceAtts.normal = (-0.939531, -0.342463, 0)
SliceAtts.axisType = SliceAtts.Arbitrary  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
SliceAtts.upAxis = (0, 0, 1)
SliceAtts.project2d = 0
SliceAtts.interactive = 1
SliceAtts.flip = 0
SliceAtts.originZoneDomain = 0
SliceAtts.originNodeDomain = 0
SliceAtts.meshName = "Bathymetry_Mesh"
SliceAtts.theta = 0
SliceAtts.phi = 0
SetOperatorOptions(SliceAtts, 2, 0)
DrawPlots()

