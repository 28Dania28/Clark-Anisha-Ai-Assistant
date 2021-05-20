from gtts import gTTS
import playsound
import webbrowser

i = 0
def speak(audio):
    global i
    i = i+1
    tts = gTTS(text=audio, lang="en-IN")
    filename = str("voiceyt"+str(i)+".mp3")
    tts.save(filename)
    print("Anisha : {}".format(audio))
    playsound.playsound(filename)


def daniaQuery(query):

    if 'play songs in youtube' in query or 'play song in youtube' in query or 'search songs in youtube' in query or 'search song in youtube' in query or 'play songs on youtube' in query or 'play song on youtube':

        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/watch?v=TqWYLdtLvIk&list=RDMM&start_radio=1")
        except Exception as e:
            print("Try again sir.")

    elif 'search' in query and 'in youtube' in query:
        query = query.replace("search", "")
        query = query.replace("in youtube", "")
        speak("Searching " + query + " in youtube")
        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/results?search_query={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'search' in query and 'on youtube' in query:
        query = query.replace("search", "")
        query = query.replace("on youtube", "")
        speak("Searching " + query + " on youtube")
        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/results?search_query={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'open' in query and 'on youtube' in query:
        query = query.replace("open", "")
        query = query.replace("on youtube", "")
        speak("Opening " + query + " on youtube")
        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/results?search_query={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'open' in query and 'in youtube' in query:
        query = query.replace("open", "")
        query = query.replace("in youtube", "")
        speak("Opening " + query + " in youtube")
        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/results?search_query={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'play' in query and 'in youtube' in query:
        query = query.replace("play", "")
        query = query.replace("in youtube", "")
        speak("Playing " + query + " in youtube")
        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/results?search_query={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'play' in query and 'on youtube' in query:
        query = query.replace("play", "")
        query = query.replace("on youtube", "")
        speak("Playing " + query + " on youtube")
        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/results?search_query={}".format(query))
        except Exception as e:
            print("Try again sir.")

    elif 'search' in query and 'youtube' in query:
        query = query.replace("search", "")
        query = query.replace("youtube", "")
        speak("Searching " + query + " in youtube")
        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/results?search_query={}".format(query))
        except Exception as e:
            print("Try again sir.")


    elif 'open youtube' in query:
        speak("Opening Youtube")
        try:
            webbrowser.get().open_new_tab("youtube.com")
        except Exception as e:
            print("Try again sir.")


    elif 'open' in query and 'youtube' in query:
        query = query.replace("open", "")
        query = query.replace("youtube", "")
        speak("Opening " + query + " in youtube")
        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/results?search_query={}".format(query))
        except Exception as e:
            print("Try again sir.")




    else:
        query = query.replace("youtube", "")
        speak("Opening " + query + " youtube")
        try:
            webbrowser.get().open_new_tab(
                "https://www.youtube.com/results?search_query={}".format(query))
        except Exception as e:
            print("Try again sir.")


