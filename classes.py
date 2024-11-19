class User:
    id:int
    name:str
    surname:str
    def __init__(self,id: int,name:str,surname:str) -> None:
            self.id=id
            self.name=name
            self.surname=surname
    def info(self) ->None:
         print(f"ID: {self.id},\n"
              f"Name: {self.name},\n"
              f"Surname: {self.surname},\n")
    def to_format(self):
        return {
            "id":self.id,
            "name":self.name,
            "surname":self.surname,
        }
class SocialNetwork:
    network_name:str
    user:User
    def __init__(self,user:User) -> None:
         self.network_name=self.__class__.__name__
         self.user=user
    def to_format(self):
        data = {
            "social network":self.network_name,
            "user":self.user.to_format()
        }
        return data
    def features(self) -> None:
        print(f"{self.network_name}: Основные функции социальной сети.")
class Instagram(SocialNetwork):
    def __init__(self, user: User) -> None:
         super().__init__(user)
    def features(self) -> None:
        print(f"Пользователь {self.user.surname} {self.user.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Публикация фото и видео, Stories(временные публикации), Reels(короткие видео), IGTV(длинные видео), Прямые эфиры")
class Telegram(SocialNetwork):
    def __init__(self, user: User) -> None:
         super().__init__(user)
    def features(self) -> None:
        print(f"Пользователь {self.user.surname} {self.user.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Чаты с шифрованием, Группы, Каналы, Боты, Приватные сообщения и секретные чаты")
class Tiktok(SocialNetwork):
    def __init__(self, user: User) -> None:
         super().__init__(user)
    def features(self) -> None:
        print(f"Пользователь {self.user.surname} {self.user.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Короткие видео с музыкой и фильтрами, Вирусные челленджи, Duet и Stitch (взаимодействие с другими видео), Алгоритм персонализированных рекомендаций, Прямые трансляции")
class Vkontakte(SocialNetwork):
    def __init__(self, user: User) -> None:
         super().__init__(user)
    def features(self) -> None:
        print(f"Пользователь {self.user.surname} {self.user.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Публикация фото, видео, музыки, Ленты новостей, Группы и сообщества, Видео трансляции и стримы, Магазины и оплата через приложение, Истории")
class Snapchat(SocialNetwork):
    def __init__(self, user: User) -> None:
         super().__init__(user)
    def features(self) -> None:
        print(f"Пользователь {self.user.surname} {self.user.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Секретные фото и видео, Snap Map (карта местоположений), Линзы (фильтры и эффекты), Истории, Прямые трансляции, Челленджи и игры с друзьями")
class Facebook(SocialNetwork):
    def __init__(self, user: User) -> None:
         super().__init__(user)
    def features(self) -> None:
        print(f"Пользователь {self.user.surname} {self.user.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Публикация текстов, фото и видео, Истории, Группы по интересам, Прямые эфиры, Marketplace для покупок, Лента новостей, Оповещения о событиях")
class Twitter(SocialNetwork):
    def __init__(self, user: User) -> None:
         super().__init__(user)
    def features(self) -> None:
        print(f"Пользователь {self.user.surname} {self.user.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Краткие твиты (до 280 символов), Хештеги и тренды, Ответы и ретвиты, Прямые трансляции, Лента новостей, Отслеживание событий через твиты")
class Whatsapp(SocialNetwork):
    def __init__(self, user: User) -> None:
         super().__init__(user)
    def features(self) -> None:
        print(f"Пользователь {self.user.surname} {self.user.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Мгновенные текстовые сообщения, Голосовые и видеозвонки, Групповые чаты, Отправка фото, видео и документов, Статусы, Шифрование сообщений")

