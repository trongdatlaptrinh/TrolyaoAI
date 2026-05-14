import speech_recognition

robot_hear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot is listening...")
    audio = robot_hear.listen(mic)
try:
    you = robot_hear.recognize_google(audio)
except:
    you == ""

print("You said: " + you)
