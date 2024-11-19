from data_storage import DataStorage
from my_exceptions import InvalidTypeFileException,InvalidTypeSocialNetwork,InvalidIdUserException

def interface_info() -> None:
    print("\n1. Создать информацию о пользователе")
    print("2. Обновить информацию о пользователе") 
    print("3. Удалить пользователя")
    print("4. Вывести информацию о всех пользователях")
    print("5. Вывести информацию о пользователе по его id")
    print("6. Сохранить информацию о пользователях в json файл")
    print("7. Выгрузить информацию о пользователях из json файла")
    print("8. Сохранить информацию о пользователях в xml файл")
    print("9. Выгрузить информацию о пользователях из xml файла")
    print("0. Выход из программы")


def main():
    ds = DataStorage()
    while True:
        interface_info()
        interface_num = input("\nВведите соответствующий пункт меню:")
        match interface_num:
            case "1":
                try:
                    social_network = input("Введите социальную сеть, которую использует наш пользователь:")
                    name= input("Введите имя пользователя: ")
                    surname = input("Введите фамилию пользователя: ")
                    user = ds.create(social_network,name,surname)
                except InvalidTypeSocialNetwork as err:
                    print(f"Error:{err}")
            case "2":
                try:
                    id_user = int(input("Укажите id пользователя, которому вы хотите что-либо обновить: "))
                    choose_update = input("Укажите, что вы хотите обновить: 1 - Имя, 2 - Фамилию, 3 - Имя и Фамилию: ")
                    if choose_update == 1:
                        upd_name = input("Укажите новое имя: ")
                        ds.update(id_user,new_name=upd_name)
                    elif choose_update == 2:
                        upd_surname = input("Укажите новую фамилию: ")
                        ds.update(id_user,new_surname=upd_surname)
                    elif choose_update == 3:
                        upd_name = input("Укажите новое имя: ")
                        upd_surname = input("Укажите новую фамилию: ")
                        ds.update(id_user, new_name=upd_name, new_surname=upd_surname)
                except ValueError:
                    print("ID должно быть целым числом.")
                except InvalidIdUserException as err:
                    print(f"Error: {err}")                    
            case "3":
                try:
                    id_user = int(input("Укажите id пользователя, информацию о котором вы хотите удалить: "))
                    ds.delete(id_user)
                except ValueError:
                    print("ID должно быть целым числом.")
                except InvalidIdUserException as err:
                    print(f"Error: {err}")
            case "4":
                arr=ds.read_all()
                for obj in arr:
                    print(obj.features())
            case "5":
                try:
                    id_user = int(input("Укажите id пользователя, информацию о котором вы хотите узнать: "))
                    us1 = ds.read_by_id(id_user)
                    print(us1.features())
                except ValueError:
                    print("ID должно быть целым числом.")
                except InvalidIdUserException as err:
                    print(f"Error: {err}")
            case "6":
                try:
                    filename=input("Укажите название файла, в который вы хотите сохранить информацию о пользователях (например name.json):")
                    ds.to_json(filename)
                except InvalidTypeFileException as err:
                    print(f"Error: {err}") 
            case "7":
                try:
                   filename=input("Укажите название файла, из которого вы хотите выгрузить информацию о пользователях (например name.json):")
                   ds.from_json(filename)
                except (FileNotFoundError,InvalidTypeFileException ) as err:
                    print(f"Failed to loading objects: {err}") 
            case "8":
                try:
                    filename=input("Укажите название файла, в который вы хотите сохранить информацию о пользователях (например name.xml):")
                    ds.to_xml(filename)
                except InvalidTypeFileException as err:
                    print(f"Error: {err}") 
            case "9":
                try:
                   filename=input("Укажите название файла, из которого вы хотите выгрузить информацию о пользователях (например name.xml):")
                   ds.from_xml(filename)
                except (FileNotFoundError,InvalidTypeFileException ) as err:
                    print(f"Failed to loading objects: {err}")
            case "0":
                print("Программа завершена.")
                break
            case _:
                print("Неверный пункт, попробуйте снова.")

if __name__=="__main__":
    main()