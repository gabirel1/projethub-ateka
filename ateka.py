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
        5: INST_API_INTRA.getCurrentProjects(),
        6: INST_API_INTRA.getCurrentActivities(),
        7: INST_API_INTRA.getCurrentModules(),
        8: INST_API_INTRA.getLastNotes(),
        # 9: INST_API_INTRA.getLastNotification(),
        # 10: INST_API_INTRA.getLastNotes(),
        # 11: "November",
        # 12: "December"
    }
    return switcher.get(id, "")

def mainFunction(source, VOICE_PLAYER, INST_API_INTRA, COMMANDS):
    audio = r.listen(source)
    text = r.recognize_google(audio, language='fr_FR')

    print("-----")
    print(text)
    print("-----")
    commands = COMMANDS.getCommands()

    ratio1 = fuzz.ratio(text, "inscrit moi au module xxx")
    if (ratio1 > 50):
        VOICE_PLAYER.__say__("vous avez bien ete inscrit au module " + INST_API_INTRA.register_module(text[-10:]) + " ")
        return
    # ratio2 = fuzz.ratio(text, "inscrit moi au projet xxx")
    # ratio3 = fuzz.ratio(text, "inscrit moi a l'activite xxx")
    ratio4 = fuzz.ratio(text, "desinscrit moi du module xxx")
    if (ratio4 > 50):
        VOICE_PLAYER.__say__("vous avez bien ete desinscrit au module " + INST_API_INTRA.unregister_module(text[-10:]) + " ")# ratio5 = fuzz.ratio(text, "desinscrit moi du projet xxx")
        return
    # ratio6 = fuzz.ratio(text, "desinscrit moi de l'activite xxx")


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