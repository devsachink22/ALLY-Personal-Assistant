import speech_recognition as sr
import pyttsx3
import datetime
import random
import webbrowser
import cv2
import socket
import os
import time
import pyautogui
import pyaudio
import requests
import sys
import wikipedia

u=pyttsx3.init()

def say(audio):
    print(audio)
    u.say(audio)
    u.runAndWait()

def speak(audio):
    print("Answer:",audio)
    u.say(audio)
    u.runAndWait()

current_time=datetime.datetime.now()
current_time.hour
print(str(current_time))

if current_time.hour<12:
    say("Good Morning Sir.")
    say("Welcome to an ALLY Assistant using JARVIS.")
    say("How can I help You?")

elif 12<=current_time.hour<18:
    say("Good Afternoon Sir.")
    say("Welcome to an ALLY Assistant using JARVIS.")
    say("How can I help You?")

elif 18<=current_time.hour<21:
    say("Good Evening Sir.")
    say("Welcome to an ALLY Assistant using JARVIS.")
    say("How can I help You?")

else:
    say("Good Night Sir.")
    say("Welcome to an ALLY Assistant using JARVIS.")
    say("How can I help You?")

def mycommand():
    r=sr.Recognizer()
    s=sr.Microphone()
    t=sr.UnknownValueError

    with s as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        r.pause_threshold=1

    try:
        command=r.recognize_google(audio)
        print("You speak:",command)
    except t:
        say("Sorry sir! I didn't recognize your question! Try typing the command.")
        command=str(input("Command:"))

    return command

def jarvis(command):
    if "Hello" in command or "hello" in command or "Hi" in command or "hi" in command:
        string1=("Hello, here you can ask questions.","Hi, here you can ask questions.")
        speak(random.choice(string1))

    elif "How are you" in command or "how are you" in command or "What's up" in command or "what's up" in command:
        string2=("I am fine.","Nice.")
        speak(random.choice(string2))

    elif "What is my name" in command or "what is my name" in command or "What's my name" in command or "what's my name" in command or "My name" in command or "my name" in command:
        speak("Your name is Sachin Kumar.")

    elif "What is my Father's name" in command or "what is my father's name" in command or "what is my father name" in command or "What's my Father's name" in command or "what's my father's name" in command or "what's my father name" in command or "My Father's name" in command or "my father's name" in command or "my father name" in command:
        speak("Your father's name is Rajinder Kumar.")

    elif "What is my Mother's name" in command or "what is my mother's name" in command or "what is my mother name" in command or "What's my Mother's name" in command or "what's my mother's name" in command or "what's my mother name" in command or "My Mother's name" in command or "my mother's name" in command or "my mother name" in command:
        speak("Your mother's name is Premlata.")

    elif "How old am I" in command or "how old am i" in command or "My age" in command or "my age" in command:
        string3=("I am 19 years old.","My age is 19 years old.")
        speak(random.choice(string3))

    elif "open Firefox" in command or "open firefox" in command:
        say("Ok sir, I got. Please wait for a second.")
        webbrowser.open("Firefox")

    elif "open Gmail" in command or "open gmail" in command:
        say("Ok sir, I got. Please wait for a second.")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    elif "open Facebook" in command or "open facebook" in command or "open FB" in command or "open fb" in command:
        say("Ok sir, I got. Please wait for a second.")
        webbrowser.open("https://www.facebook.com/")

    elif "open Instagram" in command or "open instagram" in command:
        say("Ok sir, I got. Please wait for a second.")
        webbrowser.open("https://www.instagram.com/?hl=en")

    elif "Navigation" in command or "navigation" in command or "start Navigation" in command or "start navigation" in command or "get Directions" in command or "get directions" in command:
        say("Ok sir, I got. Please wait for a second.")
        webbrowser.open("https://www.google.com/maps/dir/")

    elif "open YouTube" in command or "open youtube" in command or "open You Tube" in command or "open you tube" in command:
        say("Ok sir, I got. Please wait for a second.")
        webbrowser.open("https://www.youtube.com/")


    elif "open Camera" in command or "open camera" in command or "open My Webcam" in command or "open my webcam" in command or "open Webcam" in command or "open webcam" in command:
        say("Ok sir, I got. Please wait for a second.")
        def show_webcam(mirror=False):
            cam=cv2.VideoCapture(0)
            while True:
                ret_val,img=cam.read()
                if mirror:
                    img=cv2.flip(img,1)
                cv2.imshow("Camera",img)
                if cv2.waitKey(1)==27:
                    break
            cv2.destroyAllWindows()
        def main():
            show_webcam(mirror=True)
        if __name__=="__main__":
            main()

    elif "check System Information" in command or "check system information" in command or "get System Information" in command or "get system information" in command:
        hostname=socket.gethostname()
        IPAddr=socket.gethostbyname(hostname)
        say("Your Computer's Name is:")
        speak(hostname)
        say("Your Computer's IP Address is:")
        speak(IPAddr)

    elif "Play Music" in command or "play music" in command or "Play Songs" in command or "play songs" in command:
        music_folder=("C:\\Users\\DELL\\Desktop\\Songs\\")
        music=["a","b","c","d","e","f"]
        random_music=music_folder+random.choice(music)+".mp3"
        os.system(random_music)
        say("Ok sir, here is your music. Enjoy!")

    elif "Go to C Drive" in command or "go to C drive" in command or "go to c drive" in command or "Open C Drive" in command or "open C drive" in command or "open c drive" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:")

    elif "Go to D Drive" in command or "go to D drive" in command or "go to d drive" in command or "Open D Drive" in command or "open D drive" in command or "open d drive" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("D:")

    elif "Go to E Drive" in command or "go to E drive" in command or "go to e drive" in command or "Open E Drive" in command or "open E drive" in command or "open e drive" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("E:")

    elif "Go to F Drive" in command or "go to F drive" in command or "go to f drive" in command or "Open F Drive" in command or "open F drive" in command or "open f drive" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("F:")

    elif "Go to Command Prompt" in command or "go to Command Prompt" in command or "go to command prompt" in command or "Open Command Prompt" in command or "open Command Prompt" in command or "open command prompt" in command or "Open CMD" in command or "open CMD" in command or "open cmd" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt")

    elif "Go to Control Panel" in command or "go to Control Panel" in command or "go to control panel" in command or "Open Control Panel" in command or "open Control Panel" in command or "open control panel" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel")

    elif "Go to My Computer" in command or "go to My Computer" in command or "go to my computer" in command or "Open My Computer" in command or "open My Computer" in command or "open my computer" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\This PC")

    elif "Go to Recycle Bin" in command or "go to Recycle Bin" in command or "go to recycle bin" in command or "Open Recycle Bin" in command or "open Recycle Bin" in command or "open recycle bin" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Recycle Bin")

    elif "Go to Run" in command or "go to Run" in command or "go to run" in command or "Open Run" in command or "open Run" in command or "open run" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run")

    elif "Go to Calculator" in command or "go to Calculator" in command or "go to calculator" in command or "Open Calculator" in command or "open Calculator" in command or "open calculator" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Calculator")

    elif "Go to Calendar" in command or "go to Calendar" in command or "go to calendar" in command or "Open Calendar" in command or "open Calendar" in command or "open calendar" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Calendar")

    elif "Go to Excel" in command or "go to Excel" in command or "go to excel" in command or "Open Excel" in command or "open Excel" in command or "open excel" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Excel")

    elif "Go to PowerPoint" in command or "go to PowerPoint" in command or "go to powerpoint" in command or "Open PowerPoint" in command or "open PowerPoint" in command or "open powerpoint" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\PowerPoint")

    elif "Go to Word" in command or "go to Word" in command or "go to word" in command or "Open Word" in command or "open Word" in command or "open word" in command:
        say("Ok sir, I got. Please wait for a second.")
        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Word")

    elif "Start Timer" in command or "start Timer" in command or "start timer" in command or "Start Stopwatch" in command or "start Stopwatch" in command or "start stopwatch" in command:
        startTimer=input("Press enter to start the timer.")
        say("The timer has started.")
        start=time.time()
        endTimer=input("Press enter to stop the timer.")
        end=time.time()
        say("The timer has stopped.")
        elapsed=end-start
        elapsed=str(elapsed)
        speak("The time elapsed is "+elapsed+" seconds.")

    elif "Capture Screenshot" in command or "Capture screenshot" in command or "capture screenshot" in command or "Click Screenshot" in command or "Click screenshot" in command or "click screenshot" in command or "Click a Screenshot" in command or "Click a screenshot" in command or "click a screenshot" in command or "Take a Screenshot" in command or "Take a screenshot" in command or "take a screenshot" in command:
        say("Ok sir, I got. Please wait for a second.")
        pic=pyautogui.screenshot()
        filename=input("Enter the file name to save the screenshot:")
        output=filename+".png"
        pic.save(output)
        say("Your screenshot has been successfully saved.")
        os.startfile("C:\\Users\\DELL\\PycharmProjects\\Advanced Python Projects\\"+output)

    elif "Start Recording" in command or "Start recording" in command or "start recording" in command:
        say("Ok sir, I got. Please wait for a second.")
        filename=input("Enter the file name to save the recording:")
        FORMAT=pyaudio.paInt16
        CHANNELS=2
        RATE=44100
        CHUNK=1024
        RECORD_SECONDS=5
        output=(filename+".wav")
        audio=pyaudio.PyAudio()
        stream=audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
        print("Recording....")
        frames=[]
        for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
            data=stream.read(CHUNK)
            frames.append(data)
        say("Your recording has been successfully saved.")
        os.startfile("C:\\Users\\DELL\\PycharmProjects\\Advanced Python Projects\\"+output)

    elif "Check Current Temperature" in command or "Check current temperature" in command or "check current temperature" in command or "Check Temperature" in command or "Check temperature" in command or "check temperature" in command or "Check Current Weather" in command or "Check current weather" in command or "check current weather" in command or "Check Weather" in command or "Check weather" in command or "check weather" in command:
        say("Ok sir, I got. Please wait for a second.")
        api_address="http://api.openweathermap.org/data/2.5/weather?appid=a5cdd5b81160a2eb8247658da386a49c&q="
        city=input("Enter city name:")
        url=api_address+city
        json_data=requests.get(url).json()
        weather=json_data["weather"][0]["main"]
        temp_k=float(json_data["main"]["temp"])
        temp_f=(temp_k-273.15)*1.8+32
        temp_c=(temp_f-32)*5/9
        pressure=float(json_data["main"]["pressure"])
        humidity=float(json_data["main"]["humidity"])
        say("Weather:")
        speak(weather)
        say("Temperature in °C:")
        speak(temp_c)
        say("Pressure in mb:")
        speak(pressure)
        say("Humidity in percentage:")
        speak(humidity)

    elif "where I am" in command or "where i am" in command or "where am I" in command or "where am i" in command or "check my Location" in command or "check my location" in command:
        say("Ok sir, I got. Please wait for a second.")
        res=requests.get("https://ipinfo.io/")
        data=res.json()
        city=data["city"]
        region=data["region"]
        postal = data["postal"]
        country=data["country"]
        location=data["loc"].split(",")
        latitide=location[0]
        longitude=location[1]
        say("City: "+city)
        say("Region: "+region)
        say("Postal: " + postal)
        say("Country: "+country)
        say("Latitude: "+latitide)
        say("Longitude: "+longitude)

    elif "check my Network IP" in command or "check my network IP" in command or "check my network ip" in command:
        say("Ok sir, I got. Please wait for a second.")
        ip_request=requests.get("https://get.geojs.io/v1/ip.json")
        my_ip=ip_request.json()["ip"]
        say("Your Network's IP Address is:")
        speak(my_ip)

    elif "Nothing" in command or "nothing" in command or "Abort" in command or "abort" in command or "Stop" in command or "stop" in command or "Stop Working" in command or "stop Working" in command or "stop working" in command:
        say("Ok sir.")
        sys.exit()

    elif "Ok Bye" in command or "ok bye" in command or "Ok" in command or "ok" in command or "Bye" in command or "bye" in command:
        say("Ok bye sir, have a nice day.")
        sys.exit()

    else:
        command=command
        say("Searching....")
        try:
            result=wikipedia.summary(command,sentences=4)
            say("Ok sir, I got. Please wait for a second.")
            say("Wikipedia says:")
            speak(result)
        except:
            webbrowser.open("https://www.google.com/")

while True:
    command=mycommand()
    jarvis(command)
    say("Next Command! Sir:")