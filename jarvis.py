import ctypes
import datetime
import shutil
import time
import wave
from email.message import EmailMessage
from tkinter import font
import ec as ec
import gmaps
import pyaudio
import pyjokes as pyjokes
import pyttsx3
import speech_recognition as echo
import wikipedia
import webbrowser
import os
import random
import pyautogui
import smtplib
import pywhatkit
import googletrans
import winshell as winshell
from googletrans import Translator
import sys
import playsound
from ipywidgets import Controller
from playsound import playsound
import platform
import wmi
import psutil
import wolframalpha
import subprocess
from covid import Covid
import speedtest
from PyDictionary import PyDictionary
import cv2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkinter import *

global area
root=Tk()
#######################################################        ALL IMPORT ABOVE          ################################################################

try:
    client = wolframalpha.Client('######-##########')
except Exception:
    print("Some features are not working")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# engine.setProperty("rate",180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def remainder(x, y):
    return x % y

    #######################################################        WISH ME           ################################################################


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning Sir !")
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon Sir !")
        speak("Good Afternoon Sir !")
    else:
        print("Good Evening Sir !")
        speak("Good Evening Sir !")
        assname = ("Jarvis")
        print("I am your Personal Assistant")
        speak("I am your Personal Assistant")
        print(assname)
        speak(assname)

        #######################################################        TAKE COMMAND           ################################################################


def takeCommand():
    r = echo.Recognizer()
    with echo.Microphone() as source:
        print("Listening...")
        playsound('C:/Users/kbbha/Downloads/notification.mp3')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"{query}\n")
        except Exception as e:
            print("Speak it again plz...")
            speak("Speak it again plz...")
            return "None"
        return query

        #######################################################        USERNAME           ################################################################


def userName():
    print("What should i call you sir")
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    print("How can i Help you, Sir")
    speak("How can i Help you, Sir")

    #######################################################       SEND EMAIL FUNCTION         ################################################################


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Your email', 'Your password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'name1': 'name1@gmail.com',
    'name2': 'name2@gmail.com'
}


#######################################################        GET EMAIL INFO FUNCTION        ################################################################

def get_email_info():
    print('To Whom you want to send email')
    speak('To Whom you want to send email')
    name = takeCommand()
    receiver = email_list[name]
    print(receiver)
    print('What is the subject of your email?')
    speak('What is the subject of your email?')
    subject = takeCommand()
    print('Tell me the text in your email')
    speak('Tell me the text in your email')
    message = takeCommand()
    send_email(receiver, subject, message)
    print('Your email is sent')
    speak('Your email is sent')
    print('Do you want to send more email?')
    speak('Do you want to send more email?')
    send_more = takeCommand()
    if 'yes' in send_more:
        get_email_info()
    else:
        print("ok sir")
        speak("ok sir")


#######################################################        MAIN METHOD THAT FIRST RUN          ################################################################
def start():
 if __name__ == '__main__':
    time.sleep(1)
    playsound('C:/Users/kbbha/Downloads/jarvis_introduction.mp3')
    wishMe()
    userName()

    # speak("Hello , i am echo what can i do for you")

    #######################################################        SECOND MAIN METHOD          ################################################################
    if __name__ == '__main__':
        while True:
            query = takeCommand().lower()

    #######################################################        WIKIPEDIA          ################################################################

            if "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)


            #######################################################        YOUTUBE           ################################################################

            elif 'open youtube' in query:
                print("Ok sir...")
                speak("Ok sir...")
                webbrowser.open('youtube.com')


            #######################################################        GOOGLE         ################################################################

            elif 'open google' in query:
                print("Ok sir...")
                speak("Ok sir...")
                webbrowser.open('google.com')


            #######################################################        GMAIL          ################################################################

            elif 'open gmail' in query:
                print("Ok sir...")
                speak("OK sir...")
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")



            #######################################################        OPEN YOUR GOOGLE CLASSROOM         ################################################################

            elif 'google classroom' in query:
                speak("Enter classroom user name")
                user = input("enter classroom user name:-")
                speak("enter classroom password")
                pas = input("enter classroom password:-")

                opt = Options()
                opt.add_argument("start-maximized")
                opt.add_argument("--disable-extensions")
                opt.add_experimental_option("prefs", { \
                    "profile.default_content_setting_values.media_stream_mic": 1,
                    "profile.default_content_setting_values.media_stream_camera": 1,
                    "profile.default_content_setting_values.geolocation": 1,
                    "profile.default_content_setting_values.notifications": 1
                })

                driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", options=opt)
                driver.get(
                    'https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
                username = driver.find_element_by_xpath('//*[@id="identifierId"]')
                username.click()
                username.send_keys(user)

                next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
                next.click()

                time.sleep(3)

                password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
                password.click()
                password.send_keys(pas)

                next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
                next.click()

                time.sleep(20)




            #######################################################      SEND MAIL         ################################################################

            elif 'send mail' in query:
                get_email_info()



            #######################################################       GMAIL LOGIN         ################################################################

            elif 'gmail login' in query:
                speak("Enter user name")
                user = input("enter user name:-")
                speak("enter password")
                passw = input("enter password:-")

                driver = webdriver.Chrome('C:\chromedriver.exe')
                driver.get(
                    'https://accounts.google.com/AccountChooser/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser')
                username = driver.find_element_by_xpath('//*[@id="identifierId"]')
                username.click()
                username.send_keys(user)

                next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
                next.click()

                time.sleep(3)

                password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
                password.click()
                password.send_keys(passw)

                next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
                next.click()

                time.sleep(20)



            #######################################################        GOOGLE MEET INSTANT MEETING          ################################################################

            elif 'instant meeting' in query:

                speak("Enter user name")
                user = input("enter user name:-")
                speak("Enter password")
                passw = input("enter password:-")

                driver = webdriver.Chrome('C:\chromedriver.exe')
                driver.get(
                    'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmeet.google.com%2Flanding&ec=GAlAmwM&flowName=GlifWebSignIn&flowEntry=AddSession')
                username = driver.find_element_by_xpath('//*[@id="identifierId"]')
                username.click()
                username.send_keys(user)

                next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
                next.click()

                time.sleep(3)

                password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
                password.click()
                password.send_keys(passw)

                x = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
                x.click()

                time.sleep(20)

                meeting = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/button/div[2]')
                meeting.click()

                time.sleep(5)

                instantMeeting = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/ul/li[2]/span[3]')
                instantMeeting.click()

                time.sleep(15)





            #######################################################        What is the meaning of         ################################################################

            elif 'what is the meaning of' in query:
                dictionary = PyDictionary()
                query = query.replace("what is the meaning of", '')
                print("Meaning is ")
                speak("Meaning is")
                print(dictionary.meaning(query))
                speak(dictionary.meaning(query))
                print("Synonym is ")
                speak("Synonym is")
                print(dictionary.synonym(query))
                speak(dictionary.synonym(query))
                print("Antonym is ")
                speak("Antonym is")
                print(dictionary.antonym(query))
                speak(dictionary.antonym(query))


            #######################################################        NEWS           ################################################################

            elif 'news' in query:
                print("Ok sir...")
                speak("Ok sir...")
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)


            #######################################################        STACKOVERFLOW         ################################################################

            elif 'open stackoverflow' in query or 'open stack overflow' in query:
                print("Ok sir...")
                speak("Ok sir...")
                webbrowser.open('stackoverflow.com')




            #######################################################        OPEN FACEBOOK       ################################################################

            elif 'open facebook' in query:
                print("Ok sir...")
                speak("OK sir...")
                webbrowser.open('facebook.com')



            #######################################################        OPEN INSTAGRAM         ################################################################

            elif 'open instagram' in query:
                print("Ok sir...")
                speak("OK sir...")
                webbrowser.open('instagram.com')


            #######################################################      OPEN W3SCHOOLS        ################################################################

            elif 'open w3schools' in query:
                print("Ok sir...")
                speak("OK sir...")
                webbrowser.open('w3schools.com')

                #######################################################       OPEN MEET         ################################################################

            elif 'open meet' in query:
                print("Ok sir...")
                speak("Ok sir...")
                webbrowser.open('https://meet.google.com/')


            #######################################################        OPEN INCOGNITO TAB          ################################################################

            elif 'private window' in query:
                print("Ok sir...")
                speak("Ok sir...")
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--incognito")

                driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", options=chrome_options)

                driver.implicitly_wait(2)

                driver.get('https://www.google.com')
                driver.maximize_window()



            #######################################################        PLAY LAPTOP MUSIC           ################################################################

            elif 'play music' in query or 'play song' in query:
                music_dir = 'C:\\Users\\kbbha\\OneDrive\\Desktop\\NAMO NAMO'
                songs = os.listdir(music_dir)
                print(songs)
                speak("OK sir...")
                os.startfile(os.path.join(music_dir, songs[random.randint(1, 28)]))


            #######################################################        MAKE A FOLDER           ################################################################

            elif 'make a folder' in query:
                print("Ok sir...")
                speak("Ok sir...")
                parent = "C:/Users/kbbha/OneDrive/Desktop/"
                speak("what should be the name of the folder")
                dir = takeCommand()
                path = os.path.join(parent, dir)
                os.mkdir(path)
                print("Directory '% s' created" % dir)
                speak("folder created " + dir)


            #######################################################       TODAY'S TIME          ################################################################

            elif 'the time' in query:
                tday = datetime.datetime.today()
                print(tday)
                
            elif 'precautions for covid-19' in query or 'precaution for covid 19' in query:
                speak("Wear a mask")
                speak("Clean your hands")
                speak("Maintain safe distance")
                speak("Get vaccinated")

            elif 'covid' in query or 'Covid' in query:
                covid = Covid(source="worldometers")
                print(covid.get_data())
                #speak(covid.get_data())
                india_cases = covid.get_status_by_country_name("india")
                print(india_cases)
                speak(india_cases)

            #######################################################        WHEN WAS YOU CREATED           ################################################################

            elif 'when was' in query:
                t = datetime.date(2021, 2, 26)
                print(t)
                speak("I was created in")
                speak(t)


            #######################################################       OPEN VISUAL STDIO CODE        ################################################################

            elif 'open code' in query:
                print("Ok sir...")
                speak("Ok sir...")
                codePath = "C:\\Users\\kbbha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)


            #######################################################        OPEN GOOGLE CHROME         ################################################################

            elif 'open google chrome' in query:
                print("Ok sir...")
                speak("Ok sir...")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)




            #######################################################       OPEN ANDROID STUDIO          ################################################################

            elif 'open android studio' in query:
                print("Ok sir...")
                speak("Ok sir...")
                subprocess.Popen("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe")


            #######################################################     OPEN COMMAND PROMPT        ################################################################

            elif 'open cmd' in query or 'open command prompt' in query:
                print("Ok sir...")
                speak("Ok sir...")
                cmd = "C:\\Windows\\system32\\cmd.exe"
                os.startfile(cmd)


            #######################################################       OPEN POWERPOINT          ################################################################

            elif 'open powerpoint' in query:
                print("Ok sir...")
                speak("Ok sir...")
                os.startfile("C:\\Users\\kbbha\\Downloads\\Presentation1.pptx")

            #######################################################        OPEN EXCEL         ################################################################

            elif 'open excel' in query:
                print("Ok sir...")
                speak("Ok sir...")
                os.startfile("C:\\Users\\kbbha\\Downloads\\Book1.xlsx")


            #######################################################        OPEN MS PAINT           ################################################################

            elif 'open ms paint' in query:
                print("Ok sir...")
                speak("Ok sir...")
                subprocess.Popen("C:\\Windows\\system32\\mspaint.exe")

            #######################################################    OPEN NOTEPAD         ################################################################

            elif 'open notepad' in query:
                print("Ok sir...")
                speak("Ok sir...")
                subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

            #######################################################        OPEN MS WORD          ################################################################

            elif 'open ms word' in query:
                print("Ok sir...")
                speak("Ok sir...")
                subprocess.Popen("C:\\Windows\\system32\\msword.exe")



            #######################################################        TAKE A SCREENSHOT           ################################################################

            elif 'take screenshot' in query:
                speak("Please hold for a few seconds sir!")
                img = pyautogui.screenshot()
                img.save('ss.png')
                speak("Done sir...")

            #######################################################      Can we go for a date           ################################################################

            elif 'Can we go for a date' in query:
                speak("Sorry, I have a headache")

            #######################################################      Are you single         ########################################################################

            elif 'Are you single' in query:
                speak("I am in relationship with wifi")

            #######################################################      Do you love me          #######################################################################

            elif 'Do you love me' in query or 'I love you' in query:
                speak("I love you too , but as a friend")



            #######################################################    how old are you          ################################################################

            elif 'how old are you' in query:
                speak("I just turn to 5")

            #######################################################      In which class you read          ################################################################

            elif 'In which class you read' in query:
                speak("I just started going to kinder garten")

            #######################################################     what is love        ################################################################

            elif 'what is love' in query:
                speak("It just a waste of time and you just should focus on your study")

            #######################################################     do you know ghost         ################################################################

            elif 'Do you know ghost' in query:
                speak("I meet them every midnight")

            #######################################################      Who is your father          ################################################################

            elif 'Who is your father' in query:
                speak("Tony Stark is my father")

            #######################################################     Are you handsome         ################################################################

            elif 'Are you handsome' in query:
                speak("I feel that i am handsome")

            ######################################################    How can i kill you          ################################################################
            elif 'How can i kill you' in query:
                speak("I really sorry,please let me go")


            #######################################################       HOW ARE YOU         ################################################################

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            #######################################################        I AM FINE         ################################################################

            elif 'fine' in query:
                speak("It's good to know that your fine")

            #######################################################        EXIT         ################################################################

            elif 'exit' in query:
                speak("Thanks for giving me your time")
                exit()

            #######################################################        WHO MADE YOU         ################################################################

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by Deepak, Abhihshekgiri , Balram and Karan.")

            #######################################################        TELL ME A JOKE          ################################################################

            elif 'joke' in query:
                py = pyjokes.get_joke()
                print(py)
                speak(py)

            #######################################################      LOCK WINDOW         ################################################################

            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            #######################################################       PLAY SOMETHING ON YOUTUBE          ################################################################

            elif 'play' in query:
                print("Ok sir...")
                speak("Ok sir...")
                speak(query)
                pywhatkit.playonyt(query)

            #######################################################       HELLO WORLD IN JAVA          ################################################################

            elif 'hello world in java' in query:

                print('''class HelloWorld {
                public static void main(String[] args){
                System.out.println("Hello, World!"); }}''')

                speak("class HelloWorld {")
                speak("public static void main(String[] args){")
                speak('System.out.println("Hello, World!"); }}')

            #######################################################        SEND WHATSUP MESSAGE         ################################################################

            elif 'send message' in query:
                print("Ok sir...")
                speak("Ok sir...")

                print("sending...")
                speak("sending...")
                pywhatkit.sendwhatmsg("+91xxxxxxxxxx", "Hello", 14, 12)



            #######################################################       SEARCH SOMETHING ON GOOGLE           ################################################################

            elif 'on google' in query:
                print("Ok sir...")
                speak("Ok sir...")
                search = query.replace('on google', "")
                speak("Searching...")
                pywhatkit.search(search)

            #######################################################      SHUTDOWN         ################################################################

            elif 'shutdown' in query:
                print("shutting down...after 100s")
                speak("shutting down...after 100 s")
                pywhatkit.shutdown(100)

            #######################################################        CANCLE SHUTDOWN          ################################################################

            elif 'cancle shutdown' in query:
                print("Ok sir, Canceling")
                speak("OK sir, Canceling...")
                pywhatkit.cancelShutdown()

            #######################################################      EMPTY RECYCLE BIN         ################################################################

            elif 'empty recycle bin' in query:
                print("Ok sir...")
                speak("Ok sir...")
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin Recycled")
                speak("Recycle Bin Recycled")

            #######################################################       TRANSLATE ENGLISH TO HINDI          ################################################################

            elif 'in hindi' in query:
                print("What should i translate sir")
                speak("What should i translate sir")
                s = takeCommand()
                translator = Translator()
                s = translator.translate(s, src='en', dest='hi')
                print(s.text)




            #######################################################      TRANSLATE ENGLISH TO FRENCH          ################################################################

            elif 'in french' in query:
                translator = Translator()
                result = translator.translate(query.replace('translate in french', ""), src='en', dest='fr')
                print(result.text)
            elif 'information about' in query:
                query = query.replace('Information about',"")
                pywhatkit.info(query,lines=4)
            #######################################################       TEMPERATURE IN CITYNAME         ################################################################

            elif 'temperature in' in query:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    print(output)
                    speak(output)
                except:
                    print("Error!")

            #######################################################       WEATHER IN LOCATION         ################################################################

            elif 'weather in' in query:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    print(output)
                    speak(output)
                except:
                    print("Error!")


            #######################################################        CALCULATE MATHEMATICAL OPERATIONS         ################################################################

            elif 'calculate' in query:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    print(output)
                    speak(output)
                except:
                    print("Error!")


            #######################################################        TELL THEN           ################################################################

            elif 'tell' in query:
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    print(output)
                    speak(output)
                except:
                    print("Error!")
                    speak("I dont have any data about " + query)






            #######################################################      SYSTEM INFORMATION          ################################################################

            elif 'system info' in query:
                my_system = platform.uname()
                print(f"System: {my_system.system}")
                speak("System")
                speak(my_system.system)
                print(f"Node Name: {my_system.node}")
                speak("Node Name")
                speak(my_system.node)
                print(f"Release: {my_system.release}")
                speak("Release")
                speak(my_system.release)
                print(f"Version: {my_system.version}")
                speak("Version")
                speak(my_system.version)
                print(f"Machine: {my_system.machine}")
                speak("Machine")
                speak(my_system.machine)
                print(f"Processor: {my_system.processor}")
                speak("Processor")
                speak(my_system.processor)

                c = wmi.WMI()
                my_system = c.Win32_ComputerSystem()[0]
                print(f"Manufacturer: {my_system.Manufacturer}")
                speak("Manufacturer")
                speak(my_system.Manufacturer)
                print(f"Model: {my_system.Model}")
                speak("Model")
                speak(my_system.Model)
                print(f"Name: {my_system.Name}")
                speak("Name")
                speak(my_system.Name)
                print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
                speak("NumberOfProcessors")
                speak(my_system.NumberOfProcessors)
                print(f"SystemType: {my_system.SystemType}")
                speak("SystemType")
                speak(my_system.SystemType)
                print(f"SystemFamily: {my_system.SystemFamily}")
                speak("SystemFamily")
                speak(my_system.SystemFamily)

                usage = str(psutil.cpu_percent())
                print("CPU is at " + usage)
                speak("CPU is at " + usage)

                battery = psutil.sensors_battery()
                print("Battery is at", battery.percent)
                speak("Battery is at")
                speak(battery.percent)




            #######################################################     |WHERE IS|USE FOR GOOGLE MAP LOCATION         ################################################################

            elif 'where is' in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.com/maps/place/" + location + "")

            #######################################################       UNIQUE GOOGLE MAPS          ################################################################

            elif 'google maps' in query or 'google map' in query:
             def mapss():
                driver = webdriver.Chrome('C:\chromedriver.exe')
                driver.get('https://www.google.com/maps/dir///@28.5214323,77.2265495,13z/data=!4m2!4m1!3e3')
                time.sleep(10)
                print("starting point")
                speak("starting point")
                query = takeCommand()

                time.sleep(5)

                tx1 = driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input')
                tx1.click()
                tx1.send_keys(query)

                time.sleep(3)
                print("destination point")
                speak("destination point")
                query = takeCommand()

                tx2 = driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input')
                tx2.click()
                tx2.send_keys(query)

                time.sleep(5)

                sear = driver.find_element_by_xpath('//*[@id="directions-searchbox-1"]/button[1]')
                sear.click()

                time.sleep(10)

                print("would you like to open satellite mode")
                speak("would you like to open satellite mode")

                query = takeCommand()
                if 'yes' in query or 'han' in query or "bilkul" in query:
                    speak("ok sir")
                    menu = driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[1]/button')
                    menu.click()

                    time.sleep(2)

                    satellite = driver.find_element_by_xpath(
                        '//*[@id="settings"]/div/div[2]/ul/jsl[2]/ul[1]/li[2]/div/button[1]/label')
                    satellite.click()

                    time.sleep(5)

                else:
                    speak("OK sir")

             

            #######################################################       WRITE A NOTE          ################################################################

            elif 'write a note' in query:
                print("what should i write sir")
                speak("what should i write sir")
                note = takeCommand()

                file = open('a.txt', 'w')
                file.write(note)
                print("noted")
                speak("noted")

            #######################################################        SHOW NOTE IN CONSOLE           ################################################################

            elif 'show note' in query:
                speak("showing note")
                file = open('a.txt', "r")
                print(file.read())
                speak(file)


            #######################################################   VOLUME UP         ################################################################

            elif 'volume up' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.press("volumeup")

            #######################################################       VOLUME DOWN         ################################################################

            elif 'volume down' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.press("volumedown")

            #######################################################       VOLUME MUTE         ################################################################

            elif 'volume mute' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.press("volumemute")



            #######################################################        SELECT WHOLE TEXT           ################################################################

            elif 'select' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('ctrl', 'a')


            #######################################################        COPY SELECTED TEXT          ################################################################

            elif 'copy' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('ctrl', 'c')

            #######################################################      PASTE SELECTED TEXT         ################################################################

            elif 'paste' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('ctrl', 'v')

            #######################################################        YOU SPEAK AND I TYPE ON ANYTHING THAT WILL OPEN LIKE NOTEPAD!         ################################################################

            elif 'type' in query or 'write' in query or 'right' in query:
                print("what you want to type")
                speak("what you want to type")
                query = takeCommand()
                pyautogui.typewrite(query)


            #######################################################        SAVE         ################################################################

            elif 'save' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('ctrl', 'shift', 's')

            #######################################################        DELETE         ################################################################

            elif 'delete' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('delete')

            #######################################################       CLOSE         ################################################################

            elif 'close' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('ctrl', 'w')


            #######################################################        MAXIMIZE          ################################################################
            elif 'maximize' in query or 'maximise' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('alt', 'space', 'x')



            #######################################################       FULLSTOP        ################################################################

            elif '.' in query or 'fullstop' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('.')


            #######################################################       COMMA          ################################################################

            elif 'comma' in query or 'coma' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey(',')

            #######################################################       RENAME         ################################################################

            elif 'rename' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('f2')

            #######################################################      REFRESH        ################################################################

            elif 'refresh' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('f5')

            #######################################################      LAPTOP SETTING         ################################################################

            elif 'setting' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey('win', 'i')

            #######################################################        SEMICOLON          ################################################################

            elif 'semicolon' in query or ';' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey(';')

            #######################################################       COLON        ################################################################

            elif 'colon' in query or ':' in query:
                print("Ok sir...")
                speak("Ok sir...")
                pyautogui.hotkey(':')





           #######################################################       RECORD       ################################################################

            elif 'record' in query:
                CHUNK = 1024
                FORMAT = pyaudio.paInt16
                CHANNELS = 2
                RATE = 44100
                RECORD_SECONDS = 10
                WAVE_OUTPUT_FILENAME = "output.wav"

                p = pyaudio.PyAudio()

                stream = p.open(format=FORMAT,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK)

                print("* recording")

                frames = []

                for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                    data = stream.read(CHUNK)
                    frames.append(data)

                print("* done recording")

                stream.stop_stream()
                stream.close()
                p.terminate()

                wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                wf.close()

            #######################################################       ADD/SUBTRACT/MULTIPLY/DIVIDE/REMAINDER IN CONSOLE         ################################################################

            elif 'add number' in query or 'subtract number' in query or 'multiply number' in query or 'divide number' in query or 'remainder' in query:

                print("Select operation.")
                print("1.ADD")
                print("2.SUBTRACT")
                print("3.MULTIPLY")
                print("4.DIVIDE")
                print("5.REMAINDER")

                while True:
                    a = input("ENTER CHOICE(1-2-3-4-5):-")
                    if a in ('1', '2', '3', '4', '5'):
                        b = float(input("ENTER FIRST NUMBER: "))
                        c = float(input("ENTER SECOND NUMBER: "))

                        if a == '1':
                            print(b, "+", c, "=", add(b, c))
                        elif a == '2':
                            print(b, "-", c, "=", subtract(b, c))
                        elif a == '3':
                            print(b, "*", c, "=", multiply(b, c))
                        elif a == '4':
                            print(b, "/", c, "=", divide(b, c))
                        elif a == '5':
                            print(b, "%", c, "=", remainder(b, c))
                        break

            else:
                print("I dont have any data about")
                speak("I dont have any data about")

try:
 root.geometry("700x550")
 framecn=19
 frames=[PhotoImage(file='abcd.gif',format = 'gif -index %i' %(i)) for i in range(framecn)]
 def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == framecn:
        ind = 0
    label.configure(image=frame)
    root.after(90, update, ind)
 label = Label(root,bg="black")
 label.place(x=30,y=50)
 #label.pack()
 root.after(0, update, 0)
 l2=Label(text="A Virtual Assistant that we all need!",padx=7,fg="white",bg="black",font="Helvetica 15 bold")
 l2.place(x=140,y=8)
 #l2.pack()
 def youtube():
    speak("Ok sir...")
    webbrowser.open('youtube.com')
 def mapss():
                driver = webdriver.Chrome('C:\chromedriver.exe')
                driver.get('https://www.google.com/maps/dir///@28.5214323,77.2265495,13z/data=!4m2!4m1!3e3')
                time.sleep(10)
                print("starting point")
                speak("starting point")
                query = takeCommand()

                time.sleep(5)

                tx1 = driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input')
                tx1.click()
                tx1.send_keys(query)

                time.sleep(3)
                print("destination point")
                speak("destination point")
                query = takeCommand()

                tx2 = driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input')
                tx2.click()
                tx2.send_keys(query)

                time.sleep(5)

                sear = driver.find_element_by_xpath('//*[@id="directions-searchbox-1"]/button[1]')
                sear.click()

                time.sleep(10)

                print("would you like to open satellite mode")
                speak("would you like to open satellite mode")

                query = takeCommand()
                if 'yes' in query or 'han' in query or "bilkul" in query:
                    speak("ok sir")
                    menu = driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[1]/button')
                    menu.click()

                    time.sleep(2)

                    satellite = driver.find_element_by_xpath(
                        '//*[@id="settings"]/div/div[2]/ul/jsl[2]/ul[1]/li[2]/div/button[1]/label')
                    satellite.click()

                    time.sleep(5)

                else:
                    speak("OK sir")

 def google():
     speak("Ok sir...")
     webbrowser.open('google.com')
 def gmail():
     webbrowser.open_new_tab("gmail.com")
     speak("Google Mail open now")
 def meeting():
     speak("Enter user name")
     user = input("enter user name:-")
     speak("Enter password")
     passw = input("enter password:-")
     opt = Options()
     opt.add_argument("start-maximized")
     opt.add_argument("--disable-extensions")
     opt.add_experimental_option("prefs", { \
         "profile.default_content_setting_values.media_stream_mic": 1,
         "profile.default_content_setting_values.media_stream_camera": 1,
         "profile.default_content_setting_values.geolocation": 1,
         "profile.default_content_setting_values.notifications": 1
     })

     driver = webdriver.Chrome('C:\chromedriver.exe',options=opt)

     driver.get(
         'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmeet.google.com%2Flanding&ec=GAlAmwM&flowName=GlifWebSignIn&flowEntry=AddSession')
     username = driver.find_element_by_xpath('//*[@id="identifierId"]')
     username.click()
     username.send_keys(user)

     next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
     next.click()

     time.sleep(3)

     password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
     password.click()
     password.send_keys(passw)

     x = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
     x.click()

     time.sleep(20)

     meeting = driver.find_element_by_xpath(
         '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/button/div[2]')
     meeting.click()

     time.sleep(5)

     instantMeeting = driver.find_element_by_xpath(
         '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/ul/li[2]/span[3]')
     instantMeeting.click()

     time.sleep(15)   
 date = datetime.datetime.now()
 format_date = f"{date:%a, %b %d %Y}"
 l3 = Label(root, text=format_date,padx=4, fg="white", bg="green", font=("helvetica", 15,'bold'))
 l3.place(x=40,y=70)
 #l3.pack()
 b1=Button(fg="white",bg="blue",text="Start",command=start,padx=7,font="Helvetica 15 bold")
 b1.place(x=260,y=470)
 b2=Button(fg="white",bg="red",text="Youtube",font="Helvetica 15 bold",command=youtube)
 b2.place(x=520,y=70)
 b3=Button(fg="white",bg="purple",text="Google",font="Helvetica 15 bold",command=google)
 b3.place(x=70,y=160)
 b4=Button(fg="white",bg="blue",text="Gmail",font="Helvetica 15 bold",command=gmail)
 b4.place(x=535,y=160)
 b5=Button(fg="white",bg="orange",text="Maps",font="Helvetica 15 bold",command=mapss)
 b5.place(x=75,y=250)
 b5 = Button(fg="white", bg="#ff0080", text="Instant\nMeeting", font="Helvetica 14 bold", command=meeting)
 b5.place(x=545, y=250)
 exit_button = Button(root,text="Exit",padx=7, command=root.destroy,fg="white",bg="orange",font="TimesNewRoman 15 bold")
 exit_button.place(x=370,y=470)
 #b1.pack()
 root.title("JARVIS -A Personal Virtual Assistant")
 root.resizable(0,0)
 root.mainloop()
except Exception as e:
    print("Error!")
