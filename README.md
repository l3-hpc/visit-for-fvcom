# visit-for-fvcom
VisIt scripts for plotting data from FVCOM output files

# Getting the code
Instructions are on the [GitHub README](https://github.com/l3-hpc/visit-for-fvcom#readme), or in the README.md after cloning the repo.  To clone the repo, from Linux/Mac terminal or Windows git bash, do
```
git clone https://github.com/l3-hpc/visit-for-fvcom
cd visit-for-fvcom
```

In that directory, there is a file **.gitignore**.  Files listed there will be ignored by git.  It includes files that are likely to change between users, like setpaths.py, and also files that may be created in the directory but should not be saved, such as core files and SLURM/LSF output.

# Modify the paths
The paths to the input files and output directories are defined in the file **setpaths.py**.

The file **setpaths.py** will be different for each user, and for each user will be different from PC to HPC.  So that git does not track your changes to the file, a template **setpaths.py.template** is included in this git repo.  Copy the template.
```
cp setpaths.py.template setpaths.py
```
Modify the following in **setpaths.py**:
```
EPA_directory
MARK_directory
IMGS_DIR
```
If the netCDF files do not begin with "mi_", then change that as well:
```
file_prefix_epa
file_prefix_mark
```
Note, if **IMGS_DIR** does not already exist, it will be created.  Also, any existing files will be overwritten.  Do not modify any lines below the file declarations.

# Run the code
Sample submission scripts were created for Henry2 and atmos.  Before modifying, make a local copy.  For example,
```
cp submit.csh.atmos submit.csh
```
or
```
cp submit.csh.henry2 submit.csh
```

After copying, modify submit.csh to change the wall clock time and, for atmos, the run directory, which is the directory from where you submit the job.  To submit the job, on atmos, use 
```
sbatch submit.sh
```
and for Henry2, use
```
bsub < submit.sh
```



## Some notes 

Even though these made nice plots on my Mac, the ones on Henry2 were huge.  That has to do with the save window settings.  (I assume the same will happen on atmos.  So I need to fix that.)

# Updating your git repo to the newest version (pull)

If you are just using the code, to get new changes, do:
```
git pull
```

Note, since setpaths.py is in the gitignore, it will not notice this necessary addition!  But if setpaths.py.template has changed, you may need to modify your setpaths.py.  Best practice is to do this after doing a new 'git pull'
```
diff setpaths.py setpaths.py.template
```

If you created files in that directory, it will give an error.  If you need those files, but don't need those files in that directory, you can move them.  If they are junk files that you don't need at all, you can use 'git stash', and it will remove anything that changed since you last did 'clone' or 'pull'.  If you expect to aways make those same named files in that directory, add the name of the file (or directory) to the .gitignore.

To check if the changes you have are actually important, you can check what exactly was changed by doing
```
git status
git diff
```

To develop the code, we need to...
[Add Instructions for Fetch and Merge here!]

# Running the codes

The codes that call VisIt are **make_all.py** and **make_slices.py**.  The sample batch scripts are included for Henry2 and atmos, and they contain:
```
visit -cli -nowin -s make_all.py
visit -cli -nowin -s make_slices.py
```

As is, those scripts assume you have all 13 mi files, and they loop through and make a plot of the first timestep in each mi plot.  If you uncomment the 'break' statement, they will do every timestep.

After you run those scripts, set the environment for Python 3 by whichever module.  A YAML file is provided for folks who want to make a Conda environment themselves.  So far, the Python scripts use libraries that are available with any Python 3 module on atmos.

After loading the module or activating the Conda environment, do:
```
python multiplot.py
python multiplot_slices.py
```

Those will take the separate image files and contatenate them.  The script **multiplot.py** puts 4 PNGs in a 2x2 layout,  and **multiplot_slices.py** puts 4 images in a single row.

On a Mac from command line, I can look at images with `open`.  On Henry2, with `display`.  On atmos...(let me know and I'll put it in the documenation).



To open GUI from command line:
```
visit -cli -s scriptname.py
```
To run without window:
```
visit -cli -nowin -s scriptname.py
```
Or open visit or python and (Capital S is correct):
```
Source("scriptname.py")
```

Useful commands in the VisIt command shell:
```
dir()
help()
ClearCache
a = GetAnnotationAttributes()
print(a)
```

Sometimes during extended VisIt runs, you might want to periodically clear the compute engine’s network cache to reduce the amount of memory being used by the compute engine
```
SetPipelineCachingMode
SetPipelineCachingMode(0) # Disable caching
```

Disabling caching is still grinding script to a halt on the Mac while on Linux it is fine.  I suspect a memory leak.

YAML file to create a Conda environment for multiplots.py:
```
name: fvcom
channels:
  - conda-forge
dependencies:
 - matplotlib
 - numpy
```

To create the environment:
```
conda env create --prefix /[your_path]/env_fvcom -f fvcom.yml
```

To use
```
conda activate /[your_path]/env_fvcom
```
Then run multiplot.py:
```
python multiplot.py
```

### VisIt links
- [VisIt - Home](https://visit-dav.github.io/visit-website/index.html)
- [VisIt GUI Manual](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/gui_manual/index.html)
- [VisIt Python (CLI) Manual](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/cli_manual/index.html)

### Other links
- [GitHub markdown syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Vim and Python syntax](https://wiki.python.org/moin/Vim)
