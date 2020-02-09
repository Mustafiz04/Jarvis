import pyttsx3
import random as r
import pythoncom
import speech_recognition as sr
import pyaudio
import datetime
import webbrowser
import wikipedia
import os

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis. Please tell me how can I help you ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:- {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please... ")
        return 'None'
    return query

if __name__ == "__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikikpedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')    
        elif 'play music' in query:
            music_dr = 'E:\\Mp3'
            songs = os.listdir(music_dr)
            ran = r.randint(0, len(songs)-1 )
            # print(songs)
            os.startfile(os.path.join(music_dr, songs[ran])) # random
        elif 'play video' in query:
            video_dr = 'F:\\download\\music'
            videos = os.listdir(video_dr)
            ran = r.randint(0, len(videos)-1 )
            # print(songs)
            os.startfile(os.path.join(video_dr, videos[ran])) # random
        elif 'time' in query:
            Time = datetime.datetime.now().strftime('%H:%M:%S')
            print(Time)
            speak(f"Sir, The time is {Time}")
        elif 'open code' in query:
            cpath = '"C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(cpath)
        elif 'thank you for your help' in query:
            speak("Welcome")
            break
