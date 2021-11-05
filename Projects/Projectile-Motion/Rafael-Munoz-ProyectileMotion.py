# gun = "M700 Bolt action Sniper"
# caliber = "7.62 x 51mm NATO"
# ammunition = "M61"
# velocity_ms = "826"

# Building = "Soleil"
# Building_Height = 288

# gravity_ms = 9.81

import math
def ProjectileFunction(experimentalData: ExperimentalData):
    time_s = math.sqrt((2 * experimentalData.Building_Height) / experimentalData.gravity_ms)

    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)
    print(f"The gun selected for the expirament is {experimentalData.gun}. The caliber of {experimentalData.gun} is {experimentalData.caliber} and the ammunition is {experimentalData.ammunition}. The {experimentalData.gun} is {experimentalData.velocity_ms} fast, and i will be at the {experimentalData.Building} building, which is {experimentalData.Building_Height} tall.")

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
experimentalData = ExperimetnalData("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M61", 826, "Soleil", 288, 9.81)

ProjectileFunction