# visit-for-fvcom
VisIt scripts for plotting data from FVCOM output files

# Getting the code
Instructions are on the [GitHub README](https://github.com/l3-hpc/visit-for-fvcom#readme), or in the README.md after cloning the repo.  To clone the repo, from Linux/Mac terminal or Windows git bash (and set your HOME directory to the new cloned repo) do:
```
git clone https://github.com/l3-hpc/visit-for-fvcom
cd visit-for-fvcom
```

In that directory, there is a file **.gitignore**.  Files listed there will be ignored by git.  It includes files that are likely to change between users, like setpaths.py, and also files that may be created in the directory but should not be saved, such as core files and SLURM/LSF output.

# Modify the paths
The paths to the input files and output directories are defined in the file **setpaths.py**.

The file **setpaths.py** will be different for each user, and for each user will be different from PC to HPC.  To avoid having git track changes to all of our filepaths, a template **setpaths.py.template** is included in this git repo.  

## Current setpaths.py for some systems 
For the current setpaths.py with path definitions for atmos, Henry2, and others, see **Current sample setpaths.py** on [How to use VisIt](https://sites.google.com/ncsu.edu/lllowe/ord/visit/visit-faq).

## Modify your own setpaths.py
Copy the template and modify **setpaths.py**. The file **setpaths.py** is listed in the **.gitignore** and it will not be tracked or overwritten with new pulls.
```
cp setpaths.py.template setpaths.py
```
Modify the following in **setpaths.py** to point to the appropriate directory paths:
```
EPA_directory
COMPARE_directory
IMGS_DIR
```
If your netCDF files do not begin with **mi_**, then change these as well:
```
file_prefix_epa
file_prefix_compare
```
Note, if **IMGS_DIR** does not already exist, it will be created.  Also, any existing files in the **IMGS_DIR** will be overwritten.  

Do not modify any lines below the file declarations.

# Set plot parameters
Set the parameters for various plots in file **setparams.py**.  The commenting is decent, but there is no error checking.

The images are named after the type of plot and the time/date stamp and **RUN_NAME**, defined in **setpaths.py**, is appended.  If you rerun the script for a different transect or colormap, etc., the old plots will be overwritten if you do not choose a different **RUN_NAME**.  You may alternatively or additionally change the name of **IMGS_DIR** before a new run. 

# Print plot parameters
To print the paths and parameters for basic error checking, run ##test_params.py##, which prints the value and type of each function.  When adding variables to the code, please add them here as well.
```
python test_params.py
``` 

# Run the scripts in a batch job on HPC  
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
sbatch submit.csh
```
and for Henry2, use
```
bsub < submit.csh
```
You can check the status of the batch job by
```
squeue -u <username> 
```

# Updating your git repo to the newest version (pull)

If you are just using and not modifying the code, to get new changes, do:
```
git pull
```

Note, since setpaths.py is in the gitignore, it will not notice if there were changes made.  If setpaths.py.template has changed, you may need to modify your setpaths.py.  Best practice is to do this after doing a new `git pull`.
```
diff setpaths.py setpaths.py.template
```

If you changed or created files in that directory since you last got the code, it will give an error message on trying to `git pull`.  
 - If you added files to the directory, and need those files but don't need them specifically in that directory, you should move them.
 - If they are junk files, you can remove them or do `git stash`, which will remove anything that changed since you last did `git clone` or `git pull`.  If you expect to aways make those same named files in that directory, add the name of the file (or directory) to the **.gitignore**.
 - If you made changes and what to keep them, then you need to do fetch and merge.  Instructions for Fetch and Merge will be added later. 

To check if the changes you have are actually important, you can check what exactly was changed by doing
```
git status
git diff
```

# Running the codes interactively from a GUI

## On HPC

### Run the VisIt scripts
The code that calls VisIt is **plot_any.py**.  To run interactively, start an interactive session, load the visit module, and type the commands which are listed in the submit scripts but remove the 'nowin' argument:
```
[On HPC, start interactive session]
[On HPC, module load the visit module via 'module load visit']
visit -cli -s plot_any.py
```
For HPC, X11 forwarding is enabled with MobaXterm by default.  If using a Mac, you may need to use 'ssh -X' and XQuartz.  On Henry2, use the HPC-VCL.  


# Run the post-processing Python scripts
After the images were created by VisIt, run the Python scripts.  First, set the environment for Python 3 by loading an appropriate module or activating a Conda environment. For example:
```
module load intelpython3
```
A YAML file is provided for folks who want to make a Conda environment themselves.  So far, the Python scripts use libraries that are available with any Python 3 module on atmos.

After loading the module or activating the Conda environment, run the Python script by typing:
```
python multiplot.py
```
Ideally, if you are on an HPC, do the command in a batch script or interactive session.

The script simply take multiple image files and contatenate them into a single image, i.e. 4 PNGs in a 2x2 layout.

The script takes the info from **setpaths.py** and **setparams.py** to create the image names.  As is, they work if you are doing a comparison run and have the output from the first timestep in each of the 13 mi_*.nc files.

On a Mac from command line, I can look at images with `open`.  On Henry2, with `display`.  On atmos use 'display' to open Image Magick and navigate to the file you want to open(you may need to click on the window that opens to have the menu window pop up). Or navigate to the directory with the images on atmos and open from there.


# Useful commands in the VisIt command shell:
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

# Create your own Conda environment
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


### Additional Notes and ToDos: 

Even though these made nice plots on my Mac, the ones on Henry2 were huge.  I think that has to do with the save window settings.  (I assume the same will happen on atmos.  So I need to fix that.)

