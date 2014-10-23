#Name: Bryan Huebner
#Date: 22 October 2014
#Description: GIS_501/Lab4 - Solutions to challenge problems for exercise 5

#Challlenge problem 4

#import modules
import arcpy
from arcpy import env

#set workspace
env.workspace = "E:/GIS_501/Labs/Lab_4/Data"
env.overwriteOutput = True

#check for extensions
current_extensions = ["3D", "Network", "Spatial"]
for extension in current_extensions:
    if arcpy.CheckExtension(extension) == "Available":
        print "The requested extensions are accessible." 
    else:
        print "Request denied - Licensing required."
