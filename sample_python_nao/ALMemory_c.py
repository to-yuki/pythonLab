class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.tts = ALProxy('ALTextToSpeech')
        self.motion = ALProxy('ALMotion')
        self.mem = ALProxy("ALMemory")

    def onLoad(self):
        pass

    def onUnload(self):
        pass

    def onInput_onStart(self):
        self.mem.insertData("Key1","NAO")
        self.log(self.mem.getData("Key1"))
        self.mem.removeData("Key1")

        self.log("PythonScript Run!")




    def onInput_onStop(self):
        self.onUnload() 
        self.onStopped()
