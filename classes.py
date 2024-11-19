class User:
    network_name:str
    id:int
    name:str
    surname:str
    def __init__(self,id: int,name:str,surname:str) -> None:
         self.network_name=self.__class__.__name__
         self.id=id
         self.name=name
         self.surname=surname
    def to_format(self):
        data = {
            "social_network":self.network_name,
            "id":self.id,
            "name":self.name,
            "surname":self.surname,
        }
        return data
    def features(self) -> str:
        return(f"{self.network_name}: Основные функции социальной сети.")
class Instagram(User):
    def __init__(self,id: int,name:str,surname:str) -> None:
         super().__init__(id,name,surname)
    def features(self) -> str:
        return(f"Пользователь {self.surname} {self.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Публикация фото и видео, Stories(временные публикации), Reels(короткие видео), IGTV(длинные видео), Прямые эфиры")
class Telegram(User):
    def __init__(self,id: int,name:str,surname:str) -> None:
         super().__init__(id,name,surname)
    def features(self) -> str:
        return(f"Пользователь {self.surname} {self.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Чаты с шифрованием, Группы, Каналы, Боты, Приватные сообщения и секретные чаты")
class Tiktok(User):
    def __init__(self,id: int,name:str,surname:str) -> None:
         super().__init__(id,name,surname)
    def features(self) -> str:
        return(f"Пользователь {self.surname} {self.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Короткие видео с музыкой и фильтрами, Вирусные челленджи, Duet и Stitch (взаимодействие с другими видео), Алгоритм персонализированных рекомендаций, Прямые трансляции")
class Vkontakte(User):
    def __init__(self,id: int,name:str,surname:str) -> None:
         super().__init__(id,name,surname)
    def features(self) -> str:
        return(f"Пользователь {self.surname} {self.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Публикация фото, видео, музыки, Ленты новостей, Группы и сообщества, Видео трансляции и стримы, Магазины и оплата через приложение, Истории")
class Snapchat(User):
    def __init__(self,id: int,name:str,surname:str) -> None:
         super().__init__(id,name,surname)
    def features(self) -> str:
        return(f"Пользователь {self.surname} {self.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Секретные фото и видео, Snap Map (карта местоположений), Линзы (фильтры и эффекты), Истории, Прямые трансляции, Челленджи и игры с друзьями")
class Facebook(User):
    def __init__(self,id: int,name:str,surname:str) -> None:
         super().__init__(id,name,surname)
    def features(self) -> str:
        return(f"Пользователь {self.surname} {self.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Публикация текстов, фото и видео, Истории, Группы по интересам, Прямые эфиры, Marketplace для покупок, Лента новостей, Оповещения о событиях")
class Twitter(User):
    def __init__(self,id: int,name:str,surname:str) -> None:
         super().__init__(id,name,surname)
    def features(self) -> str:
        return(f"Пользователь {self.surname} {self.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Краткие твиты (до 280 символов), Хештеги и тренды, Ответы и ретвиты, Прямые трансляции, Лента новостей, Отслеживание событий через твиты")
class Whatsapp(User):
    def __init__(self,id: int,name:str,surname:str) -> None:
         super().__init__(id,name,surname)
    def features(self) -> str:
        return (f"Пользователь {self.surname} {self.name} использует {self.network_name}, так как данная соц.сеть имеет ряд функций: Мгновенные текстовые сообщения, Голосовые и видеозвонки, Групповые чаты, Отправка фото, видео и документов, Статусы, Шифрование сообщений")

