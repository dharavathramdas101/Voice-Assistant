import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import os
import sys
from PyQt5 import QtWidgets

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hello, I am your voice assistant. How can I help you today?")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("I didn't understand that.")
    except sr.RequestError:
        print("Sorry, I couldn't process your request. Please try again.")
    return data

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # Select Indian female voice (change index if needed)
    engine.setProperty('voice', voices[1].id)
    # Increase the speech rate (change value if needed)
    engine.setProperty('rate', 200)
    engine.say(text)
    engine.runAndWait()

def weather():
    city = listen()
    weather_data = wikipedia.summary(city + " weather", sentences=1)
    speak(weather_data)

def todo():
    todo_list = []
    while True:
        task = listen()
        todo_list.append(task)
        print("Your to-do list is now: " + str(todo_list))
        answer = listen()
        if answer == "n":
            break

def alarm():
    hour = int(listen())
    minute = int(listen())
    speak("Your alarm is set for " + str(hour) + ":" + str(minute))

def google_search():
    query = listen()
    url = "https://www.google.com/search?q=" + query
    os.system(f"start {url}")

def chrome_search():
    query = listen()
    url = "https://www.google.com/search?q=" + query
    os.system(f"start chrome {url}")

def youtube_search():
    query = listen()
    url = "https://www.youtube.com/results?search_query=" + query
    os.system(f"start chrome {url}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Voice Assistant")
    button = QtWidgets.QPushButton("Listen")
    button.clicked.connect(lambda: speak(listen()))
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(button)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
