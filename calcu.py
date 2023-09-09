import wolframalpha
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# print(voices[0])
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wolframalpha(query):
    apikey = "W5L3U7-A3WP8X9WRJ"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("this is not anserable")

def calc(query):
    term = str(query)
    term = term.replace("nova","")
    term = term.replace("multiply by","*")
    term = term.replace("plus","+")
    term = term.replace("divide by","/")
    term = term.replace("minus","-")

    final = str(term)
    try:
        result = Wolframalpha(final)
        print(f"{result}")
        speak(result)
    except:
        speak("value is not answerable")


