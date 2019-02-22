import arcpy,os,sys
import csv
from arcpy import env
#Assigning values to local variables
in_layer=r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb\General_Offense'
#Giving in the field names
field1='OffenseCustom'
field2='locationTranslation'
#Creating where clauses
whereClause = '"OffenseCustom"' + " = '" + 'BURGLARY FORCE' + "'"
whereClause1='"locationTranslation"' + " = '" + 'Residence/Home'+ "'"
#Initializing search cursor
with arcpy.da.SearchCursor(in_layer,(field1,),whereClause) as cur:
    for r in cur:
        with arcpy.da.SearchCursor(in_layer,(field2,),whereClause1) as cur1:
            for r1 in cur1:
#Creating  CSV file
                def tableToCSV(in_table,csv_path):
                    fld_list=arcpy.ListFields(in_table)
                    fld_names=[fld.name for fld in fld_list]
                    with open(csv_path, 'w') as csv_file:
                        writer = csv.writer(csv_file)
#Making the field names as headers
                        writer.writerow(fld_names)
                        with arcpy.da.SearchCursor(in_table, fld_names) as cursor:
                            for row in cursor:
                                writer.writerow(row)
                                print(csv_path)
                    csv_file.close()
                fc=r'C:\Users\prane\Desktop\610\Exercise 3.gdb\Exercise 3.gdb\GOSele'
                out_csv=r'C:\Users\prane\Desktop\610\GOSelection'
                tableToCSV(fc, out_csv)
        