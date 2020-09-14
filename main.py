import pyttsx3 # to be pip installed
import speech_recognition as sr # to be pip installed
import datetime
import wikipedia #to be pip installed
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')#initialize the engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis  Sir. Please tell me how may I help you")       

def takeCommand():
    '''It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('raajasrieeth.python@gmail.com', 'raajasrieeth6')# think its the wrong password!
    server.sendmail('raajasrieeth.python@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")   
        elif 'open github' in query:
            webbrowser.open("www.github.com")


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Kavitha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("Sir To whom shall I send it?")
                to = takeCommand()+"@gmail.com"# default

                speak("What should I say?")
                content = takeCommand()
                speak("Sending to" + to)
                permission = takeCommand()
                if permission == "No" or permission == "Stop":
                    break
                else:
                    sendEmail(to, content)

                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")    
        elif 'shut up' in query:
            speak('Allright')
            break
        elif 'open website' in query:
            speak("Which website do you want to open")
            name = takeCommand()
            try: 
                webbrowser.open('www.'+ name+'.com')
                speak("opening" + name)
            except Exception:
                speak("Error!")


# import pyttsx3#see available voices
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()