class person:
    __name = ''
    __email = ''


    def __init__(self,name, email):
        self.__name = name
        self.__email = email


    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setemail(self, email):
        self.__email = email

    def getname(email):
        return self.__email

Angelo = person("Angelo Hastings","angelos email")

print(Angelo.getname)