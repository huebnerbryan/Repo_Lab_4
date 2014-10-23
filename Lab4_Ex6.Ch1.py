#Name: Bryan Huebner
#Date: 22 October 2014
#Description: GIS_501/Lab4 - Solutions to challenge problems for exercise 6

#Challlenge problem 1

#import modules
import arcpy
from arcpy import env

#set workspace path
env.workspace = "E:/Python/Data/Exercise06"
env.overwriteOutput = True

featurelist = arcpy.ListFeatureClasses()
for features in featurelist:
    describe = arcpy.Describe(features)
    print describe.basename + " is a " + describe.shapeType
   
