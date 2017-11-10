class MyClass(GeneratedClass):
	def __init__(self):
		GeneratedClass.__init__(self)
		self.tts = ALProxy('ALTextToSpeech')
		self.motion = motion = ALProxy("ALMotion")

	def onLoad(self):
		pass

	def onUnload(self):
		pass

    def onInput_onStart(self):
		self.motion.moveInit()
		self.motion.moveTo(0.5,0,0)
		self.motion.setAngles(["RShoulderPitch", "RShoulderRoll"], [-1.0, -0.3], 0.1)
		self.tts.say("Walking!")
		self.log("PythonScript Run!")

	def onInput_onStop(self):
		self.onUnload()
		self.onStopped()
