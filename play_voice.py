import pyttsx3

engine = pyttsx3.init('espeak')
engine.setProperty('rate', 180)
engine.setProperty('voice', 'french')
voices = engine.getProperty('voices')