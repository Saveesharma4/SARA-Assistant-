import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrary
import requests
import game
import wikipedia

recognizer = sr.Recognizer()
engine = pyttsx3.init()
# newsapi = "" here you can add news api key for news 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        speak("Sorry, I couldn't find anything on Wikipedia.")

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif  "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "game" in c.lower():
        game.play()
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkdln" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
            song = c.lower().split(" ",)[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
    elif " tell news" in c.lower():
        r = requests.get( f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
        for article in articles:
            speak(article['title'])
   
    print(c)
    
if __name__ == "__main__" :
    speak ("initializing Sara ...")#listening for the wake word SARA
    #audio from microphone
    while True:

     r = sr.Recognizer()
   
     print ("recognining")
     try:
        with sr.Microphone() as source:
            print("say something!")
            audio = r.listen(source, timeout = 2, phrase_time_limit = 1 ) # wake word waiting 
        word = r.recognize_google(audio)
        
        if (word.lower() == "bunty"):
            speak ("ya")
            print ("sara Active ...")
        with sr.Microphone()as source:
         print("Listening for command ...")
         audio = r.listen(source)
         command = r.recognize_google(audio)
         processCommand(command)
     except sr.UnknownValueError:
        print("could not understand the audio")
     except sr.RequestError as e:
        print(f"Speech recognition service error:{e}")
    
     except Exception as e:
        print(f"Error: {e}")