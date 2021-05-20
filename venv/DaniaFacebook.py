from gtts import gTTS
import playsound
import webbrowser
from selenium import webdriver
from time import sleep

i = 0
psid = "\"hidden\""

def speak(audio):
    global i
    i = i + 1
    tts = gTTS(text=audio, lang="en-IN")
    filename = str("voicefb" + str(i) + ".mp3")
    tts.save(filename)
    print("Anisha : {}".format(audio))
    playsound.playsound(filename)



def daniaQuery(query):
    global psid
    if 'open my facebook' in query:
        speak("Opening Your Facebook ID Sir")
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(executable_path='E:\DaniaAI\AnishaAI\chromedriver.exe', chrome_options=options)
        driver.get('https://www.facebook.com/')
        sleep(1)
        username_box = driver.find_element_by_id('email')
        username_box.send_keys("hdania28@gmail.com")
        sleep(1)
        vision_box = driver.find_element_by_id('pass')
        vision_box.send_keys(psid)
        sleep(1)
        login_box = driver.find_element_by_id('loginbutton')
        login_box.click()




    elif 'open facebook' in query:
        speak("Opening Facebook")
        try:
            webbrowser.get().open_new_tab(
                "https://www.facebook.com")
        except Exception as e:
            print("Try again sir.")


