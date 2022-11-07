import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
 engine.say(audio) 
 engine.runAndWait() #Without this command, speech will not be audible to us.
 
 
def wishme():
 hour = int(datetime.datetime.now().hour)
 if hour>=0 and hour<=12:
     speak("Good Morning !")
 elif hour>=12 and hour<=18:
     speak("Good Afternoon !")
 elif hour>=18 and hour<=24:
     speak("Good Night !")
 else:
     speak("Good evening !")
     

def get_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1

        audio = rec.listen(source)

        try:
            print("Recognizing...")
            query = rec.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "None"

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query

if __name__=="__main__" :
    speak("Hello, it's me saangam AI model ,ask me anything Accoroding to wikipidia,for open google, for open youtube,for play music,my other functions are coming soon")
    wishme()
    while True:
    # if 1:
        query = get_command().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com") 
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "F:\\Python\\Jarvis"
            os.startfile(codePath)
            
        elif 'play music' in query:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[30]))    
         