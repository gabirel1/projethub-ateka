import pyttsx3

class VOICE:
    def __init__(self):
        self.engine = pyttsx3.init('espeak')
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('voice', 'french')
        self.voices = self.engine.getProperty('voices')

    def __say__(self, message):
        self.engine.say(message)
        self.engine.runAndWait()