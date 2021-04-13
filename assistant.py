import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init()
engine.setProperty('voice',engine.getProperty('voices')[1].id)
r = sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    speak("Have Fun Using Desktop Assistant")
    
def inputVoice():
   
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)          #without it the program takes ambient noises and keeps on recording at a strech        
        print("Say something!")
        audio = r.listen(source)
    try:
        query=r.recognize_google(audio,language='en-US')
    except Exception as e:
        print(f"Repeat please{e}")
        return ""
    return query
    
def moduleWikipedia(query):
    query=query.replace('wikipedia',"")
    try:
        speak(wikipedia.summary(query,sentences=2))
    except Exception:
        speak("Could Not Find The Result")

def moduleBrowse(query):
    query=query.replace('browse',"").strip()
    if "www." not in query:
        query="www."+query
    if ".com" not in query:
        query=query+".com"
    webbrowser.open(query)

def google(query):
    query=query.replace('google',"").strip()
    webbrowser.open(f"www.google.com/search?q={query}")


if __name__ == '__main__':
    greet()
    while(1):
        query=inputVoice().lower()
        if(query in ["quit","terminate","exit","bye"]):
            exit()
        print(query)
        if 'wikipedia' in query:
            moduleWikipedia(query)
        elif 'browse' in query:
            moduleBrowse(query)
        elif 'google' in query:
            google(query)
        elif 'open' in query:
            os.system(query.replace("open","").strip())

            

            

        

    
    

    





