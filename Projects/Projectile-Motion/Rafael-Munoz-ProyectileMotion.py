# gun = "M700 Bolt action Sniper"
# caliber = "7.62 x 51mm NATO"
# ammunition = "M61"
# velocity_ms = "826"

# Building = "Soleil"
# Building_Height = 288

# gravity_ms = 9.81

import math
def ProjectileFunction(gun:str, caliber:str, ammunition:str, velocity_ms:int, Building:str, Building_Height:int, gravity_ms:int):
    time_s = math.sqrt((2 * Building_Height) / gravity_ms)
    distance_m = (velocity_ms * time_s)
    print(f"The gun selected for the expirament is {gun}. The caliber of {gun} is {caliber} and the ammunition is {ammunition}. The {gun} is {velocity_ms} fast, and i will be at the {Building} building, which is {Building_Height} tall.")

ProjectileFunction("M700 Bolt action Sniper", "7.62 x 51mm NATO", "M61", 826, "Soleil", 288, 9.81)