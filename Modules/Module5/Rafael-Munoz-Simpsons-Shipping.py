print("Welcome to Simpsons Shipping")
weight:float = float(input("What is the weight of your package:"))

#ground shipping
if (weight == 2 or weight < 2):
    cost_ground = weight * 1.75 + 20
    print("Ground Shippiing: $", float(cost_ground))
elif (weight == 2 or weight <6):
    cost_ground = weight * 3.50 + 20
    print ("Ground Shipping: $", float(cost_ground))
elif (weight == 6 or weight < 10):
    cost_ground = weight * 4.50 + 20
    print ("Ground Shipping: $", float(cost_ground))
else:
    cost_ground = weight * 5.25 + 20
    print("Ground Shipping: $", float(cost_ground))

#courrier shipping
if (weight == 2 or weight < 2):
    cost_ground = weight * 3.50 + 20
    print("Courrier Shippiing: $", float(cost_ground))
elif (weight == 2 or weight <6):
    cost_ground = weight * 7.00 + 20
    print ("Courrier Shipping: $", float(cost_ground))
elif (weight == 6 or weight < 10):
    cost_ground = weight * 9.00 + 20
    print ("Courrier Shipping: $", float(cost_ground))
else:
    cost_ground = weight * 10.50 + 20
    print("Courrier Shipping: $", float(cost_ground))

#drone shipping
if (weight == 2 or weight < 2):
    cost_ground = weight * 5.25 + 20
    print("Drone Shippiing: $", float(cost_ground))
elif (weight == 2 or weight <6):
    cost_ground = weight * 10.50 + 20
    print ("Drone Shipping: $", float(cost_ground))
elif (weight == 6 or weight < 10):
    cost_ground = weight * 13.50 + 20
    print ("Drone Shipping: $", float(cost_ground))
else:
    cost_ground = weight * 15.75 + 20
    print("Drone Shipping: $", float(cost_ground))

#ground shipping premium charge
print("If you have premium your charge is: $150")
