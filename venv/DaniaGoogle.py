from gtts import gTTS
import playsound
import webbrowser

i = 0


def speak(audio):
    global i
    i = i + 1
    tts = gTTS(text=audio, lang="en-IN")
    filename = str("voicegg" + str(i) + ".mp3")
    tts.save(filename)
    print("Anisha : {}".format(audio))
    playsound.playsound(filename)


def daniaQuery(query):
    if 'search' in query and 'in google' in query:
        query = query.replace("search", "")
        query = query.replace("in google", "")
        speak("Searching " + query + " in google")
        try:
            webbrowser.get().open_new_tab(
                "https://www.google.com.tr/search?q={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'search' in query and 'on google' in query:
        query = query.replace("search", "")
        query = query.replace("on google", "")
        speak("Searching " + query + " on google")
        try:
            webbrowser.get().open_new_tab(
                "https://www.google.com.tr/search?q={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'open' in query and 'on google' in query:
        query = query.replace("open", "")
        query = query.replace("on google", "")
        speak("Opening " + query + " on google")
        try:
            webbrowser.get().open_new_tab(
                "https://www.google.com.tr/search?q={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'open' in query and 'in google' in query:
        query = query.replace("open", "")
        query = query.replace("in google", "")
        speak("Opening " + query + " in google")
        try:
            webbrowser.get().open_new_tab(
                "https://www.google.com.tr/search?q={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'open google' in query:
        speak("Opening Google")
        try:
            webbrowser.get().open_new_tab("https://www.google.com/")
        except Exception as e:
            print("Try again sir.")



    elif 'search' in query and 'google' in query:
        query = query.replace("search", "")
        query = query.replace("google", "")
        speak("Searching " + query + " in google")
        try:
            webbrowser.get().open_new_tab(
                "https://www.google.com.tr/search?q={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'open' in query and 'google' in query:
        query = query.replace("open", "")
        query = query.replace("google", "")
        speak("Opening " + query + " in google")
        try:
            webbrowser.get().open_new_tab(
                "https://www.google.com.tr/search?q={}".format(query))
        except Exception as e:
            print("Try again sir.")



    else:
        query = query.replace("google", "")
        speak("Searching " + query + " on google")
        try:
            webbrowser.get().open_new_tab(
                "https://www.google.com.tr/search?q={}".format(query))
        except Exception as e:
            print("Try again sir.")


