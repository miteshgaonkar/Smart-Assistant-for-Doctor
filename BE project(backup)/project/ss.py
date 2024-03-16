name = 'bob'

import pyttsx
Engine = pyttsx.init()
Engine.say("my name is",name)
Engine.runAndWait()