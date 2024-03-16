import pyttsx3
voiceEngine = pyttsx3.init()

rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')

print(rate)
print(volume)
print(voice) 

newVoicerate = 50
while newVoicerate <= 300:
		voiceEngine.setProperty('rate', newVoicerate)
		voiceEngine.say('testing the vocie')
		voiceEngine.runAndWait()
		
		