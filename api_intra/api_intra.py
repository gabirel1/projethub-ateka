import requests
from fuzzywuzzy import fuzz

class API_INTRA:
    def __init__(self, auth_token):
        self.baseURL = "https://intra.epitech.eu/" + auth_token
        self.auth_token = auth_token

    #### PROFIL ####

    def __request__profil(self):
        r = requests.get(self.baseURL + "/user?format=json")
        return r.json()

    def getName(self):
        return self.__request__profil()["title"]

    def getLogin(self):
        return self.__request__profil()["login"]

    def getPromo(self):
        return self.__request__profil()["promo"]

    def getSemester(self):
        return self.__request__profil()["semester"]

    def getGPA(self):
        return self.__request__profil()["gpa"][0]["gpa"]

    def getLogTime(self):
        return self.__request__profil()["nsstat"]["active"]

    def getCredits(self):
        return str(self.__request__profil()["credits"])

    def getCycle(self):
        return self.__request__profil()["gpa"][0]["cycle"]

    def getNotes(self):
        login = self.getLogin()
        print(f"login : {login}")
        r = requests.get(self.baseURL + "/user/" + login + "/notes?format=json")
        data = r.json()["notes"]
        tab = []
        index = 0
        if (len(tab) <= 10):
            for i in range(data) :
                tab.append({"title": i["title"], "note": i["final_note"]})
        else :
            for i in range(data) :
                index += 1
                if (index > 10) :
                    tab.append({"title": i["title"], "note": i["final_note"]})
        return tab

    def getFlags(self):
        login = self.getLogin()
        print(f"login : {login}")
        r = requests.get(self.baseURL + "/user/" + login + "/flags?format=json")
        data = r.json()
        medals = data["flags"]["medal"]["modules"]
        nb_of_medals = data["flags"]["medal"]["nb"]
        tab = []
        for i in range(nb_of_medals) :
            tab.append(medals[i]["title"])
        return tab

    #### DASHBOARD ####

    def __request__dashboard(self):
        r = requests.get(self.baseURL + "/?format=json")
        return r.json()["board"]

    def __request__dashboard2(self):
        r = requests.get(self.baseURL + "/?format=json")
        return r.json()["history"]

    def getCurrentProjects(self):
        return ' '.join([i["title"] for i in self.__request__dashboard()["projets"]])

    def getCurrentActivities(self):
        return self.__request__dashboard()

    def getCurrentModules(self):
        listModule = [i['title'] for i in self.__request__dashboard()["modules"]]
        return ' '.join(listModule)

    def getLastNotes(self):
        return self.__request__dashboard()["notes"][0]['note']

    def getLastNotification(self):
        return self.__request__dashboard2()[0]["title"]

    def getModules(self):
        return self.__request__dashboard()["modules"]

    def getNotifications(self):
        text = ""
        request = self.__request__dashboard2()
        for i in request :
            text += i["title"]
            text += ". "
        return text

    ### POST METHODS ####

    def checkName(self, module_name) :
        res = self.getCurrentModules()

        for i in res :
            ratio = fuzz.ratio(module_name, i["title"])
            print(ratio)
            if (ratio >= 35):
                print(i["title_link"])
                return i["title_link"]
        return ""

    def register_module(self, module_name) :
        name = self.checkName(module_name)
        if (name == "") :
            return
        print(name)
        requests.post("https://intra.epitech.eu/" + name + "/register?format=json", json="{login:\"" + self.getLogin() +"\"")
        return name

    def unregister_module(self, module_name) :
        name = self.checkName(module_name)
        if (name == "") :
            return name
        requests.post("https://intra.epitech.eu/" + name + "/unregister?format=json", json="{login:\"" + self.getLogin() +"\"")
        return name

    def register_projet(self, module_name) :
        return (200)

    def unregister_projet(self, module_name) :
        return (200)

    def register_activity(self, module_name) :
        return (200)

    def unregister_activity(self, module_name) :
        return (200)
