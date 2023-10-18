# Write a program to clear the clutter inside a folder on your computer. 
# You should use os module to rename all the .extension files from 1.extension 
# all the way till n.extension where n is the number of png files in that folder.
# Do the same for all the file formats.

import os
import glob

def get_most_recent_file(directory):
    list_of_files = glob.glob('*')  # this helps to find all the files and we can also use this with specifically extensions 
    a = list(list_of_files)
    return a

# Call the function to get the list of files
recent_files = get_most_recent_file('C:/Users/hp/OneDrive/Desktop/OS Module')

for i in range(0,len(recent_files)):
    os.rename(f"{recent_files[i]}",f"Day_{i+1}.pdf")



# import os

# # Define the base path
# base_path = "C:/Users/hp/OneDrive/Desktop/College Reports"

# # Create directories for each day
# for i in range(1, 2):
#     os.mkdir(f"{base_path}/Day_{i}")



