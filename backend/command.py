import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',120)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    
def takecommand():
    a= sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        a.pause_threshold = 1
        a.adjust_for_ambient_noise(source)
        
        audio=a.listen(source,10,6)
        
    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')

        query=a.recognize_google(audio,language='en-in')
        print(f"User said : {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
  
    except Exception as e:
        return ""
    return query.lower()

@eel.expose
def all_command():
    try:
        query= takecommand()
        print(query)
        if "open" in query:
            from backend.features import opencommand
            opencommand(query)
        elif "on youtube":
            from backend.features import playyoutube
            playyoutube(query)
        else:
            print("not run")
    except:
        print("error")
        
    eel.ShowHood()

#text=takecommand()
    
#speak(text)