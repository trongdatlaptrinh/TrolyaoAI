import speech_recognition as sr
import pyttsx3
from datetime import date, datetime
import webbrowser
import time

robot_hear = sr.Recognizer()
robot_voice = pyttsx3.init(driverName = 'sapi5')

robot_voice.setProperty('rate',150)
robot_voice.setProperty('volume',1.0)

voices = robot_voice.getProperty('voices')
robot_voice.setProperty('voice', voices[1].id)
robot_brain = ""

def speak(text):
    print("Robot: ", text)
    robot_voice.say(text)
    robot_voice.runAndWait()
    robot_voice.stop()

while True:
    with sr.Microphone() as mic:
        robot_hear.adjust_for_ambient_noise(mic,duration = 1)
        print("Robot is listening...")
        audio = robot_hear.listen(mic, timeout = 5)
    try:
        you = robot_hear.recognize_google(audio).lower()
        print("You said: ", you)
    
    
        if you == "":
            robot_brain = "I can't hear you, Dat"
        elif "hello" in you:
            robot_brain = "Hi, Dat"
        elif "your name" in you:
            robot_brain = "I am a robot without a name"
        elif "today" in you:
            today = date.today()
            robot_brain = today.strftime("%B %d, %Y")
            print("Date: ", robot_brain)
        elif "time" in you:
            now = datetime.now()
            robot_brain = now.strftime("%H hour %M minutes %S seconds")
        elif "open google" in you:
            webbrowser.open("https://google.com")
            robot_brain = "Open Google"
        elif "open youtube" in you:
            webbrowser.open("https://www.youtube.com/")
            robot_brain = "Open Youtube"
        elif "bye" in you:
            robot_brain = "Goodbye you"
            speak(robot_brain)
            break
        else: 
            robot_brain = "I don't understand what you are saying, Dat"

        speak(robot_brain)
        time.sleep(0.3)
    except Exception as e:
        print("Error", e)
        you = ""
