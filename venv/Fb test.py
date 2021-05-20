from gtts import gTTS
import playsound
import webbrowser
from selenium import webdriver
from time import sleep

i = 0
psid = "EnterYourPasswordHere"

def speak(audio):
    global i
    i = i + 1
    tts = gTTS(text=audio, lang="en-IN")
    filename = str("voicefb" + str(i) + ".mp3")
    tts.save(filename)
    print("Anisha : {}".format(audio))
    playsound.playsound(filename)


speak("Opening Your Facebook ID Sir")
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path='C:\Python\Python37/chromedriver.exe', options=options)
driver.get('https://www.facebook.com/')
sleep(1)
username_box = driver.find_element_by_id('email')
username_box.send_keys("enteruridhere@gmail.com")
sleep(1)
vision_box = driver.find_element_by_id('pass')
vision_box.send_keys(psid)
sleep(1)
login_box = driver.find_element_by_id('loginbutton')
login_box.click()
messenger_btn = driver.find_element_by_xpath("//*[@id='navItem_217974574879787']/a")
messenger_btn.click()


