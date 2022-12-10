from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os


def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "disVRtek/answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("hava çok sıcak")
