import pyttsx3
import speech_recognition as sr
from requests import get
import wikipedia
import webbrowser
import pyautogui
import requests
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
from time import sleep
import pywhatkit
import speedtest
from datetime import date
import datetime

keyboard = Controller()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# print(voices[0])
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.phrase_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source)
    try:
        print("recognising..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning,boss")
    elif 12 <= hour <= 18:
        speak("Good afternoon,boss")
    else:
        speak("Good evening,boss")
    speak("fail here, how can i help you ")


# for i in range(3):
#     a = takecommand().lower()
#     pw_file = open("code.txt","r")
#     pw = pw_file.read()
#     pw_file.close()
#     if a==pw:
#         speak("wake me up boss")
#         break
#     elif i ==2 and a!=pw:
#         exit()
#     elif a!=pw:
#         speak("try again")


if __name__ == '__main__':

    while True:
        # if 1:

        query = takecommand().lower()

        # logic
        if "wake up" in query or "fail" in query or "hi,fail" in query or "hello fail" in query:
            wish()
            while True:
                query = takecommand().lower()
                if "go to sleep" in query:
                    speak("ok boss")
                    break
                elif "introduce yourself" in query or "tell me something about yourself" in query:
                    query = query.replace("fail", "")

                    speak("Hello, I am Dj's first attempt in learning, AKA Fail, an AI that functions as Dj's assistant, "
                          "running 24 hours of day 7 days of week, taking care of some of the internal systems "
                          " of this laptop,In short, i am a natural-language user "
                          "interface, created by Dj to operate his laptop, And,I am "
                          "an inspiration from JARVIS of MCU ")


                elif "ip address" in query:
                    ip = get('https://api.ipify.org').text
                    print(ip)
                    speak(f"your IP address is {ip}")
                elif "launch" in query:
                    from dictapp import openappweb

                    openappweb(query)
                elif "close" in query:
                    speak("closing it boss!!")
                    query = query.replace("close", "")
                    query = query.replace("tabs", "tab")
                    from dictapp import closeappweb

                    closeappweb(query)


                elif "wikipedia" in query:
                    speak("onto it boss")
                    query = query.replace("wikipedia", "")
                    # query = query.replace("who is","")
                    # query = query.replace("what is","")
                    # query = query.replace("which are","")
                    results = wikipedia.summary(query, sentences=2)
                    print(results)
                    speak(results)
                elif "open youtube" in query:
                    speak("onto it boss")
                    webbrowser.open("www.youtube.com")
                    speak("what do you want from here, boss")
                    msg = takecommand().lower()
                    if msg == "none":
                        msg = None
                    else:
                        msg = msg.replace("play", "")
                        msg = msg.replace("give me a video of", "")
                        msg = msg.replace("find me a video of", "")
                        speak("playing" + msg)
                        pywhatkit.playonyt(msg)

                elif "open stackoverflow" in query:
                    speak("onto it boss")
                    webbrowser.open("www.stackoverflow.com")
                elif "open google" in query or "let's search" in query:

                    speak("what should i search boss")
                    look = takecommand().lower()
                    look = look.replace("search", "")
                    look = look.replace("find me", "")
                    look = look.replace("fetch", "")
                    pywhatkit.search(f"{look}")
                    speak("this is what i found boss")


                elif "send message" in query or "send a message" in query or "open whats app" in query:
                    from whatsapp import sendmsg

                    sendmsg()
                elif "tell me the temperature" in query or "current temperature" in query:
                    url = "https://www.google.com/search?q=local+temperature+now"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"local temperature is , {temp}")
                elif "tell me the time" in query:
                    strtime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the time is {strtime}")
                elif "stop the video" in query:
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

                elif "internet speed" in query:

                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
                    download_net = wifi.download() / 1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ", download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                elif "calculate" in query:
                    from calcu import Wolframalpha, calc

                    query = query.replace("calculate", "")
                    query = query.replace("fail", "")
                    calc(query)
                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("fail open", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "finally sleep" in query:
                    speak("see you soon boss")
                    exit()

                elif "take a screenshot" in query:
                    import pyautogui

                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                elif "translate" in query:
                    from translate import translategl

                    query = query.replace("fail", "")
                    query = query.replace("translate", "")
                    speak("sure boss")
                    translategl(query)

                elif "my location" in query:
                    query = query.replace("tell me", "")
                    query = query.replace("give me", "")
                    query = query.replace("show me", "")
                    ip_add = requests.get('https://api.ipify.org').text
                    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
                    geo_q = requests.get(url)
                    geo_d = geo_q.json()
                    state = geo_d['city']
                    country = geo_d['country']
                    speak(f"Boss,your current location is {state, country}.")
                    print(f"Boss,your current location is {state, country}.")

                elif "tell me space fact of the day" in query or "space fact" in query:
                    speak("tell me the date in the following format")
                    speak("year and month and day")
                    date = input("year and month and day: ")

                    from nasa import news_nasa

                    news_nasa(date)


                elif "show me the map of" in query or "map" in query:
                    query = query.replace("show me the map of", "")
                    query = query.replace("map", "")
                    from location import map
                    speak("this is what i can get boss")

                    map(query)

                elif "let's talk fail" in query or "let's talk" in query:
                    from talk import Gossip
                    query=query.replace("fail","")
                    Gossip()
                elif query == "how old are you" or query == "what is your age":
                    d0 = date(int(date.today().strftime("%Y")),
                              int(date.today().strftime("%m")),
                              int(date.today().strftime("%d")))
                    d1 = date(2023, 1, 3)
                    delta = d0 - d1
                    speak(f"i am {delta.days} days old")

                # elif "draw a photo" in query or "draw me  a photo" in query or "draw something" in query:
                #     query = query.replace("fail", "")

                #     from draw import drwing
                #     drwing()


