# visit-for-fvcom
VisIt scripts for plotting data from FVCOM output files

Before running, do: 

cp setpaths.py.template setpaths.py

Then set the paths


Also before creating a movie with the outputs, do:

cp makemovie.csh.tempate makemovie.csh

Then copy to the directory where the images are (sorry, will change later), set the FFMEG parameters, and do:

source makemovie.csh


To open GUI from command line:
visit -cli -s scriptname.py

To run without window:
visit -cli -nowin -s scriptname.py

actually:
/full/path/to/visit -cli -nowin -s /path/to/visit-for-fvcom/scriptname.py

Or open visit or python and (Capital S is correct):
Source("scriptname.py")

Useful commands:
dir()
help()

ClearCache
Sometimes during extended VisIt runs, you might want to periodically clear the compute engine’s network cache to reduce the amount of memory being used by the compute engine

SetPipelineCachingMode
SetPipelineCachingMode(0) # Disable caching

Disabling caching is still grinding script to a halt.
