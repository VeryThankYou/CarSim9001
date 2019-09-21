from random import randint
#Her importeres funktionen randint fra det eksterne bibliotek random

class Car(object):
#Her beskriver jeg klassen Car, der arver egenskaber fra object
	def __init__(self):
	#Her definerer jeg initieringsmetoden for klassen Car
		self.theEngine = Engine()
	#Jeg tilf�jer en variabel der indeholder et objekt af klassen Engine

	def updateModel(self, dt):
	#Her definerer jeg updatemetoden for klassen Car. Den modtager parametret dt
		self.theEngine.updateModel(dt)
	#Her kalder jeg metoden updateModel for det engine-objekt car-objektet indeholder, med parametret dt

class Wheel(object):
#Her beskriver jeg klassen Wheel, der arver egenskaber fra object

	def __init__(self):
	#Her definerer jeg initieringsmetoden for klassen Wheel
		self.orientation = randint(0, 360)
	#Her tilf�jer jeg en variabel til klassen, som bliver sat til et tilf�ldigt tal mellem 0 og 360, inklusiv 0, eksklusiv 360

	def rotate(self, revolutions):
	#Her definerer jeg rotatemetoden for klassen Wheel. Den modtager parametret revolutions
		self.orientation = (self.orientation+(revolutions*360))%360
	#Her bliver orientationsvariablen for objektet opdatereret, hvor der f�rst l�gges en m�ngde grader til variablen lig med 360 ganget med revolutions, og derefter findes modulus for 360 af det samlede tal, og variablen s�ttes til dette

class Engine(object):
#Her beskriver jeg klassen Engine, der arver egenskaber fra object

	def __init__(self):
	#Her definerer jeg initieringsmetoden for klassen Engine

		self.throttlePosition = 0
	#Her tilf�jer jeg en variabel til klassen, som bliver sat til 0. Variablen beskriver speederens position
		self.theGearbox = Gearbox()
	#Jeg tilf�jer en variabel der indeholder et objekt af klassen Gearbox
		self.currentRpm = 0
	#Her tilf�jer jeg en variabel til klassen, som bliver sat til 0. Variablen beskriver rotationer per minut
		self.consumptionConstant = 0.0025
	#Her tilf�jer jeg en variabel til klassen, som bliver sat til 0,0025. Variablen beskriver en konstant for hvor meget br�ndstof bilen forbruger
		self.maxRpm = 100
	#Her tilf�jer jeg en variabel til klassen, som bliver sat til 100. Variablen beskriver en konstant for hvor mange rotationer per minut bilen maksimalt kan have
		self.theTank = Tank()
	#Jeg tilf�jer en variabel der indeholder et objekt af klassen Tank

	def updateModel(self, dt):
	#Her definerer jeg updateModelmetoden for klassen Engine. Den modtager parametret dt

		if self.theTank.contents > 0:
	#Her laver jeg en if-s�tning, der tjekker om indholdet i tankens contentsvariabel er st�rre end 0
			self.currentRpm = self.throttlePosition*self.maxRpm
	#hvis if-s�tningen giver true, s�tter jeg her self.currentRpm til self.throttleposition ganget med self.maxRpm
			self.theTank.remove(self.currentRpm*self.consumptionConstant)
	#Her kaldes tankens remove-metode med parametret self.currentRpm ganget med self.consumptionConstant
			self.theGearbox.rotate(self.currentRpm*(dt/60))
	#Her kaldes gearboksens rotate-metode med parametret self.currentRpm ganget med dt delt med 60
		else:
	#Her beskriver jeg hvad der sker hvis if-s�tningen giver false
			self.currentRpm = 0
	#Variablen self.currentRpm s�ttes til 0

class Gearbox(object):
#Her beskriver jeg klassen Gearbox, der arver egenskaber fra object

	def __init__(self):
	#Her definerer jeg initieringsmetoden for klassen Gearbox

		self.wheels = dict(frontLeft=Wheel(), frontRight=Wheel(), rearLeft=Wheel(), rearRight=Wheel())
	#Jeg tilf�jer en variabel der indeholder et dictionary der indeholder 4 keys der hver bliver koblet til et Wheel-objekt
		self.currentGear = 0
	#Her tilf�jer jeg en variabel til klassen, som bliver sat til 0. Variablen beskriver hvilket gear bilen er i

		self.clutchEngaged = False
	#Her tilf�jer jeg en variabel til klassen, som bliver sat til False. Variablen beskriver om koblingen er slået til eller fra

		self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
	#Her tilf�jer jeg en variabel til klassen,indeholder en liste med tal. Tallene beskriver gearkonstanten for de 5 gear plus frigear


	def shiftUp(self):
	#Her definerer jeg shiftUp-metoden for klassen Gearbox

		if self.currentGear == (len(self.gears)-1) or self.clutchEngaged == True:
	#Her laver jeg en if-sætning der tjekker om koblingen er slået til, eller om man er i det højeste gear
			pass
	#Her beskriver jeg at der ikke skal ske noget hvis if-sætningen giver True
		else:
	#Her beskriver jeg hvad der ellers skal ske
			self.currentGear += 1
	#Her lægges 1 til det nuværende gear

	def shiftDown(self):
	#Her definerer jeg shiftDown-metoden for klassen Gearbox

		if self.currentGear == 0 or self.clutchEngaged == True:
	#Her laver jeg en if-sætning der tjekker om koblingen er slået til, eller om man er i frigear
			pass
	#Her beskriver jeg at der ikke skal ske noget hvis if-sætningen giver True
		else:
	#Her beskriver jeg hvad der ellers skal ske
			self.currentGear -= 1
	#Her trækkes der 1 fra det nuværende gear


	def rotate(self, revolutions):
	#Her definerer jeg rotate-metoden for klassen Gearbox. Metoden modtager parametret revolutions
		if self.clutchEngaged == True:
	#Her laver jeg en if-sætning der tjekker om koblingen er slået til
			wheelRotations = revolutions*self.gears[self.currentGear]
	#Her udregner jeg hvor meget hjulene skal rotere ved at gange revolutions med gearkonstanten for det nuværende gear
			for e in self.wheels:
	#Her laver jeg en for-løkke, der kører en gang for hvert element i listen self.wheels
				self.wheels[e].rotate(wheelRotations)
	#Her kalder jeg rotate-metoden der hører til objektet Wheel, på et af hjulene i self.wheels, med parametret wheelRotations, som var hvor meget hvert hjul skulle rotere

class Tank(object):
#Her beskriver jeg klassen Tank, der arver egenskaber fra object

	def __init__(self):
	#Her definerer jeg initieringsmetoden for klassen Tank
		self.capacity = 100
	#Her tilf�jer jeg en variabel til klassen, som bliver sat til 100. Variablen beskriver hvor stor kapacitet tanken har
		self.contents = 100
	#Her tilf�jer jeg en variabel til klassen, som bliver sat til 100. Variablen beskriver hvor meget brændstof der er i tanken

	def remove(self, amount):
	#Her definerer jeg remove-metoden for klassen Tank. Metoden modtager parametret amount
		if amount < self.contents:
	#Her laver jeg en if-sætning der tjekker om inputet amount er mindre end indholdet i tanken
			self.contents -= amount
	#Hvis if-sætningen er sand trækker jeg her amount fra indholdet i tanken
		else:
	#Her beskriver jeg hvad der ellers skal ske
			self.contents = 0
	#Her sættes tankens indhold til 0

	def refuel(self):
	#Her definerer jeg refuel-metoden for klassen Tank
		self.contents = self.capacity
	#Her sætter jeg tankens indhold til tankens kapacitet
