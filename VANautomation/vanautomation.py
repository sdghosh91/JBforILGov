import os
import pandas as pd
import zipfile
from zipfile import ZipFile
import re
import time

# ------- extract .zip file ----------------------------------------------------
# select .zip file based on name

# set variables
exportTime = "6PM"
exportType = "tpexport"
year, month, day = time.strftime("%Y,%m,%d").split(',')
exportDate = year+month+day
fileName = exportTime + exportType + exportDate

path = r'C:\Users\Natalie Tham\Downloads'

# select .zip file based on exportTime, exportDate, exportType
# i is a file
#files = []
for i in os.listdir(path): # looks in path folder
    # if file starts with fileName + ends in .zip + is in path
    if os.path.isfile(os.path.join(path,i)) and i.endswith('.zip') and i.startswith(fileName):
        #print(i)
        j = os.path.join(path,i)
        #print(j)
        #print(os.path.abspath(i))
        #print(os.listdir(i))
        #os.chdir(os.path.join(path,i))
        #print(os.path.abspath(i))

        with zipfile.ZipFile(j,"r") as zip_ref:
            zip_ref.extractall(path)
            #os.rename(zip_ref,'thisfile')
        #files.append(i) # adds file i to list "files" if name convention is completed

for k in os.listdir(path):
    if os.path.isfile(os.path.join(path,k)) and k.endswith('.txt') and k.startswith(fileName):
        m = os.path.join(path,k) # this is the extracted file!
        print(os.path.abspath(m))
