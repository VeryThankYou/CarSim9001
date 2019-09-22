from model import Car

car1 = Car()

print(str(car1.theEngine) + " Maxrpm er lig med " + str(car1.theEngine.maxRpm))

for e in car1.theEngine.theGearbox.gears:
    print(str(e))

print(str(car1.theEngine.theTank) + " Tankens kapacitet er lig med " + str(car1.theEngine.theTank.capacity))

for e in car1.theEngine.theGearbox.wheels:
    print(str(e))
