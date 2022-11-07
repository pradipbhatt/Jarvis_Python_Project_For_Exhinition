#This program is for text to voice command using Python.
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)
engine.setProperty('rate', 150)
# engine.say("Hello, How are you ?")
engine.runAndWait()

def speak(str):
    engine.say(str)
    engine.runAndWait()

speak("Hello, What's going on there yogesh is there alright  I am going to show you that how you can convert Text to Speech in Python using the pyttsx or pyttsx3 module. Both the modules have same syntax so you can use any of them without confusion. Install the module in your PC using the command 'pip install pyttsx' or 'pip install pyttsx3', and the plus point here is that it works offline...?   ")