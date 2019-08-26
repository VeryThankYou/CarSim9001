from random import randint

class Car(object):
	pass

class Wheel(object):
	pass

class Engine(object):
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
	pass

class Tank(object):
	pass

hej=Gearbox()

hej.shiftUp()
print(str(hej.currentGear))
