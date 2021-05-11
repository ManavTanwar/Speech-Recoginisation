# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:08:17 2020

@author: pushp
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
import time
from datetime import date
from win10toast import ToastNotifier


from capstone import takeCommand, speak


# def speak(audio):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.say(audio)
#     engine.runAndWait()

rem_list= {}
def get_details_about_reminder():
    flag = 0
    speak("What shall I remind you about")
    while(flag ==0):  
        rem = takeCommand().lower()
        if rem !="none":
            flag = 1
            speak(rem)
            
    flag = 0
    speak("on which date")
    while(flag ==0): 
        d = takeCommand().lower()
        if(d !="none"):
            ext = ["th","st","nd","rd"]
            for ex in ext:
                if ex in d:
                    d = d.replace(ex,"")
                    break
            flag = 1
            speak(d)
    speak("At what time")
    flag = 0
    while(flag ==0): 
        t = takeCommand().lower()
        if (t !="none"):
            for i in range(len(t)):
                if(t[i] == "."):
                    t = t[0:i]
                    t = t+"m"
                    break
            t = t.replace(" ","")
            
            s = 0
                    
            flag =1
            speak(t)
            
    if(d in rem_list):
        a = rem_list[d]
        a.extend([t,rem])
        rem_list[d] = a
    else:
        rem_list[d] = [t,rem]
        
        
def show_reminder(reminder):
    # print("enter in show reminders function")
    notification = ToastNotifier()
    speak(reminder)
    notification.show_toast(f"Reminder",reminder,duration = 10)      
        
        
def check_for_reminders():

    today = date.today()
    one = today.strftime("%B %d")
    one = one.lower()
    one = one.replace(" 0"," ")
    
    two = today.strftime("%d %B")
    two = two.lower()
    if(two[0] == "0"):
        two = two.replace("0","")
    
    t = time.localtime()
    current_time = time.strftime("%I:%M %p ", t)
    current_time = current_time.lower()
    if(current_time[0] == "0"):    
        current_time = current_time[1:]
    current_time = current_time.replace(":0",":")
    current_time = current_time.replace(" ", "")
    
    
    if one in rem_list:
        # print("enter in if condition")
        a = rem_list[one]
        i = 0
        l = len(a)
        
        while(i<l):
            # print("a is",a)
            # print("a[i] is :",a[i])
            
            # print("current time is :",current_time)
            
            if(a[i] == str(current_time)):
                # print("enter in check condition",a[i],current_time)
                # print("enter condition")
                show_reminder(a[i+1])
                
            i = i+2
    if two in rem_list:
       # print("enter in elif condition")
        a = rem_list[two]
        i = 0
        l = len(a)
        while(i<l):
            # print("a is",a)
            # print("a[i] is :",a[i])
            
            # print("current time is :",current_time)
           
            if(a[i] ==str(current_time)) :
                # print("enter in check condition",a[i],current_time)
                # print("enter condition")
                show_reminder(a[i+1])
                #print("enter in the if ")
            i = i+2
    else:
        pass




# def takeCommand():
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print('Listening')

#         r.pause_threshold =0.7
#         audio = r.listen(source)

#         try:
#             print("Recognizing")


#             Query = r.recognize_google(audio, language='en-in')
#             print("the command is printed=", Query)

#         except Exception as e:
            
#             speak("I couldn't get it. Please say that again Sir")
#             print("I couldn't get it. Please say that again sir")
#             return "None"

#         return Query

# def Take_query():
#     while(True):
#         query = takeCommand().lower()
        
#         if "set a reminder" in query:
#             get_details_about_reminder()
#             continue
#         elif "bye" in query:
#             speak("Bye. Have a nice day.")
#             print("Bye. Have a nice day.")
#             break
#         elif "none" in query:
#             check_for_reminders()
        
# if __name__ == '__main__':
#     Take_query()

