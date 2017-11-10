class MyClass(GeneratedClass):
	def __init__(self):
		GeneratedClass.__init__(self)
		self.tts = ALProxy("ALTextToSpeech")
		self.tts.setLanguage("Japanese")
		self.motion = ALProxy("ALMotion")
		self.mem = ALProxy("ALMemory")

	def onLoad(self):
		#put initialization code here
		pass

	def onUnload(self):
		#put clean-up code here
		pass

	def onInput_onStart(self):
		#self.onStopped() #activate the output of the box

		self.speek = self.mem.getData("WordRecognized")[0] # User SpeechReco

		self.motion.moveInit() # ポジションリセット
		if(self.speek == "前進"):
			self.motion.moveTo(0.3,0,0)
		elif(self.speek == "左向け"):
			self.motion.moveTo(0,0,1.5708)
		elif(self.speek == "右向け"):
			self.motion.moveTo(0,0,-1.5708)
		elif(self.speek == "右手上げる"):
			self.motion.setAngles(["RShoulderPitch","RShoulderRoll"], [-1.0,-0.3], 0.2)
		elif(self.speek == "左手上げる"):
			self.motion.setAngles(["LShoulderPitch","LShoulderRoll"], [-1.0,0.3], 0.2)            
		else:
			self.tts.say("その命令は実行できません")

		self.tts.say("次の命令をお願いします")

		self.log(self.speek)

		self.log("PythonScript Run!")

	def onInput_onStop(self):
		self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
		self.onStopped() #activate the output of the box
