
import pywhatkit
from datetime import timedelta
from datetime import datetime
from main import speak , takecommand

strtime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))


def sendmsg():
    speak("who do you want to message boss")
    a = takecommand().lower()
    if a == "kunal":
        speak("what do you want to send him boss ")
        msg = takecommand().lower()
        pywhatkit.sendwhatmsg("+918697503203", msg, time_hour=strtime, time_min=update)
    elif a == "shruti":
        speak("what do you want to send her boss ")
        msg = takecommand().lower()
        pywhatkit.sendwhatmsg("+919748934716", msg, time_hour=strtime, time_min=update)
    elif a == "baba":
        speak("what do you want to send him boss ")
        msg = takecommand().lower()
        pywhatkit.sendwhatmsg("+919674782833", msg, time_hour=strtime, time_min=update)
    elif a == "madhumita":
        speak("what do you want to send her boss ")
        msg = takecommand().lower()
        pywhatkit.sendwhatmsg("+916290287808", msg, time_hour=strtime, time_min=update)
    elif a == "anirban sir":
        speak("what do you want to send her boss ")
        msg = takecommand().lower()
        pywhatkit.sendwhatmsg("+919830078197", msg, time_hour=strtime, time_min=update)
