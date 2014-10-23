#Name: Bryan Huebner
#Date: 22 October 2014
#Description: GIS_501/Lab4 - Solutions to challenge problems for exercise 7

#Challlenge problem 2

#import modules
import arcpy
from arcpy import env

#set workspace
env.workspace = "E:/Python/Data/Exercise07"

FeatureClass = "roads.shp"
ferry = "FERRY"

arcpy.AddField_management(FeatureClass, ferry, "TEXT", "", "", 20)
cursor = arcpy.da.UpdateCursor(FeatureClass, ["FEATURE", ferry])
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "Yes"
    else:
        row[1]= "NO"
    cursor.updateRow(row)
    
