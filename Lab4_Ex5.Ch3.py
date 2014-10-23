#Name: Bryan Huebner
#Date: 22 October 2014
#Description: GIS_501/Lab4 - Solutions to challenge problems for exercise 5

#Challlenge problem 3

#import modules
import arcpy
from arcpy import env

#set workspace path
env.workspace = "C:/EsriPress/Python/Data/Exercise05"
env.overwriteOutput = True

#execute dissolve
arcpy.Dissolve_management("parks.shp", "C:/EsriPress/Python/Data/Exercise05/Results/parks_dissolved.shp", ["PARK_TYPE"], "", "SINGLE_PART", "")  


