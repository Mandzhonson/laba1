class User:
    def __init__(self,email,password,nickname):
        self.__email=email
        self.__password = password
        self.__nickname=nickname
        self.__profile=self.Profile()
    def __repr__(self):
        return f"User: {self.__nickname},Info:\n{self.__profile}"
    class Profile:
        def __init__(self):
            self.__name = ""
            self.__surname=""
            self.__BIO=""
            self.__birth_day = ""
        def __repr__(self):
            return f"Name: {self.__name},\nSurname:{self.__surname},\nBIO:{self.__BIO},Birth_day:{self.__birth_day}"
class UserManager:
    pass
class Message:
    pass
class Post:
    pass
class Communities:
    pass
class Video:
    pass
class Music:
    pass
class News:
    pass
class Comments:
    pass
class Photos:
    pass


us1=User('example@checks.com','12345678','  cinly')
print(us1)