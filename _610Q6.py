#Importing packages
import arcpy,sys,os
#Setting up the work environment
arcpy.env.workspace=r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb'
#Initializing the characteristics of the field
shapefile='CallsforService'
field_name='Crime_Explanation'
field_type='text'
arcpy.AddField_management(shapefile,field_name,"TEXT")
feature_class=r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb\CallsforService'
#Adding a field
field_names=['CFSType','Crime_Explanation']
#Updating field values in the new field based on an older field
with arcpy.da.UpdateCursor(feature_class,field_names) as cur:
    for row in cur:
        if row[0]==('Burglary Call'):
            row[1]='This is burglary'
            cur.updateRow(row)
        else:
            row[1]='This is not a burglary'
            cur.updateRow(row)
print('Row is updated')


