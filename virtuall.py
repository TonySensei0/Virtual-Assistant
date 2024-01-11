import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
from selenium import webdriver
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon boss!")   

    else:
        speak("Good Evening boss!")  

    speak("I am Tuesday . Please tell me how may i help you")       

def takeCommand():
    #It takes microphone query from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
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

  

def generate_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
        "Why did the computer keep its drink on the windowsill? Because it wanted to have a cold drink.",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised",
        "Parallel lines have so much in common. It's a shame they'll never meet",
        "I used to play piano by ear, but now I use my hands and fingers",
        "I told my computer I needed a break, and now it won't stop sending me vacation ads",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I only know 25 letters of the alphabet. I don't know y"
    ]

    return random.choice(jokes)




if __name__ == "__main__":

    speak("Project X .... on")
   
    wishMe()

    
    while True:

        if 1:
           query = takeCommand().lower()
    

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
        


        elif 'thank you' in query:
            print("its my pleasure to help you boss. if you need any other help i am here for you!")
            speak("its my pleasure to help you boss. if you need any other help i am here for you!")
        

            

        elif 'tell me some jokes' in query:
            joke = generate_joke()
            print(joke)  
            speak(joke)


        elif 'google' in query:
            search_url = (f"https://www.google.com/search?q={query}")
            webbrowser.open(search_url)

        elif 'youtube' in query:
            search_url = (f"https://www.youtube.com/search?q={query}")
            webbrowser.open(search_url)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\anton\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open word' in query:
            wordPath = "C:\Program Files\LibreOffice\program\swriter.exe"
            os.startfile(wordPath)
        
        elif 'open excel' in query:
            excelPath = "C:\Program Files\LibreOffice\program\scalc.exe"
            os.startfile(excelPath)

        elif 'open powerpoint' in query:
            powPath = "C:\Program Files\LibreOffice\program\simpress.exe"
            os.startfile(powPath)
        elif 'shutdown' in query:
            print("shutting down..")
            speak("shutting down..")
            exit()


       
        
        