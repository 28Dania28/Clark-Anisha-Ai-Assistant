import DaniaAI_Conversation
import DaniaApplications
import DaniaWikipedia
import DaniaYoutube
import DaniaGoogle
import DaniaFacebook
from gtts import gTTS
import playsound
import speech_recognition as sr
import pyaudio
import datetime
import random
import os
from googletrans import Translator

i = 0
authority = "Himanshu Dania"

def speak_anisha(audio):
    global i
    i = i+1
    tts = gTTS(text=audio, lang="en-IN")
    filename = str("voice"+str(i)+".mp3")
    tts.save(filename)
    print("Anisha : {}".format(audio))
    playsound.playsound(filename)

def speak(text):
    global i
    i = i+1
    tts = gTTS(text=text, lang="en-IN")
    filename = str("voice"+str(i)+".mp3")
    tts.save(filename)
    playsound.playsound(filename)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak_anisha("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak_anisha("Good Afternoon Sir!")

    else:
        speak_anisha("Good Evening Sir!")


def listen_anisha():
    global authority
    r = sr.Recognizer()
    print("Anisha : Listening")
    text = ""
    with sr.Microphone() as source:
        audio = r.record(source, duration=4)
        print("Anisha : Recognising...")
        try:
            said = ""
            print("Anisha : Recognised")
            said = r.recognize_google(audio, language="en-IN")
            print(authority + " : " + said)
            text = said
        except Exception as e:
            return text
    return text

if __name__ == '__main__':
    wishMe()
    while True:
        query = listen_anisha().lower()
        if 'wikipedia' in query:
            DaniaWikipedia.daniaQuery(query)

        elif 'youtube' in query:
            DaniaYoutube.daniaQuery(query)


        elif 'google' in query:
            DaniaGoogle.daniaQuery(query)


        elif 'facebook' in query:
            DaniaFacebook.daniaQuery(query)

        elif 'open' in query:
            DaniaApplications.daniaQuery(query)

        elif 'say' in query or 'speak' in query:
            query = query.replace("say", "")
            speak_anisha(query)
        elif 'i am fine' in query or 'i am good' in query:
            ansList = ["Then i am also good", "Good to hear from you, How may i help"]
            speak_anisha(random.choice(ansList))

        elif 'i am' in query:
            query = query.replace("i am ", "")
            query = query.capitalize()
            speak_anisha("Ok sir i will remember that you are "+query)
            authority = query
        elif 'this is me' in query:
            authority = "Himanshu Dania"
            speak_anisha("Ok Mr DANIA")
        else:
            DaniaAI_Conversation.daniaQuery(query, authority)
