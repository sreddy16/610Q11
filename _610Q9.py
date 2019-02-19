#Import system modules
import arcpy
 
#Set environment settings
arcpy.env.workspace = r'C:\Users\prane\source\repos\610Pranks\610Pranks\output.gdb'

 
#Set local variables
inFeatures = 'CapitalCities'
fieldName1 = 'AddField'
fieldAlias = 'addedfield'
 
#Execute AddField for the new field
arcpy.AddField_management(inFeatures, fieldName1, field_alias=fieldAlias, field_is_nullable="NULLABLE")


#Adding a coded domain to the field with 5 values
arcpy.CreateDomain_management(arcpy.env.workspace, 'Domain1', 'firstdomain', 'SHORT', 'CODED', 'DUPLICATE', 'DEFAULT')
arcpy.AddCodedValueToDomain_management(arcpy.env.workspace, 'Domain1', 0, 'firstvalue')
arcpy.AddCodedValueToDomain_management(arcpy.env.workspace, 'Domain1', 1, 'secondvalue')
arcpy.AddCodedValueToDomain_management(arcpy.env.workspace, 'Domain1', 2, 'thirdvalue')
arcpy.AddCodedValueToDomain_management(arcpy.env.workspace, 'Domain1', 3, 'fourthvalue')
arcpy.AddCodedValueToDomain_management(arcpy.env.workspace, 'Domain1', 4, 'fifthvalue')

        
print('Done adding Domains')