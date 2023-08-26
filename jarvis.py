import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

name = 'siri'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


for voice in voices:
    print(voice)

def talk(text):   
    engine.say(text)
    engine.runAndWait()

def listen():
 try:
    with sr.Microphone() as source:
        print("playing...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        rec = rec.lower()
        if name in rec:
            rec = rec.replace(name, '')
            talk(rec)
 except:
    pass
 return rec
def run():
    rec = listen()
    if 'play' in rec:
        music = rec.replace('play','')
        talk('playing' + music)
        pywhatkit.playonyt(music)
        talk(rec)
        
    elif 'time' in rec:
        time = datetime.datetime.now().strftime('%H:%M')
        talk("are the"+ time)
    elif 'busca' in rec:
        order = rec.replace('busca','')
        info = wikipedia.summary(order, 1)
        talk(info)
    else:
        talk("retry")
while True:        
   run()