from io import open_code
from sys import excepthook, exec_prefix, path
from urllib.request import OpenerDirector
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import playsound
from time import sleep
import pythonwin
import pythoncom


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# initialisation
engine = pyttsx3.init()

engine.connect('started-utterance', 'onStart')
engine.connect('started-word', 'onWord')
engine.connect('finished-utterance', 'onEnd')




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" Hey Amol! I am JAR Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query  


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abp1677@gmail.com', 'Amol@7710804681.')
    server.sendmail('abp1677@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower().upper()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open whatsApp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'open Instagram' in query:
            webbrowser.open("Instagram.com")
            query
            usersiad = ('Amol Account')
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('_.amol._.patil._', 'Amol@1677.')
            server.close()

        elif 'open GTA V' in query:
            GamePath = (
                "C:\Program Files (x86)\Steam\steamapps\common\Grand Theft Auto V")

        elif 'play song' in query:
            music_dir = ("D:\Vivo 3\Videoder")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\coding\jarvis python assi"
            os.startfile(codePath)

        elif 'mail to Amol' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ("abp1677@gmail.com")
                sendEmail(to, content)
                speak("mail")
            except Exception as e:
                print(e)
                speak("Sorry my friend Amol bhai. I am not able to send this email")