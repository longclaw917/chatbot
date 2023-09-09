import googletrans
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import time
from time import sleep

translator = Translator()


def translategl(query):

     # r = sr.Recognizer()
     # with sr.Microphone() as source:
     #    print("listening..")
     #    r.phrase_threshold = 1
     #    r.energy_threshold = 300
     #    audio = r.listen(source)
     #    try:
     #        print("recognising..")
     #        query = r.recognize_google(audio, language='en-in')
     #        print(f"user said: {query}\n")
     #    except Exception as e:
     #        print("say that again")

        from main import speak
        speak("select the language boss")
        print(googletrans.LANGUAGES)
        b=str(input("select lang: "))
        results = translator.translate(query,b)
        print(results.text)

        # results = translator.translate(query,b)
        # print(results.text)
        voice = gTTS(results.text,lang=b)
        voice.save("voice.mp3")
        time.sleep(5)
        playsound("voice.mp3")
        time.sleep(3)
        os.remove("voice.mp3")

# print(googletrans.LANGUAGES)



translategl("ball")