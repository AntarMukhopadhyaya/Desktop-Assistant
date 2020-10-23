'''

Author: Antar Mukhopadhyaya
Created On: 21/10/2020
Github Link: https://github.com/arun199941/Desktop-Assistant/blob/main
You are free to use this script wherever you want and can add any feature you want....




'''


import pyttsx3,datetime,wikipedia,webbrowser,os,sys,smtplib, socket
import speech_recognition as sr
from googlesearch import  search

# Initializing pyttsx3 engine
engine = pyttsx3.init()


# _________________ Important functions ____________________________

def speak(audio):
    # Function Responsible for speaking
    engine.say(audio)
    engine.runAndWait()

def internetConnectionStatus(host="8.8.8.8", port=53, timeout=3):
    # Checks Whether internet connectivity is avail or not
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host,port))
        speak("Internet Connectivity Detected")
    except  socket.error as e:

        speak("Internet Connection Not detected")
        speak(" Make Sure you are connected to internet")
        sys.exit()



def time():
    # Tells Current Time
    currentTime = datetime.datetime.now().strftime("%I: %M : %S")
    speak("The Current Time is" + currentTime)




def date():
    # Tells Current Date
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    speak("Todays date is")
    speak(day)
    speak(month)
    speak(year)



def greet():
    # Greets The User
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour < 12:
        speak("Good Morning Master")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Master")
    elif hour >=18 and hour < 20:
        speak("Good Evening Master")
    else:
        speak("Good Night Sir")
    time()
    speak("and")


def takeCommand():
    # Speech Recognition Function
    # Make sure you are loud and clear
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that Again Please")
        return "None"
    return query

# Beta Stage
def sendEmail(to,content):
    # Send Email to desired User
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    masters_email = 'your email'
    server.login(masters_email, 'password')# make sure u import the password from another text file for better security
    server.sendmail(masters_email,to,content)
    server.close()
# Beta
def googleSearch(query):
    # Searches your query in google
    for j in search(query, tld='co.in', num=1, stop=10,pause=2):
        print(j)
        webbrowser.open(j)

if __name__ == "__main__":
    internetConnectionStatus()
    greet()
    date()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            # print(results) If you want to print the result in terminal then uncomment this line
            speak(results)
        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open('google.com')
        elif 'open stack overflow' in query:
            # If you are a programmer then you need this
            speak("Opening StackOverFlow")
            webbrowser.open('stackoverflow.com')
        elif 'open gmail' in query:
            # Open Gmail
            speak("Opening Gmail ...")
            webbrowser.open('mail.google.com')
        elif 'who are you' in query:
            # General Interaction
            speak(" I am Wilbert")
            speak("Masters AI assistant ")
            speak("Nice to meet you")
        elif 'play music' in query:
            # Play Music
            music_directory = "D:\\Music" #Please Change this According to your Music Directory

            songs = os.listdir(music_directory)
            print(songs)
            os.startfile(os.path.join(music_directory, songs[0]))
        elif 'the time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'close' in query:
            # CLoses the assistant
            speak('Thank you Master')
            speak('Closing Time')
            time()
            sys.exit()
        elif 'open vscode' in query:
            # Open Vscode
            speak("Opening Vscode...")
            os.startfile("C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'send email' in query:
            try:
                # Error handling
                speak("What shoud I say")
                content = takeCommand()
                speak("Please input the email address you want to send the email to")
                to = str(input("Enter Email"))
                sendEmail(to, content)
                speak("Email has sent Sucessfully")
            except Exception as e:
                print(e)
                speak("Sorry Master I cannot send email at this moment")
        elif 'google'in query:
            query = query.replace('google','')
            speak(f"Searching google for {query}\n ")
            print(query)
            googleSearch(query)
        elif 'notepad' in query:
            # Open Notepad
            speak("Opening Notepad...")
            os.startfile("C:\Windows\System32\\notepad.exe")
