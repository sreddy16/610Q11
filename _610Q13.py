import os,sys,arcpy

from arcpy import env
env.overwriteOutput = True

current_dir = os.getcwd() 
fgdb_name = '610Q13'
workspace_path = current_dir + '\\' +fgdb_name

#create a gdb
arcpy.CreateFileGDB_management(current_dir, fgdb_name)

arcpy.env.workspace=r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb'
out_workspace=r'C:\Users\prane\source\repos\610Q13\610Q13\610Q13.gdb'

fc_list = arcpy.ListFeatureClasses()
 
# Execute CopyFeatures for each input shapefile
for shapefile in fc_list:
    # Determine the new output feature class path and name
    out_featureclass = os.path.join(out_workspace,os.path.splitext(shapefile)[0])
    arcpy.CopyFeatures_management(shapefile, out_featureclass)

in_features=r'C:\Users\prane\source\repos\610Q13\610Q13\610Q13.gdb\Tracts'
clip_features=r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb\MaricopaCounty'
out_features=r'C:\Users\prane\source\repos\610Q13\610Q13\610Q13.gdb\TractsSel'
xy_toler=''
arcpy.Clip_analysis(in_features,clip_features,out_features,xy_toler)
