import speech_recognition as sr

# with sr.Microphone() as source:
#   try :
#     r.adjust_for_ambient_noise(source)
#     data = r.record(source, duration=2)
#     text = r.recognize_google(data, language='fr')
#     print(text)
#   except:
#     print('error')

def mainFunction(source):
  audio = r.listen(source)
  text = r.recognize_google(audio, language='fr_FR')
  print(text)


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainFunction(source)