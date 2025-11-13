import pyttsx3
import speech_recognition as sr
import pyaudio
import pywihatkit as py
import datetime
import wikipedia
from wikipedia import languages

engine=pyttsx3.init(driverName="sapi5")
engine.setProperty('rate',150)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        listener.pause_threshold=1
        audio=listener.listen(source)
    try:
        print("Listening...")
        command=listener.recognize_google(audio)
        print(f"you said:{command}")
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return " "
    except sr.RequestError:
        speak("sorry,could not request results from service")
        return " "
    return command

def run_assistant():
    command=listen()
    if "play" in command:
        song=command.replace("play","")
        speak(f"playing {song}")
        py.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time is {time}")
        speak(f"the time is {time}")
    elif "date" in command:
        date=datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Today is {date}")
        speak(f"the date is {date}")
    elif "search" in command:
        browse=command.replace("search","")
        speak(f"searching {browse}")
        py.search(browse)
    elif "open youtube" in command:
        speak("opening youtube")
        py.playonyt(" ")
    elif "stop" in command:
        speak("Tata,Have a good day")
        exit()
    else:
        speak("I didn't get that")

speak("Hello! I'm your personal voice assistant Built by Vishnu Dharshini . Nice to meet you")
while True:
    run_assistant()
