from classes import User, Instagram, Telegram, Tiktok, Vkontakte, Snapchat, Facebook, Twitter, Whatsapp
import json
from xml.etree import ElementTree as ET
class DataStorage:
    arr: list[object]
    id:int
    def __init__(self) -> None:
        self.arr = []
        self.id = 1
    def create(self,name_class: str,name: str,surname: str):
        dict_classes= {
        "instagram": Instagram,
        "telegram": Telegram,
        "tiktok": Tiktok,
        "vkontakte": Vkontakte,
        "snapchat": Snapchat,
        "facebook": Facebook,
        "twitter": Twitter,
        "whatsapp": Whatsapp
    }
        if name_class.lower() not in dict_classes:
            #exception
            pass
        else:
            obj = dict_classes[name_class.lower()](self.id,name,surname)
            self.arr.append(obj)
            self.id += 1
            return obj
    def read_all(self):
        return self.arr
    def read_by_id(self, id:int):
        for obj in self.arr:
            if obj.id==id:
                return obj
        return None
    def update(self,id:int, new_name:str = None,new_surname:str = None):
        obj = self.read_by_id(id)
        if obj:
            if new_name:
                obj.name = new_name
            if new_surname:
                obj.surname = new_surname
            print(f"User with id {id} has been update")
            return obj
        return f"User not found."
                
    def delete(self,id)->None:
        obj = self.read_by_id(id)
        if obj:
            self.arr.remove(obj)
            return f"Object with id {id} has been deleted."
        return f"Object not found."
    def to_json(self,filename)->None:
        if ".json" not in filename:
            #exception
            pass
        else:
            with open(filename, "w") as file:
                 json.dump([o.to_format() for o in self.arr], file, indent=4)
    def from_json(self,filename)->None:
        if ".json" not in filename:
            #exception
            pass
        else:
            with open(filename, "r") as file:
                js_data = json.load(file)
                for obj in js_data:
                    self.create(obj["social_network"],obj["name"],obj["surname"])
    def to_xml(self,filename)->None:
        root = ET.Element("users")
        for obj in self.arr:
            user_elem = ET.SubElement(root, "user")
            for key, value in obj.to_format().items():
                ET.SubElement(user_elem, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)
    def from_xml(self,filename)->None:
        tree = ET.parse(filename)
        root = tree.getroot()
        for user_elem in root.findall("user"):
            user_data = {}
            for child in user_elem:
                user_data[child.tag] = child.text
            self.create(user_data["social_network"], user_data["name"], user_data["surname"])
ds = DataStorage()
# Load from XML
ds.from_xml("users.xml")
ds.to_json("db.json")