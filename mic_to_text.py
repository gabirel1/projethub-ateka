import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
  try :
    r.adjust_for_ambient_noise(source)
    data = r.record(source, duration=2)
    text = r.recognize_google(data, language='fr')
    print(text)
  except:
    print('error')
