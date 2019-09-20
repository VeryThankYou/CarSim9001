from random import randint

#Definerer klassen Car, der nedarver fra object 
class Car(object):
    def __init__(self): # Metoden __init__(self) kører altid når klassen instancieres 
        self.theEngine = Engine() #Definerer instansvariablen theEngine til at være klassen Engine()

    def updateModel(self, dt): #Metoden der kører instansvariablen theEngine's updateModel metode.
        self.theEngine.updateModel(dt) 

#Definerer klassen Wheel, der nedarver fra object 
class Wheel(object):
    def __init__(self):
        self.orientation = randint(0,360) #Definerer instansvariablen orientation til at være en random int mellem 0 og 360, hvor 0 er inklusiv og 360 er exklusiv

    def rotate(self, revolutions): #Metoden der beregner (int) orientation ved at lægge revolutions gange 360 til orientation. Derefter findes modulo af resultatet iforhold til 360.
        self.orientation = (self.orientation + revolutions * 360) % 360

#Definerer klassen Engine ,der nedarver fra object 
class Engine(object):
    def __init__(self):
        self.throttlePosition = 0 #Definerer instansvariablen throttlePosition til at være (int) 0
        self.theGearbox = Gearbox() #Definerer instansvariablen theGearbox til at være klassen Gearbox()
        self.currentRpm = 0 #Definerer instansvariablen currentRpm til at være (int) 0
        self.consumptionConstant = 0.0025 #Definerer instansvariablen consumptionConstant til at være (float) 0.0025
        self.maxRpm = 100 #Definerer instansvariablen maxRpm til at være (int) 100
        self.theTank = Tank() #Definerer instansvariablen theTank til at være klassen Tank()

    def updateModel(self, dt):
        if(self.theTank.contents > 0): #Checker om instansvariablen theTank.contents er mere end 0
            self.currentRpm = self.throttlePosition * self.maxRpm #Beregner currentRpm ved at gange throttlePosition med maxRpm
            self.theTank.remove(self.currentRpm*self.consumptionConstant) #Kalder theTank's remove metode, med currentRpm gange consumptionConstant som parameter
            self.theGearbox.rotate(self.currentRpm*(dt/60)) #Kalder theGearbox's rotate metode, med currentRpm gange med dt divideret med 60 som parameter
        else: 
            self.currentRpm = 0 #Sætter currentRpm til (int) 0

#Definerer klassen Gearbox, der nedarver fra object 
class Gearbox(object):
    def __init__(self):
        self.wheels =  {'frontLeft':Wheel(),'frontRight':Wheel(), 'rearLeft':Wheel(),'rearRight':Wheel()} #Erklærer instansvariablen wheels som er typen dictionary
        self.currentGear = 0 #Erklærer instansvariablen currentGear som er typen int 
        self.clutchEngaged = False #Erklærer instansvariablen clutchEngaged som er typen boolean
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8] #Erklærer instansvariablen gears som er typen list

    def shiftUp(self):
        if(self.currentGear < len(self.gears) and self.clutchEngaged != True):
            self.currentGear += 1 # lægger 1 til integeren currentGear hvis antallet af elementer i listen gears er mindre end integeren currentGear og booleanen clutchEngaged er True

    def shiftDown(self):
        if(self.currentGear != 0 and self.clutchEngaged != True):
            self.currentGear -= 1 # Trækker 1 fra integeren currentGear hvis integeren currenGear ikke er 0 og booleanen clutchEngaged er True
    
    def rotate(self, revolutions):
        if(self.clutchEngaged == True): # Checker om booleanen clutchEngaged er True  
            for wheel in self.wheels: # For-løkke som kalder rotate metoden på hver instans af Wheel i (dict) wheels
                self.wheels[wheel].rotate(revolutions * self.gears[self.currentGear])

#Definerer klassen Tank, der nedarver fra object 
class Tank(object):
    def __init__(self):
        self.capacity = 100 # Erklærer instansvariablen capacity som er typen int
        self.contents = 100 # Erklærer instansvariablen contents som er typen int

    def remove(self, amount): #Metode der modtager self og amount som parameter
        if(self.contents > 0): # Checker om contents er større end 0
            self.contents -= amount # Trækker amount fra contents

    def refuel(self): #Metode som tilhører klassen Tank
        self.contents = self.capacity #Sætter (int) contents til at være (int) capacity
