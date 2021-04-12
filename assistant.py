import pyttsx3
import datetime
import speech_recognition as sr

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
        print(query)
    except Exception as e:
        print(f"Repeat please{e}")
        return ""
    return query
    
if __name__ == '__main__':
    greet()
    while(1):
        query=inputVoice().lower
    
    

    





