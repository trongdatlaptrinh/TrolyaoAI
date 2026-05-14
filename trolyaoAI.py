import speech_recognition as sr
import pyttsx3
from datetime import date, datetime

robot_hear = sr.Recognizer()
robot_voice = pyttsx3.init()
robot_brain = ""

while True:
    with sr.Microphone() as mic:
        print("Robot is listening...")
        audio = robot_hear.listen(mic)
    
    try:
        you = robot_hear.recognize_google(audio).lower()
    except:
        you = ""

    print("You said: ", you)

    if you == "":
        robot_brain = "I can't hear you, Dat"
    elif "hello" in you:
        robot_brain = "Hello, Dat"
    elif you == "what is your name":
        robot_brain = "I am a robot with out a name"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
        print("Date: ", robot_brain)
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hour %M minutes %S seconds")
    elif "bye" in you:
        robot_brain = "Goodbye you"
        print("Robot: " + robot_brain)
        robot_voice.say(robot_brain)
        robot_voice.runAndWait()
        break
    else: 
        robot_brain = "I don't understand what you are saying, Dat"

    print("Robot: " + robot_brain)
    robot_voice.say(robot_brain)
    robot_voice.runAndWait()
