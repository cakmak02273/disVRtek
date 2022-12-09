import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
r = sr.Recognizer()


def record():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ''
    try:
        voice = r.recognize_google(audio, language='tr-TR')
    except sr.UnknownValueError:
        speak("söylenen anlaşılamadı")
    return voice


def response(voice):
    if 'tamamdır' in voice:
        speak("kapanıyorum")
        exit()


def speak(string):
    tts = gTTS(string, lang='tr')
    rnd = random.randint(0, 100)
    file = 'audio'+str(rnd)+"mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("konuş yazayım")
voice = record()
print(voice)
speak("yazdım")
