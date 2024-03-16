from tkinter import *
from gtts import gTTS
import os
import winsound


root = Tk()

tts = gTTS(text="This is the pc speaking", lang='en')
tts.save("pcvoice.mp3")
# to start the file from python
button1 = Button(Tk, text="Enter Program", command=winsound.PlaySound('pcvoice.mp3',winsound.SND_FILENAME))
button1.pack()