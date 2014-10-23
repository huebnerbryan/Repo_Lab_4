#Name: Bryan Huebner
#Date: 22 October 2014
#Description: GIS_501/Lab4 - Solutions to challenge problems for exercise 7

#Challlenge problem 1

#import modules
import arcpy
from arcpy import env

#set workspace
env.workspace = "E:/Python/Data/Exercise07"
env.overwriteOutput = "True"

sql1 = " \"FEATURE\" = 'Airport'"
sql2 = " \"FEATURE\" = 'Seaplane Base'"
arcpy.Select_analysis ("airports.shp", "Results/airports_final.shp", sql1)
arcpy.Select_analysis ("airports.shp", "Results/seaports.shp", sql2)
arcpy.Buffer_analysis("Results/airports_final.shp", "Results/aiports_buffers.shp", "15000 METERS")
arcpy.Buffer_analysis("Results/seaports.shp", "Results/seaports_buffers.shp", "7500 METERS")
