print("Jumping Calculator")
planets = ["Mercury", "Venus", "Earth", "Mars",  "Jupiter", "Saturn", "Uranus", "Neptune"]
real_gravity = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]
myJump = int(input("How much do you jump in meters?"))

myPlanet = input(f"Select a planet from list:{planets}")
EarthJump = input(f"Your Earth jump is:{myJump}")
planet_index = planets.index(myPlanet)
print(f"Your jump in {myPlanet} is {real_gravity[planet_index] * myJump} meters.") 

