from voice.text_to_voice import VOICE
from api_intra.api_intra import API_INTRA
from commands_class.commands import COMMANDS
import speech_recognition as sr
from fuzzywuzzy import fuzz
import requests

def mainFunction(source, VOICE_PLAYER, INST_API_INTRA, COMMANDS):
    audio = r.listen(source)
    text = r.recognize_google(audio, language='fr_FR')

    commands = COMMANDS.getCommands()
    for i in commands:
        if (fuzz.ratio(text, i["sentence"].lower()) > 70) :
            VOICE_PLAYER.__say__(i["toSay"])
            break

if __name__ == "__main__":
    r = sr.Recognizer()
    VOICE_PLAYER = VOICE()
    COMMANDS = COMMANDS()
    try :
        auth_token = requests.get("http://localhost:3000/autologin").json()["token"]
        INST_API_INTRA = API_INTRA(auth_token)
    except:
        VOICE_PLAYER.__say__("Merci de renseigner votre clef d'autologin avant de pouvoir utiliser Ateka")
    with sr.Microphone() as source:
        while 1:
            mainFunction(source, VOICE_PLAYER, INST_API_INTRA, COMMANDS)