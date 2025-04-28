import arcpy
import os
import datetime
from arcgis.gis import GIS
from time import strftime
 
date=strftime('%Y%m%d')
 
# Login
gis = GIS("pro")
 
# List of your AGOL hosted feature layer names:
backupFeatureNames_List = [
    "LayerName1",
    "LayerName2",
    "LayerName3",
]
 
# Corresponding list of each layers' Item ID as found on AGOL:
itemIDs_List = [
    "abcdefghjilmnopqrstuvwxyz1234567", #item ID for LayerName1
    "bcdefghjilmnopqrstuvwxyz12345678", #item ID for LayerName2
    "cdefghjilmnopqrstuvwxyz123456789" #item ID for LayerName3
]
 
# Import Variables
output = r"C:\Users\LeungM2\Desktop\DataBackupFolder" #where you want your data downloads to be saved
outputFolder = f"{output}\{date}"
os.makedirs(outputFolder)
print(outputFolder)
 
### Create Backup
n = len(itemIDs_List)
 
for x in range(n):
    itemID = itemIDs_List[x]
    backupFeatureName = backupFeatureNames_List[x]
    tempfile = strftime(backupFeatureName + '_%Y%m%d')
    dataitem = gis.content.get(itemID)
    dataitem.export(tempfile, 'File Geodatabase', parameters=None, wait=True)
    myexport = gis.content.search(tempfile, item_type='File Geodatabase')
    fgdb = gis.content.get(myexport[0].itemid)
    fgdb.download(save_path=outputFolder)
    print(backupFeatureNames_List[x], ": download is now complete")
 
 
