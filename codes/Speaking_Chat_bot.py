
import datetime
import wikipedia
import pyaudio
import speech_recognition as sr
import os
import pyttsx3
import win32com.client
import webbrowser
import random

import openai


api_key="Apikey*******"

def ai(prompt):
    openai.api_key = api_key
    text=f"From Chat GPT response : \n###\n{prompt}\n###"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
               frequency_penalty=0,
        presence_penalty=0
    )
    ans = response["choices"][0]["text"]
    print(ans)
    say(ans)
    text+=ans


    with open(f"openai responses/{''.join(prompt.split('intelligence')[1:30])}", 'w') as f:
        f.write(text)

speaker=win32com.client.Dispatch("SAPI.SpVoice")
def say():
    while True:
        print("enter the word you want to speak: ")
        s=input()
        speaker.Speak(s)
def say(audio):
    speaker.Speak(audio)
    print(audio)


def command():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognizing....")
            query=r.recognize_google(audio,language="en-in")#language can be hi-in for hindi
            print ("::::",query,":::::")
        except Exception as e:
            print("i did not understand")
            say("i did not understand ")




        return query
chatstr=""
def chat(query):
    global chatstr
    print(chatstr)
    openai.api_key = api_key
    chatstr+=f" user : {query}\n jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    ans = response["choices"][0]["text"][1:200]
    chatstr += f"{ans}\n"
    say(ans)
    return ans

    



def wish():

        hour = int(datetime.datetime.now().hour)  # we get an hour in the integer of 24 hrs

        # setting the hours for wishing me
        if 0 <= hour < 5 and 22 < hour <= 24:
            say("here we again! , late night work")
        elif hour >= 5 and hour < 12:
            say("good morning! ")
        elif hour >= 12 and hour < 18:
            say("good AFTERNOON! ")
        elif hour >= 18 and hour < 22:
            say("good Evening! ")

        say("Systeam is ready ")





if __name__=='__main__':
    wish()
    while True:
        print("Listening....")
        query= command().lower()
        say(query)

        if "shutdown" in query:
            say("ohk! closing system")
            quit()
        elif "wikipedia" in query:
            say("searching on wikipedia")
            query = query.replace("wikipedia", "")  # removing wikipedia from sentence for the serach
            results = wikipedia.summary(query, sentences=2)  # searching that senntece on the wikipedia
            say("according to wiki")
            say(results)

        sites=[["you tube", "youtube.com"],["google","google.com"]]


        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]}")
                webbrowser.open(site[1])

        if "play music" in query:

            music_dir = "C:\\Users\\Asus\\Music\\music"
            songs = os.listdir(music_dir)
            print(songs)
            song = len(songs)
            print(song)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, song - 1)]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            time=(f"sir the time is now", strTime)
            say(time)
        elif "open vs code" in query:
            path = "C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(path)

        elif "open pycharm" in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\JetBrains\\PyCharm Community Edition 2022.3.2.lnk"
            os.startfile(path)
        elif "using chat gpt" in query:
            ai(prompt=query)
        else:
            chat(query)



        

