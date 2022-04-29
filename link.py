#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os
import sys  

index = 0
with open("layer2files.txt",'r') as data_file:
    for line in data_file:
        data = line.split('.')
        original_file = line.strip()
        linked_file = data[0] + "." + str(index).zfill(4) + ".png"
        linking_string = "ln -s ../MakeTPMovies/" + original_file + " " + linked_file
        #linking_string = "ln ../" + original_file + " " + linked_file
        os.system(linking_string)
        #print(linking_string)
        index+=1
