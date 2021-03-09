from voice.text_to_voice import VOICE
from api_intra.api_intra import API_INTRA
import speech_recognition as sr
from fuzzywuzzy import fuzz
import requests

def mainFunction(source, VOICE_PLAYER, auth_token):
    audio = r.listen(source)
    text = r.recognize_google(audio, language='fr_FR')
    Ratio = fuzz.ratio(text.lower(), "inscrit moi au projet")
    testGPA = fuzz.ratio(text.lower(), "quel est mon G P A")
    if (testGPA > 70) :
        INST_API_INTRA = API_INTRA(auth_token)
        VOICE_PLAYER.__say__("Tu as " + INST_API_INTRA.getGPA() + "de GPA")
        print(INST_API_INTRA.getGPA())

    print(text)
    print(Ratio)
    VOICE_PLAYER.__say__(text)

if __name__ == "__main__":
    r = sr.Recognizer()
    VOICE_PLAYER = VOICE()
    auth_token = requests.get("http://localhost:3000/autologin").json()["token"]
    # INST_API_INTRA = API_INTRA(auth_token)
    # VOICE_PLAYER.__say__("Tu as " + INST_API_INTRA.getGPA() + "de GPA")
    # print(INST_API_INTRA.getGPA())
    print(auth_token)
    with sr.Microphone() as source:
        while 1:
            mainFunction(source, VOICE_PLAYER, auth_token)
