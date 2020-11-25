import struct
import sys

isPython3 = sys.version_info.major == 3

class MouseInput:

	def __init__(self):
		self.mouseFile = open( "/dev/input/mice", "rb" );
		self.callback = None

	def getMouseDelta(self):
		buf = self.mouseFile.read(3);
		#button = buf[0] if isPython3 else ord(buf[0]));
		x,y = struct.unpack( "bb", buf[1:] );

		if (self.callback != None):
			self.callback(x, y)

	def addCallback(self, callbackMethod):
		self.callback = callbackMethod		

	def poll(self):
		while( 1 ):
			self.getMouseDelta();

	def clean(self):
		self.mouseFile.close();

if __name__=="__main__":

	m = MouseMovement();
	print(isPython3)
	
	if isPython3:
		callback = eval("print")
	else:
		def callback(x, y):
			print (x, y)

	m.addCallback(callback)
	m.poll();

