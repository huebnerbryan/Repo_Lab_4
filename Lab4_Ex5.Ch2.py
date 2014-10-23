#Name: Bryan Huebner
#Date: 22 October 2014
#Description: GIS_501/Lab4 - Solutions to challenge problems for exercise 5

#Challenge problem 2

#import modules
import arcpy
from arcpy import env
#set environment
env.workspace = "C:/EsriPress/Python/Data/Exercise05"
env.overwriteOutput = True

#set variables
in_data = "hospitals.shp"
in_features = "hospitals_XYpts.shp"

#Copy original dataset
arcpy.Copy_management("hospitals.shp", "hospitals_XYpts.shp")

#execute AddXY
arcpy.AddXY_management("hospitals_XYpts.shp") 


