print("Event: Cangrejeros Basketball Game")
print("Cost of seats: Courtside = 183, Arena Lateral first Aile = 160, Arena Lateral Second Aile = 150")
Courtside = int(input("How many tickets bought Courtside?"))
ArenaLateralfrirstAile = int(input("How many tickests bought Arena Lateral first Aile?"))
ArenaLateralsecondAile = int(input("How many tickets bought Arena Lateral second Aile?"))

def SectionSales(Courtside, ArenaLatealfirstAile, ArenaLatralsecondAile):
    print(f"Cost of Courtside Tickets are: {int(Courtside) * 183}")
print(f"Cost of Arena Lateral first Aile  Tickets are:  {int(ArenaLateralfrirstAile) * 160}")
print(f"Cost of Arena Lateral second Aile  Tickets are: {int(ArenaLateralsecondAile) * 150}")
print()
SectionSales(Courtside, ArenaLateralfrirstAile, ArenaLateralsecondAile)
Sales_cs = Courtside * 183
Sales_alfa = ArenaLateralfrirstAile * 160
Sales_alsa =ArenaLateralsecondAile * 150
def TicketsTotal(Sales_cs, Sales_alfa, Sales_alsa):
    print(f"The total of tickets sales is: {int(Sales_cs) + int(Sales_alfa) + int(Sales_alsa)}")
print()
TicketsTotal(Sales_cs, Sales_alfa, Sales_alsa)
