import os
import openai
from main import takecommand
from main import speak
from datetime import date
import datetime


openai.api_key="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"

def Gossip():
    speak("hi boss")
    while True:

        prompt = takecommand().lower()
        if prompt =="none":
            speak("what are you thinking just say it")
            continue
        else:
            prompt = prompt.replace("sprite","")
            prompt = prompt.replace("none","")
            if prompt == "good bye" or prompt == "goodbye":
                speak("see you until next time")
                exit()
            elif prompt =="which year it is?" or prompt =="tell me the year":
                speak(datetime.date.today())


            elif prompt == "how old are you" or prompt == "what is your age":
                d0 = date(int(date.today().strftime("%Y")), int(date.today().strftime("%m")), int(date.today().strftime("%d")))
                d1 = date(2023, 1, 3)
                delta = d0 - d1
                speak(f"i am {delta.days} days old")


            else:
                completions = openai.Completion.create(prompt = prompt,
                                                       engine="text-davinci-002",
                                                       max_tokens =100)
                completions = completions.choices[0].text
                print(prompt)
                speak(completions)
                print(completions)



