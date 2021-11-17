import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json
#we are calling everything we need for the program to run
# gun = "M700 Bolt action Sniper"
# caliber = "7.62 x 51mm NATO"
# ammunition = "M61"
# velocity_ms = "826"

# Building = "Soleil"
# Building_Height = 288

# gravity_ms = 9.81
#Here we are defining the experimental data and making a list of the planets to be used in the program
def ProjectileFunction(experimentalData: ExperimentalData):
    planets = ["Mercury", "Venus", "Earth", "Mars",  "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87,9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planets= planets.index(experimentalData.planet)
    time_s = math.sqrt((2 * experimentalData.Building_Height) / g_ms2[planets])


    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)
    #Here we are calling the variables and describing their use
    print(f"The gun selected for the experiment is {experimentalData.gun}. The caliber of {experimentalData.gun} is {experimentalData.caliber} and the ammunition is {experimentalData.ammunition}. The {experimentalData.gun} is {experimentalData.velocity_ms} fast, and i will be at the {experimentalData.Building} building, which is {experimentalData.Building_Height} tall, and it will reach {distance_m} in {time_s}.")
    print(f"The experiment is carried out in {experimentalData.planet} with a gravity of {g_ms2[planets]}")

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
#Here we are having the descriptions of the guns with the planets
experimentalData = ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M61", 826, "Soleil", 288, 9.81)

myDataSet = [
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M61", 826, "Soleil", 288, "Earth"),
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M62", 816, "Soleil", 288, "Mars"),
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M80", 833, "Soleil", 288, "Venus"),
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M993", 910, "Soleil", 288, "Saturn"),    
ExperimentalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "Ultra Nosler", 822, "Soleil", 288, "Mercury"),
]
#Here we are making a separation in the outprint in each data set
for data in myDataSet:
    print("\n---------------------------------------------------------------------\n")
    ProjectileFunction(data)

#Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "Proyectile-Motion.json")
#Here we are printing the output fil
print(myOutputFilePath)

with open(myOutputFilePath, "w") as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)

    #Deserialization
deserialize = open(myOutputFilePath)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("\n--------------------------------------------------------------------\n")
    ProjectileFunction(ExperimentalData(**e))
        #projectileFunction(expiramentalData)