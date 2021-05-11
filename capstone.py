# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:37:16 2020

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