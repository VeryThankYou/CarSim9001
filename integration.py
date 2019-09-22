from model import Car

print("Her testes hvilke dele bilen består af:\n")
car1 = Car()
#Kravspecifikation 1.a
print(str(car1.theEngine) + " Maxrpm er lig med " + str(car1.theEngine.maxRpm))

#Kravspecifikation 1.b
for e in car1.theEngine.theGearbox.gears:
    print(str(e))

#Kravspecifikation 1.c
print(str(car1.theEngine.theTank) + " Tankens kapacitet er lig med " + str(car1.theEngine.theTank.capacity))

#Kravspecifikation 1.d
for e in car1.theEngine.theGearbox.wheels:
    print(str(e))

print("\n\nHer testes funktionerne:\n")
car2 = Car()
#Kravspecifikation 2.a
car2.theEngine.throttlePosition = 0.5
car2.theEngine.theGearbox.currentGear = 2
car2.theEngine.theGearbox.clutchEngaged = True
print(car2.theEngine.theGearbox.wheels["frontLeft"].orientation)
car2.updateModel(1)
print(car2.theEngine.theGearbox.wheels["frontLeft"].orientation)

#Kravspecifikation 2.b
car2.theEngine.throttlePosition = 0
car2.updateModel(1)
print(str(car2.theEngine.currentRpm))
car2.theEngine.throttlePosition = 0.2
car2.updateModel(1)
print(str(car2.theEngine.currentRpm))
car2.theEngine.throttlePosition = 0.5
car2.updateModel(1)
print(str(car2.theEngine.currentRpm))
car2.theEngine.throttlePosition = 0.7
car2.updateModel(1)
print(str(car2.theEngine.currentRpm))
car2.theEngine.throttlePosition = 1
car2.updateModel(1)
print(str(car2.theEngine.currentRpm))
#Kravspecifikation 2.b.tank
car2.theEngine.theTank.refuel()
car2.theEngine.throttlePosition = 1
print(str(car2.theEngine.theTank.contents))
car2.updateModel(0.6)
print(str(car2.theEngine.theTank.contents))

#Kravspecifikation 2.c
car2.theEngine.theGearbox.clutchEngaged = True
print("\n" + str(car2.theEngine.theGearbox.currentGear))
car2.theEngine.theGearbox.shiftUp()
print(str(car2.theEngine.theGearbox.currentGear))
car2.theEngine.theGearbox.clutchEngaged = False
car2.theEngine.theGearbox.shiftUp()
print(str(car2.theEngine.theGearbox.currentGear))

#Kravspecifikation 2.d
print("\n" + str(car2.theEngine.theTank.contents))
car2.theEngine.theTank.refuel()
print(str(car2.theEngine.theTank.contents))

#Kravspecifikation 2.e
car2.theEngine.throttlePosition = 0.5
car2.theEngine.theGearbox.currentGear = 2
car2.theEngine.theGearbox.clutchEngaged = True
print("\n" + str(car2.theEngine.theGearbox.wheels["frontLeft"].orientation))
print(str(car2.theEngine.theGearbox.wheels["frontRight"].orientation))
print(str(car2.theEngine.theGearbox.wheels["rearLeft"].orientation))
print(str(car2.theEngine.theGearbox.wheels["rearRight"].orientation))
car2.updateModel(1)
print("\n" + str(car2.theEngine.theGearbox.wheels["frontLeft"].orientation))
print(str(car2.theEngine.theGearbox.wheels["frontRight"].orientation))
print(str(car2.theEngine.theGearbox.wheels["rearLeft"].orientation))
print(str(car2.theEngine.theGearbox.wheels["rearRight"].orientation))

print("\n\nHer testes bilens starttilstand:\n")
car3 = Car()
#Kravspecifikation 3.a
print(str(car3.theEngine.throttlePosition))

#Kravspecifikation 3.b
print(str(car3.theEngine.theGearbox.clutchEngaged))
print(str(car3.theEngine.theGearbox.currentGear))

#Kravspecifikation 3.c
print(str(car3.theEngine.theTank.capacity) + " " + str(car3.theEngine.theTank.contents))

#Kravspecifikation 3.d
for e in car3.theEngine.theGearbox.wheels:
    print(str(car3.theEngine.theGearbox.wheels[e].orientation))
