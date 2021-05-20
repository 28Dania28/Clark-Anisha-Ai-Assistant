from gtts import gTTS
import playsound
import wikipedia
import webbrowser

i = 0
def speak(audio):
    global i
    i = i+1
    tts = gTTS(text=audio, lang="en-IN")
    filename = str("voicewk"+str(i)+".mp3")
    tts.save(filename)
    print("Anisha : {}".format(audio))
    playsound.playsound(filename)


def daniaQuery(query):

    if 'search' in query and 'in wikipedia' in query:
        query = query.replace("search", "")
        speak("Searching"+query)
        query_new = query.replace("in wikipedia", "")
        results = wikipedia.summary(f'{query_new}', sentences=2)
        speak("According to wikipedia : " + results)

    elif 'search' in query and 'on wikipedia' in query:
        query = query.replace("search", "")
        speak("Searching" + query)
        query_new = query.replace("on wikipedia", "")
        results = wikipedia.summary(f'{query_new}', sentences=2)
        speak("According to wikipedia : " + results)

    elif 'open' in query and 'on wikipedia' in query:
        query = query.replace("open", "")
        speak("Opening" + query)
        query_new = query.replace("on wikipedia", "")
        try:
            webbrowser.get().open_new_tab(
                "https://en.wikipedia.org/wiki/{}".format(query_new))
        except Exception as e:
            print("Try again sir.")

    elif 'open' in query and 'in wikipedia' in query:
        query = query.replace("open", "")
        speak("Opening" + query)
        query_new = query.replace("in wikipedia", "")
        try:
            webbrowser.get().open_new_tab(
                "https://en.wikipedia.org/wiki/{}".format(query_new))
        except Exception as e:
            print("Try again sir.")

    elif 'open wikipedia' in query:
        speak("Opening Wikipedia")
        try:
            webbrowser.get().open_new_tab("https://en.wikipedia.org/wiki/")
        except Exception as e:
            print("Try again sir.")


    elif 'open' in query and 'wikipedia' in query:
        query = query.replace("open", "")
        speak("Opening" + query)
        query = query.replace("wikipedia", "")
        try:
            webbrowser.get().open_new_tab(
                "https://en.wikipedia.org/wiki/{}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'search' in query and 'wikipedia' in query:
        query = query.replace("open", "")
        speak("Searching" + query)
        query = query.replace("wikipedia", "")
        try:
            webbrowser.get().open_new_tab(
                "https://en.wikipedia.org/wiki/{}".format(query))
        except Exception as e:
            print("Try again sir.")




    else:
        speak('Searching Wikipedia')
        query_new = query.replace("wikipedia", "")
        results = wikipedia.summary(f'{query_new}', sentences=2)
        speak("According to wikipedia : " + results)


