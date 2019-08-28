from random import randint

class Car(object):
	def __init__(self):
		self.theEngine = Engine()
	
	def updateModel(self, dt):
		self.theEngine.updateModel(dt)
	pass

class Wheel(object):
	def __init__(self):
		self.orientation = randint(0, 360)
	
	def rotate(self, revolutions):
		self.orientation = (self.orientation + int(revolutions)*360) %360
	pass

class Engine(object):
	def __init__(self):
		self.throttlePosition = 0
		self.theGearbox = Gearbox()
		self.currentRpm = 0
		self.consumptionConstant = 0.0025
		self.maxRpm = 100
		self.theTank = Tank()
		
	def updateModel(self, dt):
		if self.theTank.capacity > 0:
			self.currentRpm = self.throttlePosition*self.maxRpm
			self.theTank.remove(self.currentRpm*self.consumptionConstant)
			self.theGearbox.rotate(self.currentRpm*(dt/60))
		else:
			currentRpm = 0
	pass

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
			wheelRotations = int(revolutions)*self.gears[self.currentGear]
			for e in self.wheels:
				self.wheels[e].rotate(wheelRotations)
	pass

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
		
	pass


