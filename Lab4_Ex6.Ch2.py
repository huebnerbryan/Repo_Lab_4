#Name: Bryan Huebner
#Date: 22 October 2014
#Description: GIS_501/Lab4 - Solutions to challenge problems for exercise 6

#Challlenge problem 2

#import modules
import arcpy
from arcpy import env
#create a file geodatabase in ArcCatalog - import shapefiles
#set workspace path
env.workspace = "E:/Python/Data/Exercise06/Results/inp.gdb"
#define features_list
features_list = arcpy.ListFeatureClasses()

#create the new geodatabase
arcpy.CreateFileGDB_management("E:/Python/Data/Exercise06/Results", "FeaturesList.gdb")
for features in features_list:
    describe = arcpy.Describe(features)
    if describe.shapeType == "Polygon":
        arcpy.Copy_management (features, "E:/Python/Data/Exercise06/Results/FeaturesList.gdb/" + features)
    
 
