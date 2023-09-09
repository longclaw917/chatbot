fileopen = open("api.txt", "r")
api = fileopen.read()
fileopen.close()
print(api)

import openai
from dotenv import load_dotenv

openai.api_key = api
load_dotenv()
completion = openai.Completion()


def ReplyBrain(question, chat_log=None):
    Filelog = open("api.txt", "r")
    chat_log_template = Filelog.read()
    Filelog.close()

    if chat_log is None:
        chat_log = chat_log_template
    prompt = f'{chat_log}you : {question}\nsprite : '
    response = completion.create(model="text-davinci-002"
                                 , prompt=prompt,
                                 temperature=0.5,
                                 max_tokens=60,
                                 top_p=0.3,
                                 frequency_penalty=0.5,
                                 presence_penalty=0
                                 )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nyou : {question}\nsprite :{answer}"
    Filelog = open("chat_log.txt", "w")

    Filelog.write(chat_log_template_update)
    Filelog.close()
    return answer


reply = ReplyBrain("how are you")
print(reply)
