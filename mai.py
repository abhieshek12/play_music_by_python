import speech_recognition as sr 
import webbrowser
import pyttsx3 
import music_Library as ml 

engine = pyttsx3.init()

def speak(txt) :
    engine.say(txt)
    engine.runAndWait()


def command(comand) :
    if "open google" in comand.lower() :
        webbrowser.open("https://www.google.co.in/") 
    elif "open youtube" in comand.lower() :
        webbrowser.open("https://www.youtube.com/")     
    elif comand.startswith("play") :
        song = comand[5:] 
        link = ml.library(song) 
        webbrowser.open(link)
        

speak("initializing alexa .....")        
    
while True :
    r = sr.Recognizer()
    try :
        with sr.Microphone() as source :
            print("listning")
            audio = r.listen(source , timeout=3 , phrase_time_limit=2 ) 
            text = r.recognize_google(audio) 
            if text.lower() == "alexa" :
                speak("tell me what i have to do master ") 
                print(" alexa active ....listning") 
                
                with sr.Microphone() as source :
                    audio = r.listen(source )
                    cmd = r.recognize_google(audio) 
                    command(cmd) 
    except Exception as e :
        print("say alexa to activate alexa "  )              
                    