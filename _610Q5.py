#Import packages
import os
import sys
import arcpy

from arcpy import env
#Set overwrite output to true
env.overwriteOutput = True


#Set the directory, geodatabase name and path
current_dir = os.getcwd() 
fgdb_name = 'output.gdb'
workspace_path = current_dir + '\\' +fgdb_name
    


#create a gdb
arcpy.CreateFileGDB_management(current_dir, fgdb_name)

#Creating a feature class list
featureList= ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities','Rivers']

#Creating feature classes from the elements in the list
for fc_name in featureList:
    arcpy.CreateFeatureclass_management(out_path=workspace_path, out_name=fc_name)

