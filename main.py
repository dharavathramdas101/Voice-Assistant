import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import os

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
    city = input("What city would you like to know the weather for? ")
    weather_data = wikipedia.summary(city + " weather", sentences=1)
    speak(weather_data)

def todo():
    todo_list = []
    while True:
        task = input("What would you like to add to your to-do list? ")
        todo_list.append(task)
        print("Your to-do list is now: " + str(todo_list))
        answer = input("Would you like to add another item to your to-do list? (y/n) ")
        if answer == "n":
            break

def alarm():
    hour = int(input("What hour would you like the alarm to go off? "))
    minute = int(input("What minute would you like the alarm to go off? "))
    speak("Your alarm is set for " + str(hour) + ":" + str(minute))

def main():
    while True:
        command = listen()
        if command == "weather":
            weather()
        elif command == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The current time is " + current_time)
        elif command == "todo":
            todo()
        elif command == "alarm":
            alarm()
        elif command == "exit":
            break

if __name__ == "__main__":
    main()
