class COMMANDS :
    def __init__(self):
        self.commands = [
            {"sentence": 'quel est mon G P A', "fid": 1, "toSay": 'tu as', "toSay2": 'de GPA'},
            {"sentence": "combien est ce que j'ai de credits", "fid": 2, "toSay": 'tu as', "toSay2": 'credits'},
            {"sentence": 'Lis moi ma derniere notification', "fid": 3, "toSay": " ", "toSay2": " "},
            {"sentence": 'Lis moi toutes mes notifications', "fid": 4, "toSay": " ", "toSay2": " "},
            {"sentence": 'Quels sont mes projets en cours', "fid": 5, "toSay": 'Vous travaillez actuellement sur', "toSay2": ' '},
            {"sentence": 'Quels sont mes activités', "fid": 6, "toSay": 'Vous avez actuellement', "toSay2": ' '},
            {"sentence": 'Quels sont mes modules', "fid": 7, "toSay": 'Vous travaillez actuellement sur ', "toSay2": ' '},
            {"sentence": 'Quelle est ma derniere note', "fid": 8, "toSay": 'Vous avez eu ', "toSay2": ' '},
            # {"sentence": 'yo', "fid": 9, "toSay": 'salut', "toSay2": ''},
            # {"sentence": 'yo', "fid": 10, "toSay": 'salut', "toSay2": ''},
            # {"sentence": 'yo', "fid": 11, "toSay": 'salut', "toSay2": ''},
            # {"sentence": 'yo', "fid": 12, "toSay": 'salut', "toSay2": ''},
            # {"sentence": 'yo', "fid": 13, "toSay": 'salut', "toSay2": ''},
            # {"sentence": 'yo', "fid": 14, "toSay": 'salut', "toSay2": ''},
            # {"sentence": 'yo', "fid": 15, "toSay": 'salut', "toSay2": ''},
            # {"sentence": 'yo', "fid": 16, "toSay": 'salut', "toSay2": ''},
        ]

    def getCommands(self):
        return self.commands