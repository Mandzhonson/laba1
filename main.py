from data_storage import ProfileManager
from classes import *
from my_exceptions import InvalidIdException, InvalidTypeFileException


def interface_info():
    print("\nВыберите действие:")
    print("1. Создать профиль пользователя")
    print("2. Добавить данные (фото, видео, пост)")
    print("3. Обновить данные (фото, видео, пост)")
    print("4. Удалить данные (фото, видео, пост)")
    print("5. Удалить профиль пользователя")
    print("6. Вывести информацию о пользователе по ID")
    print("7. Вывести информацию обо всех пользователях")
    print("8. Сохранить данные в JSON")
    print("9. Загрузить данные из JSON")
    print("10. Сохранить данные в XML")
    print("11. Загрузить данные из XML")
    print("0. Выход")


def main():
    manager = ProfileManager()

    while True:
        interface_info()
        choice = input("Введите номер действия: ")

        if choice == "0":
            print("Выход из программы.")
            break

        try:
            match choice:
                case "1":
                    name = input("Введите имя пользователя: ")
                    surname = input("Введите фамилию пользователя: ")
                    if not name or not surname:
                        print("Имя и фамилия не могут быть пустыми.")
                    else:
                        manager.create_profile(name, surname)

                case "2":
                    try:
                        user_id = int(input("Введите ID пользователя: "))
                        profile = manager.get_profile_by_id(user_id)
                        print("Что добавить?\n1. Фото\n2. Видео\n3. Пост")
                        add_choice = input("Выберите тип: ")
                        match add_choice:
                            case "1":
                                file_name = input("Введите имя файла фото: ")
                                profile.add_photo(file_name)
                                print(f"Фото успешно добавлено: {file_name}!")
                            case "2":
                                file_name = input("Введите имя файла видео: ")
                                duration = int(
                                    input("Введите продолжительность видео в секундах: "))
                                profile.add_video(file_name, duration)
                                print(f"Видео успешно добавлено: {file_name}!")
                            case "3":
                                content = input("Введите содержание поста: ")
                                profile.add_post(content)
                                print(f"Пост создан: {content}")
                    except (InvalidIdException, ValueError) as err:
                        print(f"Error: {err}")

                case "3":
                    try:
                        user_id = int(input("Введите ID пользователя: "))
                        profile = manager.get_profile_by_id(user_id)
                        print("Что обновить?\n1. Фото\n2. Видео\n3. Пост")
                        update_choice = input("Выберите тип: ")
                        match update_choice:
                            case "1":
                                photo_id = int(input("Введите ID фото: "))
                                profile.read_by_id(photo_id=photo_id)
                                new_name = input("Введите новое имя: ")
                                profile.update_photo(photo_id, new_name)
                            case "2":
                                video_id = int(input("Введите ID видео: "))
                                profile.read_by_id(video_id=video_id)
                                new_name = input("Введите новое имя: ")
                                profile.update_video(video_id, new_name)
                            case "3":
                                post_id = int(input("Введите ID поста: "))
                                profile.read_by_id(post_id=post_id)
                                new_content = input(
                                    "Введите новое содержание: ")
                                profile.update_post(post_id, new_content)
                    except (InvalidIdException, ValueError) as err:
                        print(f"Error: {err}")

                case "4":
                    try:
                        user_id = int(input("Введите ID пользователя: "))
                        profile = manager.get_profile_by_id(user_id)
                        print("Что удалить?\n1. Фото\n2. Видео\n3. Пост")
                        delete_choice = input("Выберите тип: ")
                        match delete_choice:
                            case "1":
                                photo_id = int(input("Введите ID фото: "))
                                profile.read_by_id(photo_id=photo_id)
                                profile.delete_photo(photo_id)
                            case "2":
                                video_id = int(input("Введите ID видео: "))
                                profile.read_by_id(video_id=video_id)
                                profile.delete_video(video_id)
                            case "3":
                                post_id = int(input("Введите ID поста: "))
                                profile.read_by_id(post_id=post_id)
                                profile.delete_post(post_id)
                    except (InvalidIdException, ValueError) as err:
                        print(f"Error: {err}")
                case "5":
                    try:
                        user_id = int(input("Введите ID пользователя: "))
                        profile = manager.get_profile_by_id(user_id)
                        manager.delete_profile(user_id)
                        print(f"Профиль с ID {user_id} удален.")
                    except (InvalidIdException, ValueError) as err:
                        print(f"Error: {err}")
                case "6":
                    try:
                        user_id = int(input("Введите ID пользователя: "))
                        profile = manager.get_profile_by_id(user_id)
                        print(profile)
                    except (InvalidIdException, ValueError) as err:
                        print(f"Error: {err}")
                case "7":
                    if not manager.profiles:
                        print("Нет зарегистрированных пользователей.")
                    else:
                        for profile in manager.profiles:
                            print(profile)
                            print("-" * 50)

                case "8":
                    try:
                        file_name = input(
                            "Введите имя файла для сохранения (например, data.json): ")
                        manager.to_json(file_name)
                    except InvalidTypeFileException as err:
                        print(f"Error: {err}")
                case "9":
                    try:
                        file_name = input(
                            "Введите имя файла для загрузки (например, data.json): ")
                        manager.from_json(file_name)
                    except InvalidTypeFileException as err:
                        print(f"Error: {err}")

                case "10":
                    try:
                        file_name = input(
                            "Введите имя файла для сохранения (например, data.xml): ")
                        manager.to_xml(file_name)
                    except InvalidTypeFileException as err:
                        print(f"Error: {err}")

                case "11":
                    try:
                        file_name = input(
                            "Введите имя файла для загрузки (например, data.xml): ")
                        manager.from_xml(file_name)
                    except InvalidTypeFileException as err:
                        print(f"Error: {err}")

                case _:
                    print("Некорректный выбор. Попробуйте снова.")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
