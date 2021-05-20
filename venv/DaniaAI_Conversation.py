from gtts import gTTS
import playsound
import os
import datetime
import random

i = 0


def speak(audio):
    global i
    i = i + 1
    tts = gTTS(text=audio, lang="en-IN")
    filename = str("voiceaicv" + str(i) + ".mp3")
    tts.save(filename)
    print("Anisha : {}".format(audio))
    playsound.playsound(filename)

def introduction():
    speak("Hi I am Anisha. I am an Artificial Intelligent assistent made by Himanshu Dania.")

def daniaQuery(query, authority):

    if 'the time' in query and 'what' in query or "what's the time" in query or 'what is the time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("The time is {}".format(time))

    elif 'who are you' in query:
        introduction()

    elif 'who am i' in query or 'who i am' in query:
        speak("You are " + authority + ". How can you forget your name Sir!")

    elif 'what is my name' in query or "what's my name"in query:
        speak("Your name is " + authority)

    elif 'what is your name' in query or "what's your name" in query:
        speak("My name is Anisha sir. How can you forget my name sir.")

    elif 'exit' in query:
        speak("Have a nice day sir, Bye")
        exit()

    elif 'go to sleep' in query:
        speak('Ok sir, Have a nice day, Bye')
        exit()

    elif query == 'hi' or query == 'hello ' or 'hello' in query or 'hi' in query:
        ansList = ["Hello, How are you?","Hello, How is your day going", "Hello ji", "Hello Mr "+authority]
        speak(random.choice(ansList))
    elif 'i am fine' in query or 'i am good' in query:
        ansList = ["Then i am also good", "Good to hear from you, How may i help"]
        speak(random.choice(ansList))

    elif query == "I love you":
        ansList = ["I admire you too"]
        speak(random.choice(ansList))

    elif 'how are you' in query:
        ansList = ["I am very good", "I am well,thank you sir, how can i help", "I am too good sir, How may i help you"]
        speak(random.choice(ansList))


    elif 'bye' in query or 'close' in query or 'exit' in query:
        speak("Have a nice day.")
        exit()








