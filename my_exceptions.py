class InvalidTypeFileException(Exception):
    def __init__(self, name_file: str) -> None:
        super().__init__(f"Программа не может работать с файлами типа '{name_file}'. (Допустимые типы: .json и .xml)")


class InvalidIdException(Exception):
    def __init__(self, id_value: int) -> None:
        super().__init__(f"Объект с ID {id_value} не найден.")
