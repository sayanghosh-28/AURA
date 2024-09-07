import struct
import time
from playsound import playsound
import eel
import os

import pyaudio 
from backend.command import speak
from backend.config import ASSISTANT_NAME 
import pywhatkit as kit
import re
import mysql.connector as sqltor
import webbrowser

from backend.helper import extract_yt_term


mycon=sqltor.connect(host="localhost",user="root",passwd="sayan2801",database='sayan')
cursor=mycon.cursor()


@eel.expose
def playassitantsound():
    music_dir="D:\\hp\\pycharmprojects\\Aura\\frontend\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
def opencommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            print("hello")
            cursor.execute(
                'SELECT path FROM commands WHERE name = %s', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT path FROM web_commands WHERE name = %s', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except Exception as e:
            speak("Something went wrong: " + str(e))
        
def playyoutube(query):
    search_item=extract_yt_term(query)
    speak("playing "+search_item+" on youtube")
    kit.playonyt(search_item)
    
def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=porcupine.create(keywords=["siri","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("k")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
