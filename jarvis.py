import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I am Veneca! Please tell me how may I help you")


def takeCommand():
    # it takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password")
    server.sendmail("yourmail@gmail.com", to, content)
    server.close()

# def createList():
#     while True:

#         if listIt is not None:
#             commandList.append.listIt()

#         if listIt is not None and listIt.lower() == "stop":
#             break
#         else:
#             print("Cannot rcognize your voice")

def addIn(item):
    with open("to_do_list.txt", "a") as file:
        file.write(item + "\n")

def printToDoList():
    try:
        with open("to_do_list.txt","r") as file:
            print("Your to-do list:")
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        speak("There is some error.Icannot file your file.")
        print("Error:File not found!")


if __name__ == "__main__":
    wishMe()
while True:
    if 1:
        query = takeCommand().lower()

        # logics to execute task based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            webbrowser.open("youtube.com")
            speak("Ok ma'am Opening youtube")
            print("opening youtube")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "open brave" in query:
            webbrowser.open("brave.com")

        elif "play music" in query:
            speak("which website would yoy prefer to listen music?")
            if "youtube music" in query:
                webbrowser.open("youtubemusic.com")
            else:
                music_dir = "C:\\Users\\Admin\\Music"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Maam, The time is {strTime}")

        elif "open VS code" in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "email to " in query:
            try:
                speak("What shouls i say...")
                content = takeCommand()
                to = "Shrutikaag01@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry your email has not been sent there is some error")

        elif "to do list" in query:
            try:
                speak("Tell me what should I add in your list")
                listIt = takeCommand()
                addIn(listIt)
                speak(f"Your list has been created.{listIt}")

                if "print to do list" in query:
                    speak("printing your to do list")
                    print("printing...")
                    printToDoList()

            except Exception as e:
                print(e)
                speak("Sorry your voice is not recognizable")

        elif "stop" in query:
            speak("Sure! Goodbye.I hope it was helpful")
            break

        elif "please quit" in query or "exit" in query:
            myList = [
                "Thank you for using me",
                "Okay,Goodbye ma'am",
                "It was pleasure talking to you",
            ]
            randBye = random.choice(myList)
            speak(randBye)
            print(randBye)
            exit()

        # else :
        #     speak("sorry I couldn't find anything related to what you said.Would you like to know something else")
        #     print("sorry! please say again")
        #     if 'yes' in query :
        #         word = takeCommand()
        #     eli
