import speech_recognition as sr
import pyttsx3
import datetime
import wx
import wikipedia
import webbrowser
import os
import openai

class desktopAssistant:
    def __init__(self):
        engine = pyttsx3.init()
        engine.say("O mai kenda sardar ji satsriakaal. How can I help you?")
        print("O mai kenda sardar ji satsriakaal. How can I help you?")
        engine.runAndWait()

    def talk(self,text=str()):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        print(text)
        return None

    def hear(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            self.talk("Say that again please...")
            return "None"
        return query.lower()
    def browser(self,name=str()):
        if 'open youtube' in name:
            webbrowser.open("youtube.com")
        elif 'open google' in name:
            webbrowser.open("google.com")
        elif 'open whatsapp' in name:
            webbrowser.open("web.whatsapp.com")
        elif 'open github' in name:
            webbrowser.open("github.com")
        elif 'open gmail' in name:
            webbrowser.open("gmail.com")
        return None
    def run(self,name=str()):
        words = name.split()
        i=words.index("open")
        app = words[i+1]
        os.system(app)
        return None
desktopAssistant = desktopAssistant()
i = 1
while i==1:
    query = desktopAssistant.hear()
    if "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        desktopAssistant.talk(f"Sir, the time is {strTime}")
    if "what is" in query:
    if "open" in query.lower():
        desktopAssistant.browser(query)
        desktopAssistant.run(query)


