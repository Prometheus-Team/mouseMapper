import math
import pyrr
import numpy as np

class MouseTracker:

	SCALE = 1

	def __init__(self):

		self.origin = (0,0,0)
		self.currentRotation = pyrr.quaternion.create_from_z_rotation(0)
		self.currentTransform = pyrr.matrix44.create_from_translation(self.origin)
		self.getRotationMethod = None

	def getLocation(self):
		return pyrr.vector3.create_from_matrix44_translation(self.currentTransform)

	def getRotation(self):
		return pyrr.quaternion.rotation_angle(self.currentRotation)

	def setGetRotationMethod(self, getRotationMethod):
		self.getRotationMethod = getRotationMethod

	def registerMovement(self, x, y):
		rotation = self.getRotationMethod()
		self.setRotation(rotation)
		print("Adding", x, y)
		self.addTranslation(x, y)
		print("Location is now", self.getLocation())

	def setRotation(self, z):
		self.currentRotation = pyrr.quaternion.create_from_z_rotation(z)
		
	def addTranslation(self, x = 0, y = 0, z = 0):
		translationMatrix = pyrr.matrix44.create_from_translation((x,y,z))
		print("translation matrix", translationMatrix)
		offsetMatrix = np.dot(translationMatrix, pyrr.matrix44.create_from_quaternion(self.currentRotation))
		print("offset matrix", offsetMatrix)
		self.currentTransform = np.dot(offsetMatrix, self.currentTransform)
		
