from  os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
from main import takecommand
from main import speak

def whatsappmsg():

    startfile("C:\\Users\\dhruba jyoti ghosh\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(3)
    click(x=504, y=164)
    speak("Who do you want to send message boss")
    name=takecommand().lower()
    speak("ok boss")
    sleep(2)
    write(name)
    sleep(2)
    click(x=365, y=365)
    speak("what should i write boss")
    msg=takecommand().lower()
    sleep(0.5)
    write(msg)
    press('enter')





