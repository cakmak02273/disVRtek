import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
from disVRtek_Arayüz.sesyazma import deneme


r = sr.Recognizer()


# class deneme:

#     def sesyaz():
#         with sr.Microphone() as source:
#             audio = r.listen(source)
#             voice = ''
#         try:
#             voice = r.recognize_google(audio, language="tr")
#         except sr.UnknownValueError:
#             speak("söylenen anlaşılamadı")
#         return str(voice)


def record():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ''
    try:
        voice = r.recognize_google(audio, language="tr")
    except sr.UnknownValueError:
        speak("söylenen anlaşılamadı")
    return str(voice)


def response(voice):
    if 'tamamdır' in voice:
        speak("kapanıyorum")
        exit()


def speak(string):
    tts = gTTS(string, lang="tr")
    rnd = random.randint(0, 100)
    file = 'disVRtek/audio'+str(rnd)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("konuş yazayım")
print("Disleksi Metin Etkinlikleri, Disleksi Etkinlik Çalışmaları, Ters ve Düz Harf Algılamaları, Ters Olan Harfleri Algılama, Harften Tersten ve Düzden Okuma")
voice = record()
#voice = deneme.sesyaz()

print(voice)
