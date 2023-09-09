import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import webbrowser
import os
from bs4 import BeautifulSoup
from time import sleep
from datetime import timedelta
from datetime import datetime
import pyautogui
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# print(voices[0])
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.phrase_threshold = 1
        audio = r.listen(source)
    try:
        print("recognising..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again")
        return "none"
    return query


def usearch():
    speak("what do you want from here, boss")
    if 1:
        query = takecommand().lower()
        if "pause the video" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "start the video" in query:
            pyautogui.press("k")
            speak("video played")
        elif "mute it" in query:
            pyautogui.press("m")
            speak("video muted")
        elif "increase volume" in query:
            speak("Turning volume up,sir")
            def volumeup():
                for i in range(5):
                    keyboard.press(Key.media_volume_up)
                    keyboard.release(Key.media_volume_up)
                    sleep(0.1)
            volumeup()
        elif "decrease volume" in query:
            speak("Turning volume down, sir")
            def volumedown():
                for i in range(5):
                    keyboard.press(Key.media_volume_down)
                    keyboard.release(Key.media_volume_down)
                    sleep(0.1)
            volumedown()
        else:
            msg = takecommand().lower()
            Actual_thing = msg.replace("play", "")
            Actual_thing = msg.replace("give me a video of", "")
            Actual_thing = msg.replace("find me a video of", "")
            speak("playing" + Actual_thing)
            pywhatkit.playonyt(Actual_thing)
