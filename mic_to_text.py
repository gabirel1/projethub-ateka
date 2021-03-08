import speech_recognition as sr
from fuzzywuzzy import fuzz

def mainFunction(source):
  audio = r.listen(source)
  text = r.recognize_google(audio, language='fr_FR')
  Ratio = fuzz.ratio(text.lower(), "inscrit moi au projet")
  print(text)
  print(Ratio)


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainFunction(source)