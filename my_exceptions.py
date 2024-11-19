class InvalidTypeSocialNetwork(Exception):
    def __init__(self, social_network_type: str) -> None:
        super().__init__(f"Соц.сети {social_network_type} не существует")
class InvalidTypeFileException(Exception):
    def __init__(self, type_file: str) -> None:
        super().__init__(f"Программа не может работать с {type_file} файлами. (Допустимые типы: .json и .xml)")
class InvalidIdUserException(Exception):
    def __init__(self, id_user: str) -> None:
        super().__init__(f"Пользователя с id: {id_user} не существует.")