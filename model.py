from random import randint
#Her importeres funktionen randint fra det eksterne bibliotek random

class Car(object):
#Her beskriver jeg klassen Car, der arver egenskaber fra object
	def __init__(self):
	#Her definerer jeg initieringsmetoden for klassen Car
		self.theEngine = Engine()
	#Jeg tilføjer en variabel der indeholder et objekt af klassen Engine
	
	def updateModel(self, dt):
	#Her definerer jeg updatemetoden for klassen Car. Den modtager parametret dt 
		self.theEngine.updateModel(dt)
	#Her kalder jeg metoden updateModel for det engine-objekt car-objektet indeholder, med parametret dt

class Wheel(object):
#Her beskriver jeg klassen Wheel, der arver egenskaber fra object

	def __init__(self):
	#Her definerer jeg initieringsmetoden for klassen Wheel
		self.orientation = randint(0, 360)
	#Her tilføjer jeg en variabel til klassen, som bliver sat til et tilfældigt tal mellem 0 og 360, inklusiv 0, eksklusiv 360
	
	def rotate(self, revolutions):
	#Her definerer jeg rotatemetoden for klassen Wheel. Den modtager parametret revolutions 
		self.orientation = (self.orientation+(revolutions*360))%360
	#Her bliver orientationsvariablen for objektet opdatereret, hvor der først lægges en mængde grader til variablen lig med 360 ganget med revolutions, og derefter findes modulus af det samlede tal, og variablen sættes til dette

class Engine(object):
#Her beskriver jeg klassen Engine, der arver egenskaber fra object

	def __init__(self):
	#Her definerer jeg initieringsmetoden for klassen Engine

		self.throttlePosition = 0
	#Her tilføjer jeg en variabel til klassen, som bliver sat til 0. Variablen beskriver speederens position
		self.theGearbox = Gearbox()
	#Jeg tilføjer en variabel der indeholder et objekt af klassen Gearbox
		self.currentRpm = 0
	#Her tilføjer jeg en variabel til klassen, som bliver sat til 0. Variablen beskriver rotationer per minut
		self.consumptionConstant = 0.0025
	#Her tilføjer jeg en variabel til klassen, som bliver sat til 0,0025. Variablen beskriver en konstant for hvor meget brændstof bilen forbruger
		self.maxRpm = 100
	#Her tilføjer jeg en variabel til klassen, som bliver sat til 100. Variablen beskriver en konstant for hvor mange rotationer per minut bilen maksimalt kan have
		self.theTank = Tank()
	#Jeg tilføjer en variabel der indeholder et objekt af klassen Tank

	def updateModel(self, dt):
	#Her definerer jeg updateModelmetoden for klassen Engine. Den modtager parametret dt 

		if self.theTank.contents > 0:
	#Her laver jeg en if-sætning, der tjekker om indholdet i tankens contentsvariabel er større end 0
			self.currentRpm = self.throttlePosition*self.maxRpm
	#hvis if-sætningen giver true, sætter jeg her self.currentRpm til self.throttleposition ganget med self.maxRpm
			self.theTank.remove(self.currentRpm*self.consumptionConstant)
	#Her kaldes tankens remove-metode med parametret self.currentRpm ganget med self.consumptionConstant
			self.theGearbox.rotate(self.currentRpm*(dt/60))
	#Her kaldes gearboksens rotate-metode med parametret self.currentRpm ganget med dt delt med 60
		else:
	#Her beskriver jeg hvad der sker hvis if-sætningen giver false
			self.currentRpm = 0
	#Variablen self.currentRpm sættes til 0

class Gearbox(object):
	def __init__(self):
		self.wheels = dict(frontLeft=Wheel(), frontRight=Wheel(), rearLeft=Wheel(), rearRight=Wheel())
		self.currentGear = 0
		self.clutchEngaged = False
		self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
		
	def shiftUp(self):
		if self.currentGear == (len(self.gears)-1) or self.clutchEngaged == True:
			pass
		else:
			self.currentGear += 1
	
	def shiftDown(self):
		if self.currentGear == 0 or self.clutchEngaged == True:
			pass
		else:
			self.currentGear -= 1
	
	def rotate(self, revolutions):
		if self.clutchEngaged == True:
			wheelRotations = revolutions*self.gears[self.currentGear]
			for e in self.wheels:
				self.wheels[e].rotate(wheelRotations)

class Tank(object):
	def __init__(self):
		self.capacity = 100
		self.contents = 100
		
	def remove(self, amount):
		if amount < self.contents:
			self.contents -= amount
		else:
			self.contents = 0
			
	def refuel(self):
		self.contents = self.capacity
		


