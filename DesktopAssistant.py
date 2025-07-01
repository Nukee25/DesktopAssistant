import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
from google import genai
from Key import api_key as key

class DesktopAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("voice",'en-IN')
        self.engine.setProperty("rate",160)
        self.recognizer = sr.Recognizer()
        self.talk("ooo mai kenhda serdaar ji sutsriakaal!! How do you do today?")

    def talk(self,text=str()):
        self.engine.say(text)
        self.engine.runAndWait()
        print(text)
        return None

    def hear(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio =self.recognizer.listen(source)
        try:
            print("Recognizing...")
            query =self.recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            self.talk("Say that again please...")
            return "None"
        return query.lower()
    @staticmethod
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
        nameword = name.split()
        website = nameword[(nameword.index("open")+1)]
        self.talk(f"Opening {website}...")
        return 1
    @staticmethod
    def run(self,name=str()):
        words = name.split()
        i=words.index("open")
        app = words[i+1]
        os.system(app)
        return None
    def gptresp(self,query=str()):
        client = genai.Client(api_key=key)
        self.talk("Please wait while I am thinking...")
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=(query.lower()+" in about 100 words")
        )
        print(response.text)
        return response.text.replace("*","")
da = DesktopAssistant()
while 1 == 1:
    query = da.hear()
    if "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        da.talk(f"Sir, the time is {strTime}")
    if "open" in query.lower():
        result = da.browser(query)
        if result == 1:
            da.run(query)
    if "tell me about" or "what is" in query.lower():
        answer = da.gptresp(query)
        da.talk(answer)
    if "exit" or "quit" in query:
        break

