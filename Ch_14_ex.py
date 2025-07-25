import os
import dbm
"""
List of exercises to finish: 
    Page 140 - print names of files in directory and subdirectories
    Page 144 - import your own module
    End of chapter 3 exercises

"""

try:
    fin = open('bad_file')
except: 
    print('Something went wrong.')