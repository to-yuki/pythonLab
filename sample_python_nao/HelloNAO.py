# -*- encoding: UTF-8 -*-
from naoqi import ALProxy

naoip = "12.0.0.1"
naoport = 9559

tts = ALProxy("ALTextToSpeech", naoip, naoport)
tts.setLanguage("Japanese")
tts.say("こんにちは") 
