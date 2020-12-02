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
		self.currentRotation = pyrr.quaternion.create_from_z_rotation(math.radians(z))
		print(self.currentRotation)
		
	def addTranslation(self, x = 0, y = 0, z = 0):
		vector = pyrr.vector3.create(x,y,z)
		rotatedVector = pyrr.quaternion.apply_to_vector(self.currentRotation, vector)
		translationMatrix = pyrr.matrix44.create_from_translation(rotatedVector)
		#print("translation matrix", translationMatrix)
		self.currentTransform = np.dot(translationMatrix, self.currentTransform)
		
