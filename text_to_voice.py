import pyttsx3

engine = pyttsx3.init('espeak')
engine.setProperty('rate', 180)
engine.setProperty('voice', 'french')
voices = engine.getProperty('voices')
# for voice in voices:
#   print(voice)
engine.say("Salut comment je peux t'aider ?")

engine.runAndWait()
