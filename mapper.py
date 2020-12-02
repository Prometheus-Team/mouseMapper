from input import MouseInput
from tracker import MouseTracker


class MouseMapper:

	def __init__(self):
		self.mouseInput = MouseInput()
		self.mouseTracker = MouseTracker()
		self.mouseInput.addCallback(self.mouseInputCallback)

	def setGetRotationMethod(self, method):
		self.mouseTracker.setGetRotationMethod(method)

	def run(self):
		self.mouseInput.poll()

	def mouseInputCallback(self, x, y):
		self.mouseTracker.registerMovement(x, y)


if __name__=="__main__":

	m = MouseMapper()
	#set the method that returns rotation in degrees
	m.setGetRotationMethod(lambda : 90)
	m.run()
