import pyttsx3

robot_brain = "I am a robot, Dat"
robot_voice = pyttsx3.init()
robot_voice.say(robot_brain)
robot_voice.runAndWait()
