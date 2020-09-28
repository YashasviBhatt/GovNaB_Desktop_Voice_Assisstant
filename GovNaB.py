# Importing the libraries

import pyttsx3                                  # python text-to-speech
import speech_recognition as sr
import datetime as dt
import wikipedia
import webbrowser
import os


# using 'sapi5' an api provided by microsoft for speech recognition within windows
engine = pyttsx3.init('sapi5')                          # creating object of pyttsx3.init() used for text-to-speech
voice = engine.getProperty('voices')                    # fetching voice from api object (zira_microsoft)
engine.setProperty('voice', voice[0])                   # setting the voice
engine.setProperty('rate', 160)                         # setting rate of speech

def speak(message):
    '''function to speak the message using text-to-speech'''
    engine.say(message)                                 # convert text-to-speech
    engine.runAndWait()

def greet():
    '''function to greet the user'''
    hour = dt.datetime.now().hour
    if 5 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 15:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('My name is GovNaB, I am a Desktop Assistant created by Yashasvi Bhatt. Please tell me How may I help you?')

def takeCommand():
    '''function to take voice input from user using speech-to-text'''
    r = sr.Recognizer()                                 # creating object of sr.Recognizer() used for speech-to-text
    with sr.Microphone() as source:                     # using the default microphone as voice input source
        print('Listening...')
        r.pause_threshold = 1                           # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 300
        audio = r.listen(source)                        # taking voice input from source
    query = ''
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in') # recognizing audio using google-speech-engine with english-india language
    except:
        print('Please! Say that Again')

    return query

if __name__ == '__main__':
    greet()
    while True:
        query = takeCommand().lower()

        # query handling

        # for google
        if 'open google' in query:
            webbrowser.open('google.com')

        # for youtube
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        # for wikipedia articles
        elif 'wikipedia' in query:
            print('Searching Wikipedia ...')
            speak('Searching Wikipedia')
            query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)     # fetching first 2 sentence as result on topic from wikipedia
            speak('According to Wikipedia')
            speak(results)

        # time
        elif 'time' in query:
            strTime = dt.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is {strTime}')

        # asking name
        elif 'what is your name' in query or 'who are you' in query:
            speak('My name is GovNaB, I am a Desktop Assistant')

        # for normal searching
        elif 'search for' in query or 'what is' in query or 'who is' in query:
            print('Surfing Internet...')
            speak('Searching for Possible Matches')
            results = wikipedia.summary(query, sentences=2)     # fetching results from wikipedia
            speak('According to Wikipedia')
            speak(results)

        # opening pycharm
        elif 'pycharm' in query:
            try:
                path = r'C:\Program Files\JetBrains\PyCharm Community Edition 2019.2.4\bin\pycharm64.exe'
                os.startfile(path)
            except:
                print('Can\'t Open')

        # opening visual studio
        elif 'visual' in query or 'code' in query:
            try:
                path = r'C:\Users\yash\AppData\Local\Programs\Microsoft VS Code\Code.exe'
                os.startfile(path)
            except:
                print('Can\'t Open')

        # exitting the program
        elif 'exit' in query or 'bye' in query or 'quit' in query or 'close' in query:
            speak('Bye! Have a nice day')
            if  21 < dt.datetime.now().hour < 5 :
                speak('Good Night')
            break

        # response handling
        elif 'thank' in query:
            speak('It\'s a Pleasure')

        else:
            try:
                results = wikipedia.summary(query, sentences=2)
                speak(results)
            except:
                print('Didn\'t get that')