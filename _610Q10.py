#Import system modules
import arcpy
#Set the parameters/local variables required for Spatial Join Analysis
target_features = r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb\General_Offense'
join_features = r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb\Tracts'
out_feature_class = r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb\JoinedFC'
#Running the spatial join analysis
arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
