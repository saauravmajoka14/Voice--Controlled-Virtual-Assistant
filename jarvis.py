import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    h=int(datetime.datetime.now().hour)
    if h>=0 and h<12:
        speak("good morning!")
    elif h>=12 and h<18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("i am alexa! how may i help you?")

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('saitama8929@gmail.com','saurav@123')
    server.sendmail('saitama8929@gmail.com', to ,content)
    server.close()





def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        r.energy_threshold=1000
        audio=r.listen(source)

    try:
        print('Recognizing....')
        q=r.recognize_google(audio, language='en-in')
        print("user said:", q)
    except:
        print("say that again please!")
        return "None"
    return q

if __name__ == "__main__":
    sendemail('sauravmajoka@gmail.com',"hi")
    wishme()
    
    while True:

        q=takecommand().lower()
        if "wikipedia" in q:
            speak("searching wikipedia...")
            q=q.replace('wikipedia',"")
            print(q)
            results=wikipedia.summary(q,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in q:
            webbrowser.open("youtube.com")
        elif "open google" in q:
            webbrowser.open("google.com")
        elif "open facebook" in q:
            webbrowser.open("facebook.com")
        elif "open instagram" in q:
            webbrowser.open("instagram.com")
        elif 'time' in q:
            t=datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir, the time is")
            speak(t)
        elif 'open code' in q:
            path="C:\\Users\\saurav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'quit' in q:
            speak("thank you sir")
            break
        elif 'send mail' in q:
            try:
                speak("what should i send")
                content=takecommand()
                to="sauravmajoka14@gmail.com"
                sendemail(to,content)
                speak("email has been sent")
            
            except:
                speak("sorry, email can not send")







