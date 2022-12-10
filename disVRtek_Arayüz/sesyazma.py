import speech_recognition as sr

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     audio = r.listen(source)
#     voice = r.recognize_google(audio, language="tr-TR")
#     print(voice)


class sesisle:
    

    def sesyaz():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            voice = r.recognize_google(audio, language="tr-TR")
            # print(voice)
        return voice
