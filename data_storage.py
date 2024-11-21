import json
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from classes import *
from my_exceptions import InvalidTypeFileException


class ProfileManager:
    def __init__(self):
        self.profiles = []

    def create_profile(self, name: str, surname: str) -> None:
        user = User(name, surname)
        profile = Profile(user)
        self.profiles.append(profile)
        print(f"Профиль для пользователя {name} {
              surname} создан с ID {user.id}.")

    def delete_profile(self, user_id: int) -> None:
        profile_to_delete = None
        for profile in self.profiles:
            if profile.user.id == user_id:
                profile_to_delete = profile
                break

        if profile_to_delete:
            self.profiles.remove(profile_to_delete)
            print(f"Профиль с ID {user_id} и все связанные данные удалены.")
        else:
            raise InvalidIdException(user_id)

    def get_profile_by_id(self, user_id: int) -> Profile:
        for profile in self.profiles:
            if profile.user.id == user_id:
                return profile
        raise InvalidIdException(user_id)

    def to_json(self, file_name: str):
        if ".json" not in file_name:
            raise InvalidTypeFileException(file_name)
        data = [profile.to_dict() for profile in self.profiles]
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в {file_name}.")

    def from_json(self, file_name: str):
        if not file_name.endswith(".json"):
            raise InvalidTypeFileException(file_name)
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.profiles = [Profile.from_dict(
                profile_data) for profile_data in data]
        print(f"Данные загружены из {file_name}.")

    def to_xml(self, file_name: str):
        if ".xml" not in file_name:
            raise InvalidTypeFileException(file_name)
        root = Element("Profiles")
        for profile in self.profiles:
            profile_elem = SubElement(root, "Profile")
            user_elem = SubElement(profile_elem, "User")
            SubElement(user_elem, "ID").text = str(profile.user.id)
            SubElement(user_elem, "Name").text = profile.user.name
            SubElement(user_elem, "Surname").text = profile.user.surname
            for tag, data_list in [("Photos", profile.photos), ("Videos", profile.videos), ("Posts", profile.posts)]:
                tag_elem = SubElement(profile_elem, tag)
                for item in data_list:
                    # Убираем "s" из тега
                    item_elem = SubElement(tag_elem, tag[:-1])
                    for key, value in item.to_dict().items():
                        SubElement(item_elem, key).text = str(value)

        tree = ElementTree(root)
        tree.write(file_name, encoding="utf-8", xml_declaration=True)
        print(f"Данные сохранены в {file_name}.")

    def from_xml(self, file_name: str):
        if ".xml" not in file_name:
            raise InvalidTypeFileException(file_name)
        tree = ElementTree()
        tree.parse(file_name)
        root = tree.getroot()
        self.profiles = []
        for profile_elem in root.findall("Profile"):
            user_elem = profile_elem.find("User")
            user_id = int(user_elem.find("ID").text)
            name = user_elem.find("Name").text
            surname = user_elem.find("Surname").text
            user = User(name, surname)
            user.id = user_id
            profile = Profile(user)
            for tag, cls in [("Photos", Photo), ("Videos", Video), ("Posts", Post)]:
                tag_elem = profile_elem.find(tag)
                if tag_elem is not None:
                    for item_elem in tag_elem:
                        item_data = {
                            child.tag: child.text for child in item_elem}
                        if "photo_id" in item_data:
                            item_data["photo_id"] = int(item_data["photo_id"])
                        if "video_id" in item_data:
                            item_data["video_id"] = int(item_data["video_id"])
                        if "duration" in item_data:
                            item_data["duration"] = int(item_data["duration"])
                        if "post_id" in item_data:
                            item_data["post_id"] = int(item_data["post_id"])
                        getattr(profile, tag.lower()).append(cls(**item_data))
            self.profiles.append(profile)
        print(f"Данные загружены из {file_name}.")
