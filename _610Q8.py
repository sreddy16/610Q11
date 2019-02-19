#Importing packages
import arcpy
#Giving the feature class path
fc = r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb\CallsforService'  
#Counting the number of records in the feature class
result = int(arcpy.GetCount_management(fc).getOutput(0))  
#Print result
print(result)  
