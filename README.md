##**Introduction**
###This is a simple virtual assistant that can do variety of task like
###Opening Google maps,Telling weather and temperature inforamtion ,
###sending email,create an instant meeting and much more!
***
##**Modules Used:**
###pyttsx3
* 'pyttsx3'###is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
##Installation
* pip install pyttsx3
###If you recieve errors such as No module named win32com.client, No module named win32, or No module named win32api, you will need to additionally install pypiwin32.
* Usage:
###import pyttsx3
###engine = pyttsx3.init()
###engine.say("I will speak this text")
###engine.runAndWait()
###speech_recognition
* Library for performing speech recognition, with support for several engines and APIs, online and offline.
##Installation
###pip install SpeechRecognition
* Usage:
###import speech_recognition as sr
###engine = pyttsx3.init('sapi5')
###voices = engine.getProperty('voices')
###engine.setProperty('voice', voices[0].id)
###selenium
* The selenium package is used to automate web browser interaction from Python.
###Installation
* from selenium import webdriver
* from selenium.webdriver.chrome.options import Options
* Usage:
###driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
###driver.get('https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
###username = driver.find_element_by_xpath('//*[@id="identifierId"]')
###username.click()
###username.send_keys(your username)
###next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
###next.click()

  



