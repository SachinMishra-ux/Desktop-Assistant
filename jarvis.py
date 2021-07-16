import pyttsx3 # Speech API 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5') # google "sapi5" for more inforamation(realted to speech API) 
voices=engine.getProperty('voices') # inbuilt voices from microsoft
#print(voices[1].id) # just to check which kind of voices are avialable in the system
engine.setProperty('voices',voices[0].id) # seted to first voice

def speak(audio): # Jarvis will speak using this funcation
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour= int(datetime.datetime.now().hour) # we get value of hour from 0-24
    if 0<hour and hour<12:
        speak("Good Morning Boss")   
    elif hour>12 and hour<18:
        speak("Good Afternoon Boss")     
    else:
        speak("Good evening Boss")
    speak("Hi I am jaarvis. Version 1.0. I am Your Personal Assistant, How may I help you")        

def takeCommand (): # This will take microphone input from user and return a string o/p
    r=sr.Recognizer() #class recognizer which will help to recognize the audio
    with sr.Microphone() as source:
        print("Listening...") 
        #r.energy_threshold=100
        r.pause_threshold=1 # till 1 sec of delay in speaking is considerable
        #r.phrase_threshold=0.3 # before 0.3 all audio will get filtered
        audio=r.listen(source)
        print(audio)

    try:
        print("Recognizing...")
        query=(r.recognize_google(audio)) # using google speech recognizer we are try to recognize the voice
        print(f"User Said:{query}\n")
    except Exception as e:
        print("say that again please...")     
        return "None"  
    return query  

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sachin19566@gmail.com','password')
    server.sendmail('sachin19566@gmail.com',to,content)
    server.close()



if __name__=="__main__":
    WishMe()
    takeCommand()

    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  

        elif 'open google' in query:
            webbrowser.open("google.com")  

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")     

        elif 'open coursera' in query:
            webbrowser.open("https://www.coursera.org/")              
                        
        elif 'play music' in query:
            music_dir= "F:\\TKWTK" 
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[7]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M") 
            h=strTime[:2]
            m=strTime[3:5]
            if int(h)>12:
                h=str(int(h)-12)
            speak(f"It's{h,m}")  

        elif 'open code' in query:
            path="D:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
            os.startfile(path)

        elif 'jarvis quit' in query:
            speak("Thank you !! have a great day") 
            exit()  

        elif 'hello jarvis how are you'in query:
            speak("I am fine  boss, How are you ?") 

        elif 'I am also fine' in query:
            speak("Glad to hear boss. how may I help you")   

        elif 'send email to sachin' in query:
            try:
                speak("What should I say")
                content=takeCommand  
                to= "sachin19566@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry,Something went wrong")

        elif 'open snake game' in query:
            speak("sure boss")  
            os.startfile("C:\\Users\\admin\\Desktop\\snake game")          


                