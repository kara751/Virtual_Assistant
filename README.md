# Virtual Assistant using Python
## Introduction
This is a simple virtual assistant that can do variety of task like
Opening Google maps , telling weather and temperature inforamtion ,
sending email, create an instant meeting and much more just using voice command!
***
## **Modules Used:**
### pyttsx3
 * pyttsx3  is a text-to-speech conversion library in Python. <br /> 
 * Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
### Installation
 * pip install pyttsx3<br /> 
 * If you recieve errors such as No module named win32com.client,<br /> 
 * No module named win32, or No module named win32api, you will need to additionally install pypiwin32.
 ### Usage:
  import pyttsx3<br />
  engine = pyttsx3.init()<br />
  engine.say("I will speak this text")<br />
  engine.runAndWait()<br />
### speech_recognition
 Library for performing speech recognition, with support for several engines and APIs, online and offline.
### Installation
* pip install SpeechRecognition
### Usage:
  import speech_recognition as sr<br />
  engine = pyttsx3.init('sapi5')<br />
  voices = engine.getProperty('voices')<br />
  engine.setProperty('voice', voices[0].id)<br />
### selenium
 The selenium package is used to automate web browser interaction from Python.
### Installation
* pip install selenium
### Usage:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
### tkinter
The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit.<br />
Both Tk and tkinter are available on most Unix platforms, as well as on Windows systems. <br />
(Tk itself is not part of Python; it is maintained at ActiveState.)
### Installation
* pip install tk
### Usage:
from tkinter import *<br />
root=Tk()<br />
root.geometry("700x550")<br />
root.resizable(0,0)<br />
root.mainloop()

![GUI TKINTER](jarvis.png)
  



