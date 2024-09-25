import pyttsx3
import speech_recognition as sr
import eel
import time
import openai
import os

from backend.helper import extract_yt_term

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',120)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
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
def all_command(message=1):
    
    if message==1:
        query= takecommand()
        print(f"Command received from speech: '{query}'")
        eel.senderText(query)
    else:
        query=message
        print(f"Command received from speech: '{query}'")
        eel.senderText(query)
    try:
        print(f"Command received from speech: '{query}'")
        #if "open" in query:
        if query.startswith("open"):
            print("open")
            from backend.features import opencommand
            opencommand(query)
        elif query.startswith("play"):
        #elif extract_yt_term(query):
            #print("youtube")
            from backend.features import playyoutube
            try:
                playyoutube(query)
            except Exception as e:
                print(f"Error :{e}")
                from backend.untitled import google_search
                response=google_search(query)
                print(f"Google search response: {response}")
                speak(response)
                #eel.DisplayMessage(response)

                #opencommand(query)
                #google_search(query)
        else:
            print("Processing with AI...")
            #from backend.features import opencommand
            #opencommand(query)
            from backend.untitled import google_search
            #google_search(query)
            response = google_search(query)  # Get response from ChatGPT
            print(f"Google search response: {response}")
            speak(response)

    except Exception as e:
        print(f"An error occurred: {e}")  # Print out the actual error message for debugging
        speak("Something went wrong while connecting to the AI service.")
        
    eel.ShowHood()




#text=takecommand()
    
#speak(text)