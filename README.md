# visit-for-fvcom
VisIt scripts for plotting data from FVCOM output files

# Getting the code
Instructions are on the website, or in the README.md after cloning the repo.  To clone the repo, from Linux/Mac terminal or Windows git bash, do
```
git clone https://github.com/l3-hpc/visit-for-fvcom
cd visit-for-fvcom
```

In that directory, there is a file **.gitignore**.  Files listed there will be ignored by git.  I have added files that are likely to change between users, like setpaths.py, and also files that may be created in the directory but should not be saved, such as core files and SLURM/LSF output.

# Modify the paths
The files setpaths.py will be different for each user, and for each user will be different from PC to HPC.  Once you create the personal setpaths file, it will not be accidentally modified when updating (git pull/merge) the code.
```
cp setpaths.py.template setpaths.py
```
Then open setpaths.py with a text editor and set the proper paths for the input (mi files) and output (images).  If a directory **IMG_DIR** does not exist, create one:
```
mkdir /path/to/IMG_DIR
```   
If **IMG_DIR** does not already exist, the code will run without any error messages, and it will appear to be making plots, but they are being written in the ether.


## BEWARE!!!  There is no error checking! (yet)

ALSO even though these made nice plots on my Mac, the ones on Henry2 were huge.  That has to do with the save window settings.  I assume the same will happen on atmos.  So I need to fix that.

#General stuff about using github...

If you are just using the code, to get new changes, do:

git pull

If you created files in that directory, it will give an error.  If you need those files, but don't need those files in that directory, you can move them.  If they are junk files that you don't need at all, you can use 'git stash', and it will remove anything that changed since you last did 'clone' or 'pull'.  If you expect to aways make those same named files in that directory, add the name of the file (or directory) to the .gitignore.

To check if the changes you have are actually important, you can check what exactly was changed by doing
```
git status
git diff
```

To develop the code, we need to...
[Add Instructions for Fetch and Merge here!]


#Instructions assuming you already have the code, already set the paths, created the image directory, and just want to use the latest stuff...

Do 'git pull', and see above if you have errors.  

Note, since setpaths.py is in the gitignore, it will not notice this necessary addition!  (Although it is added in setpaths.py.template.)  Best practice is to do this when doing a new 'git pull'

diff setpaths.py setpaths.py.template

Add this to your setpaths.py (copy and paste from the setpaths.py.template in case the format of the README is messed up.)

def set_image_path():
    return IMGS_DIR


The codes that call VisIt are make_all.py and make_slices.py.  The sample batch scripts are included for Henry2 and atmos, and they contain:
visit -cli -nowin -s make_all.py
visit -cli -nowin -s make_slices.py

As is, those scripts assume you have all 13 mi files, and they loop through and make a plot of the first timestep in each mi plot.  If you uncomment the 'break' statement, they will do every timestep.

After you run those scripts, set the environment for Python 3 by whichever module.  I make a YAML file for folks who want to make a conda environment themselves.  So far, the Python scripts use libraries that I think are in any Python 3 module on atmos.

After loading the module or activating the conda, do:

python multiplot.py

python multiplot_slices.py

Those will take the separate image files and contatenate them.  multiplot.py puts 4 PNGs in a 2x2 layout.  multiplot_slices.py puts 4 images in a single row.

On a Mac from command line, I can look at images with 'open'.  On Henry2, with 'display'.  On atmos...(let me know and I'll put it in the documenation).



To open GUI from command line:

visit -cli -s scriptname.py

To run without window:

visit -cli -nowin -s scriptname.py

Or open visit or python and (Capital S is correct):

Source("scriptname.py")

Useful commands:

dir()

help()

ClearCache

Sometimes during extended VisIt runs, you might want to periodically clear the compute engine’s network cache to reduce the amount of memory being used by the compute engine

SetPipelineCachingMode

SetPipelineCachingMode(0) # Disable caching

Disabling caching is still grinding script to a halt on the Mac

a = GetAnnotationAttributes()

print(a)


Conda environment for multiplots.py:

name: fvcom

channels:

  - conda-forge

dependencies:

 - matplotlib

 - numpy

conda env create --prefix /[your_path]/env_fvcom -f fvcom.yml

To use

conda activate /[your_path]/env_fvcom

Then run multiplot.py:

python multiplot.py

First change the IMGS_DIR.  

VisIt CLI Manual

https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/cli_manual/index.html
