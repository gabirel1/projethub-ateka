from voice.text_to_voice import VOICE
from api_intra.api_intra import API_INTRA
from commands_class.commands import COMMANDS
import speech_recognition as sr
from fuzzywuzzy import fuzz
import requests

def execFunction(id, INST_API_INTRA):
    switcher = {
        1: INST_API_INTRA.getGPA(),
        2: INST_API_INTRA.getCredits(),
        3: INST_API_INTRA.getLastNotification(),
        4: INST_API_INTRA.getNotifications(),
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(id, "")

def mainFunction(source, VOICE_PLAYER, INST_API_INTRA, COMMANDS):
    audio = r.listen(source)
    text = r.recognize_google(audio, language='fr_FR')

    print("-----")
    print(text)
    print("-----")
    commands = COMMANDS.getCommands()

    # tab = INST_API_INTRA.getFlags()

    # for i in tab:
    #     print(i)
    for i in commands:
        ratio = fuzz.ratio(text, i["sentence"].lower())
        print("-----")
        print(ratio)
        print(i["sentence"].lower())
        print("-----")
        if (ratio > 70) :
            VOICE_PLAYER.__say__(i["toSay"] + execFunction(i["fid"], INST_API_INTRA) + i["toSay2"])
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