import requests


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

    def getCredits(self):
        return str(self.__request__profil()["credits"])

    def getCycle(self):
        return self.__request__profil()["gpa"][0]["cycle"]

    #### DASHBOARD ####

    def __request__dashboard(self):
        r = requests.get(self.baseURL + "/?format=json")
        return r.json()["board"]

    def __request__dashboard2(self):
        r = requests.get(self.baseURL + "/?format=json")
        return r.json()["history"]

    def getCurrentProjects(self):
        return self.__request__dashboard()["board"]["projets"]

    def getCurrentActivities(self):
        return self.__request__dashboard()["board"]["activities"]

    def getCurrentModules(self):
        return self.__request__dashboard()["board"]["activities"]

    def getLastNotes(self):
        return self.__request__dashboard()["board"]["notes"]

    def getLastNotification(self):
        return self.__request__dashboard2()[0]["title"]

    def getNotifications(self):
        text = ""
        request = self.__request__dashboard2()
        for i in request :
            text += i["title"]
            text += ". "
        return text