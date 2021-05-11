# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyaudio
import os
from googlesearch import search
import subprocess
import shutil


# from capstone import takeCommand
# from capstone import speak
# from capstone import tellDay
# from capstone import tellTime
# from capstone import Hello
# from access_path import OS_PATH
# from reminders import get_details_about_reminder
# from reminders import show_reminder
# from reminders import check_for_reminders




class OS_PATH():
    DIR = ""
    last_query = ""
    def __init__(self, path = "C:"):
        self.DIR = path
    
    def Start(self):
        query = ""
        while(True):
            if("list contents" in query):
                self.list_dir_contents()
            elif("change directory" in query):
                content = self.list_dir_contents()
                content[len(content.keys())+2] = 'Go back...'
                speak("tell me which folder number you want to move to.")
                print("tell me which folder number you want to move to.")

                #command = takeCommand().lower()
                command = input("change dir")
                if(int(command) in content.keys()):
                    self.change_dir(content[int(command)])
                else:
                    speak("please tell the correct option")

            elif("delete" in query and "file" in query):
                content = self.list_dir_contents()
                speak("tell me which file number you want to delete.")
                print("tell me which file number you want to delete.")

                #command = takeCommand().lower()
                command = input("delete")
                if(int(command) in content.keys()):
                    self.remove_file(content[int(command)])
                else:
                    speak("please tell the correct option")

            elif("delete" in query and "folder" in query):
                content = self.list_dir_contents()
                speak("tell me which folder number you want to delete.")
                print("tell me which folder number you want to delete.")

                #command = takeCommand().lower()
                command = input("delete")
                if(int(command) in content.keys()):
                    self.remove_folder(content[int(command)])
                else:
                    speak("please tell the correct option")

            elif("stop" in query):
                break

            speak("tell me what we have to do.")
            query = takeCommand().lower()

    def change_dir(self, folder_name = ""):
        if(folder_name == ""):
            speak("Specify the folder name Sir.")
            print("Specify the folder name Sir.")
        elif(os.path.isdir(self.DIR+"\\"+folder_name)):
            self.DIR = self.DIR+"\\"+folder_name
            speak("changed the directory.")
            print(self.DIR)
        elif(folder_name == "Go back..."):
            self.DIR = os.path.dirname(self.DIR)
            speak("changed the directory.")
            print(self.DIR)

    def list_dir_contents(self):
        Content = {}
        c = 1
        for i in os.listdir(self.DIR):
            print(c, ". "+i)
            Content[c] = i
            c += 1
        return Content


    def remove_file(self, file_name = ""):
        if(file_name == "" or "." not in file_name):
            speak("Specify the file name Sir.")
            print("Specify the file name Sir.")
        elif(os.path.exists(self.DIR+"\\"+file_name)):
            speak("Do you want to delete the file "+file_name)
            print("Do you want to delete the file "+file_name)
            print("waiting for confirmation.....say yes or no.")
            command = takeCommand().lower()
           
            while('yes' not in command and 'no' not in command):
                command = takeCommand().lower()
                
            if('yes' in command):
                
                os.remove(self.DIR+"\\"+file_name)
                speak("deleted the file "+file_name)
        else:
            speak("I think the file do not exist sir. Look whether we are in the right directory.")
            print(self.DIR)

    def remove_folder(self, folder_name = ""):
        if(folder_name == ""):
            speak("Specify the folder name Sir.")
            print("Specify the folder name Sir.")
        elif(os.path.exists(self.DIR+"\\"+folder_name)):
            speak("Do you want to delete the folder "+folder_name)
            print("Do you want to delete the folder "+folder_name)
            print("waiting for confirmation.....say yes or no.")
            command = takeCommand().lower()
            
            while('yes' not in command and 'no' not in command):
                command = takeCommand().lower()
                
            if('yes' in command):
                shutil.rmtree(self.DIR+"\\"+folder_name)
                speak("deleted the folder "+folder_name)
        else:
            speak("I think the folder do not exist sir. Look whether we are in the right directory.")
            print(self.DIR)

    
            


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold =0.7
        audio = r.listen(source)

        try:
            print("Recognizing")


            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            
            speak("I couldn't get it. Please say that again Sir")
            print("I couldn't get it. Please say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():

    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    print("The time is sir" + hour + "Hours and" + min + "Minutes")
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")


def Hello():
    speak("hello sir I am Friday. Tell me how may I help you")




def Take_query():
    Hello()
    while (True):
        # check_for_reminders()
        query = takeCommand().lower()
        if "go to" in query:
            speak("Opening")
            query_web = ""
            for i in query.split(" "):
                if(".com" in i or ".in" in i or ".co.in" in i):
                    query_web = i
            if(query_web != ""):
                webbrowser.open("www."+query_web)
            continue
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif "which day it is" in query:
            tellDay()
            continue
        elif "tell me the time" in query:
            tellTime()
            continue
        elif "bye" in query:
            speak("Bye. Have a nice day.")
            print("Bye. Have a nice day.")
            break
        elif "open notepad" in query:
            speak("Opening notepad")
            print("Opening notepad")
            os.system("notepad")
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            continue
        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)
            continue
        elif "tell me your name" in query:
            speak("I am Friday. Your deskstop Assistant")      
        elif "search" in query:
            query_web = query
            i = 0
            speak("here are some suggested results for the query")
            print("here are some suggested results for the query")
            for j in search(query_web, tld="co.in", num=10, stop=10, pause=2):
                if(i == 0):
                    webbrowser.open(j)
                    i +=1
                else: 
                    print("search by command open urlname")
                    print(j)
            continue
        elif "open calculator" in query:
            speak("Opening Calculator")
            print("Opening Calculator")
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            continue
        elif("directory" in query):
            speak("Please tell me the base directory")
            print("Please tell me the base directory")
            direc = takeCommand().lower()
            while(direc=="none"):
                direc = takeCommand().lower()
            if("e" in direc.split()):
                obj = OS_PATH("E:\\")
                obj.Start()
                speak("stopped accessing the directory")
                print("stopped accessing the directory")
            elif("c" in direc.split()):
                obj = OS_PATH("C:\\")
                obj.Start()
                speak("stopped accessing the directory")
                print("stopped accessing the directory")
            elif("d" in direc.split()):
                obj = OS_PATH("D:\\")
                obj.Start()
                speak("stopped accessing the directory")
                print("stopped accessing the directory")
            else:
                speak("no directory specified")
                print("no directory specified")
        # elif("set a reminder" in query):
        #     get_details_about_reminder()
        #     continue
            
        # else:
        #     check_for_reminders()
            
if __name__ == '__main__':
    Take_query()


