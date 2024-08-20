import arcpy
import os
import datetime
from arcgis.gis import GIS

from time import strftime
print(strftime('%c'))

backupFeatureNames_List = [
    # 60715329 SUG Photostations 20240410
    "SUG_Photostations_20240410"
]

# Set the workspace/Import Variables
itemIDs_List = [
    # 60715329 SUG Photostations 20240410
    "11a47133ed7047f88b9846df8e23ef6a"
]

backupFeatureNames_List = [
    # 60715329 SUG Natural Resources (Point) 20240410
    "Natural_Resources_Point_20240410",
    # 60715329 SUG Natural Resources (Polygon) 2024010
    "Natural_Resources_Polygon_20240410",
    # 60715329 SUG Constraints Natural Resources Points
    "Natural_Resources_Points", 
    # 60715329 SUG Constraints Natural Resources Polygons
    "Natural_Resources_Polygons", 
    # 60715329 SUG Wetlands JD
    "SUG_Wetlands_JD", 
    # 60715329 SUG ESAs
    "SUG_ESAs", 
    # 60715329 SUG Access Notes
    "SUG_Access_Notes", 
    # 60715329 SUG Project Design Constraints
    "SUG_Project_Design_Constraints",
    # 60715329 SUG Constraints Aquatic Resources Lines
    "Aquatic_Resources_Lines",     
    # 60715329 SUG Constraints Aquatic Resources Points
    "Aquatic_Resources_Points",
    # 60715329 SUG Constraints Aquatic Resources Polygon
    "Aquatic_Resources_Polygon",
    # 60715629 SUG PTE
    "PTE",
    # 60715329 SUG Aquatic Resources 20240410
    "Aquatic_Resources_20240410",
    # 60715329 SUG ESAs 20240410
    "SUG_ESAs_20240410",
    # 60715329 SUG Wetlands JD 20240410
    "SUG_Wetlands_JD_20240410",
    # 60715329 SUG Project Design Constraints (Not for GPS Data Collection) 20240425
    "SUG_Project_Design_Constraints_20240425",
    # 60715329 SUG Access Notes 20240410
    "SUG_Access_Notes_20240410",
    # 60715329 SUG Map Notes (for PDF Maps) 20240410
    "SUG_Map_Notes_20240410",
    # 60715329 SUG Photostations 20240410
    "SUG_Photostations_20240410"
]

# Set the workspace/Import Variables
itemIDs_List = [
    # 60715329 SUG Natural Resources (Point) 20240410
    "8ab4bdb1dc934cad9daf000a9ab98452",
    # 60715329 SUG Natural Resources (Polygon) 2024010
    "4b2a0e338f664f44b97e924c2f859c4e",
    # 60715329 SUG Constraints Natural Resources Points
    "1ca8bd72ab11459495363e3eff011258", 
    # 60715329 SUG Constraints Natural Resources Polygons
    "a3011c0e887d45908a805f50f1365b5b", 
    # 60715329 SUG Wetlands JD
    "66905f5bf02f452dad2120fd9dd6a7cb", 
    # 60715329 SUG ESAs
    "ea5545d2c9b04227a2801e1ab0f85ac8", 
    # 60715329 SUG Access Notes
    "dc251ea6146e415ba1fc6763b6dc74fb", 
    # 60715329 SUG Project Design Constraints
    "0e8944bfe52d468ab1852c1e607d4962",
    # 60715329 SUG Constraints Aquatic Resources Lines
    "5d706fbc4bf84af9b8d7d00937665f3c", 
    # 60715329 SUG Constraints Aquatic Resources Points
    "253f1b15806848d7b5804788ac589fe1",
    # 60715329 SUG Constraints Aquatic Resources Polygon
    "1046d698f7c347d68442a04d99ac95ce",
    # 60715329 SUG PTE
    "8db67c23b1a341d3a68001a8660b0bdc",
    # 60715329 SUG Aquatic Resources 20240410
    "001b0d0050b54bbeb74e18ee9556ffee",
    # 60715329 SUG ESAs 20240410
    "484bf652a4c7475e8c2983af2de6cf27",
   # 60715329 SUG Wetlands JD 20240410
    "9e2c5aa0a1d4442aa6fac9413ab9bbbe",
    # 60715329 SUG Project Design Constraints (Not for GPS Data Collection) 20240425
    "03339f0f67414834935f256182ff9836",
    # 60715329 SUG Access Notes 20240410
    "3d22e28d449b42749eb4732b89f708cc",
    # 60715329 SUG Map Notes (for PDF Maps) 20240410
    "8f6089d788b44ea2b50332b3582a3863",
    # 60715329 SUG Photostations 20240410
    "11a47133ed7047f88b9846df8e23ef6a"
]

# Login
gis = GIS("pro")

# Import Variables
output = r'\\na.aecomnet.com\lfs\AMER\SanDiego-USSDG1\DCS\GIS\Projects\_SUG\01_Data\__Archive\Project Data Backup'

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
    fgdb.download(save_path=output)
    print(backupFeatureNames_List[x], ": download is now complete")
