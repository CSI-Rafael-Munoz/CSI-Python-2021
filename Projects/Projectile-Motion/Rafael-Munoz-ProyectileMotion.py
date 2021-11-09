import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json

# gun = "M700 Bolt action Sniper"
# caliber = "7.62 x 51mm NATO"
# ammunition = "M61"
# velocity_ms = "826"

# Building = "Soleil"
# Building_Height = 288

# gravity_ms = 9.81

def ProjectileFunction(experimentalData: ExperimentalData):
    time_s = math.sqrt((2 * experimentalData.Building_Height) / experimentalData.gravity_ms)

    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)
    print(f"The gun selected for the experiment is {experimentalData.gun}. The caliber of {experimentalData.gun} is {experimentalData.caliber} and the ammunition is {experimentalData.ammunition}. The {experimentalData.gun} is {experimentalData.velocity_ms} fast, and i will be at the {experimentalData.Building} building, which is {experimentalData.Building_Height} tall, and it will reach {experimentalData.distance_m} in {experimentalData.time_s}.")

#Convert your script parameters into a single JSON object

# experimentalData = { 
#     "gun" : "M700 Bolt action Sniper",
#  "caliber" : "7.62 x 51mm NATO",
#  "ammunition" :"M61",
#  "velocity_ms" : 826,
#  "Building" : "Soleil",
#  "Building_Height" : 288,
#  "gravity_ms" : 9.81

# }
experimentalData = ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M61", 826, "Soleil", 288, 9.81)

myDataSet = [
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M61", 826, "Soleil", 288, 9.81),
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M62", 816, "Soleil", 288, 9.81),
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M80", 833, "Soleil", 288, 9.81),
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M993", 910, "Soleil", 288, 9.81),    
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "Ultra Nosler", 822, "Soleil", 288, 9.81),
]

for data in myDataSet:
    print("\n---------------------------------------------------------------------\n")
    ProjectileFunction(data)

#Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "Proyectile-Motion.json")

print(myOutputFilePath)

with open(myOutputFilePath, "w") as outfile:
    json.dump([data.__dict__for data in myDataSet], outfile)