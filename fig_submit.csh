#!/bin/tcsh
#BSUB -n 8
#BSUB -R span[hosts=1] 
#BSUB -W 2:00 
#BSUB -R select[avx]
#BSUB -J visit 
#BSUB -o stdout.%J
#BSUB -e stderr.%J
#module load gcc/9.2.0
#conda activate ./env_pre
#module load visit/3.2.2-mesa
module load visit/3.1.4-mesa
visit -cli -nowin -s script-paper-figures-black.py
