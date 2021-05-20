from gtts import gTTS
import playsound
import webbrowser
import os

i = 0


def speak(audio):
    global i
    i = i + 1
    tts = gTTS(text=audio, lang="en-IN")
    filename = str("voiceapp" + str(i) + ".mp3")
    tts.save(filename)
    print("Anisha : {}".format(audio))
    playsound.playsound(filename)


def daniaQuery(query):

    if 'android studio' in query:
        speak("Opening Android Studio")
        try:
            studio_path = "C:/Program Files/Android/Android Studio/bin/studio64.exe"
            os.startfile(studio_path)
        except Exception as e:
            print("Try again sir.")

    elif 'notepad' in query:
        speak("Opening Notepad")
        try:
            path = "C:/Program Files (x86)/Notepad++/notepad++.exe"
            os.startfile(path)
        except Exception as e:
            print("Try again sir.")

    elif 'eclipse' in query:
        speak("Opening Eclipse IDE")
        try:
            path = "C:/Users/admin/eclipse/java-oxygen/eclipse/eclipse.exe"
            os.startfile(path)
        except Exception as e:
            print("Try again sir.")

    elif 'firefox' in query:
        speak("Opening Mozilla Firefox")
        try:
            path = "C:/Program Files/Mozilla Firefox/firefox.exe"
            os.startfile(path)
        except Exception as e:
            print("Try again sir.")


    elif 'chrome' in query:
        speak("Opening Google Chrome")
        try:
            path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
            os.startfile(path)
        except Exception as e:
            print("Try again sir.")

    elif 'unreal engine' in query:
        speak("Opening Unreal Engine")
        try:
            path = "E:/Program Files/Epic Games/UE_4.22/Engine/Binaries/Win64/UE4Editor.exe"
            os.startfile(path)
        except Exception as e:
            print("Try again sir.")

    elif 'visual' in query:
        speak("Opening Visual Studio Code")
        try:
            path = "E:/Users/admin/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(path)
        except Exception as e:
            print("Try again sir.")








