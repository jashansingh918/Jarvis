import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime #default installed engine
import webbrowser # default installed engine
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sunshine!")
    else:
        speak("Welcome Back sunshine!")

    speak("How may i help you,love!")

def takeCommand():#it will take input from user that is microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #how long it gonna wait to hear our voice and then reply to it
        audio = r.listen(source)#source is microphone

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')#query is the question we asked
        print(f"You: {query}\n") #i think this is what we said not sure tho

    except Exception as e: #we have to create exception also like if u r not connected to internet
        print(e)
        print("Sorry, PLease say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia') #when we say something to microphone so instead of printing it gonna say it but we can also make it print like we did before
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)#it gonna print first two sentences from wiki what we searched for
            speak("According to wikipedia")
            print(results)
            speak(results)
        


    

    

    



