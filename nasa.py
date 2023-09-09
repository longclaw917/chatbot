import requests
import os
from PIL import Image
from main import speak
from time import sleep
import datetime

api_key = "ESMNgi8dc59gFV0NJNQvAD4KqQzHbomMTeBkmQqg"


def news_nasa(Date):
    speak("here is your information")
    url = "https://api.nasa.gov/planetary/apod?api_key=ESMNgi8dc59gFV0NJNQvAD4KqQzHbomMTeBkmQqg"

    params = {'date': str(Date)}

    r = requests.get(url, params=params)

    data = r.json()
    Title = data['title']
    info = data['explanation']
    image_url = data['url']
    image_r= requests.get(image_url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:
        f.write(image_r.content)

    # print(Title)
    # print(info)
    # print(FileName)

    path_1 = "C:\\Users\\dhruba jyoti ghosh\\PycharmProjects\\AIProject\\" + str(FileName)


    path_2 = "C:\\Users\\dhruba jyoti ghosh\\OneDrive\\Pictures\\nasa\\" + str(FileName)

    os.rename(path_1,path_2)
    img = Image.open(path_2)
    img.show()
    speak(f"Title : {Title}")
    print(f"Title : {Title}\n")
    print(f"According to nasa : {info}\n")
    speak(f"According to nasa : {info}")
    os.remove(path_2)
    sleep(2)



# def Astro(start_date,ending_date):
#     url = f"http://https//api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={ending_date}&api_key=ESMNgi8dc59gFV0NJNQvAD4KqQzHbomMTeBkmQqg"
#     r=requests.get(url)
#     data = r.json()
#     totalbody = data['element_count']
#     neo = data['near_earth-objects']
#     speak(f"total astroid between {start_date} and {ending_date} is : {totalbody}")
#     for body in neo[start_date]:
#         id = body['id']
#         name = body['name']
#         absolute = body['absolute_magnitude_h']
#         print(id,name,absolute)
#     # print(data)
    # print(totalbody)


# news_nasa('2001-11-17')
