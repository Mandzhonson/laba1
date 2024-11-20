from classes import *
from my_exceptions import InvalidIdException, InvalidTypeFileException
import json
from xml.etree import ElementTree as ET


class ProfileManager:
    def __init__(self) -> None:
        self.arr = []
        self.id = 1
        self.id_msg = 1
        self.id_post = 1
        self.id_photo = 1
        self.id_video = 1
        self.id_comment = 1
        self.id_group = 1

    def create(self, name, surname) -> Profile:
        profile = Profile(self.id, name, surname)
        self.arr.append(profile)
        self.id += 1
        print("Профиль успешно создан.")
        return profile

    def read_all(self):
        return self.arr

    def read_by_id_user(self, profile_id: int) -> Profile:
        for profile in self.arr:
            if profile.user.id == profile_id:
                return profile
        raise InvalidIdException(profile_id)

    def send_message(self, sender_id: int, receiver_id: int, text: str) -> None:
        try:
            sender = self.read_by_id_user(sender_id)
            receiver = self.read_by_id_user(receiver_id)
            message = Message(sender_id=sender.user.id,
                              receiver_id=receiver.user.id, text=text)
            sender.messages.append(message)
            receiver.messages.append(message)
            print(f"Сообщение отправлено от ID {
                  sender_id} к ID {receiver_id}: {text}")
        except InvalidIdException as err:
            print(f"Ошибка: {err}")

    def send_comment(self, user_id: int, post_id: int, content: str) -> None:
        try:
            post = self.read_by_id_user(post_id=post_id)
            comment = Comment(post_id, user_id, content)
            post.comments.append(comment)
            print(f"К посту с ID {id} был добавлен комментарий {
                  comment.content}")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def add_friend(self, profile_id1: int, profile_id2: int) -> None:
        try:
            profile1 = self.read_by_id_user(profile_id1)
            profile2 = self.read_by_id_user(profile_id2)
            # добавляем в друзья друг друга
            friend1 = Friend(user_id=profile_id1, friend_id=profile_id2)
            friend2 = Friend(user_id=profile_id2, friend_id=profile_id1)
            profile1.friends.append(friend2)
            profile2.friends.append(friend1)
            print(f"Пользователи с ID {profile_id1} и {
                  profile_id2} стали друзьями.")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def update_message(self, message_id: int, sender_id: int, text: str) -> None:
        try:
            sender = self.read_by_id_user(sender_id)
            msg = sender.read_by_id(message_id=message_id)
            msg.text = text
            receiver_id = msg.receiver_id
            receiver = self.read_by_id_user(receiver_id)
            msg = receiver.read_by_id(message_id=message_id)
            msg.text = text
        except InvalidIdException as err:
            print(f"Error: {err}")

    def update_comment(self, profile_id: int, comment_id: int, text: str) -> None:
        try:
            profile = self.read_by_id_user(profile_id)
            profile.update_comment_text(text, comment_id)
            print(f"Комментарий с ID {comment_id} успешно изменен: {text}")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def delete_message(self, sender_id: int, message_id: int) -> None:
        try:
            sender = self.read_by_id_user(sender_id)
            msg = sender.read_by_id(message_id=message_id)
            receiver_id = msg.receiver_id
            receiver = self.read_by_id_user(receiver_id)
            sender.messages.remove(msg)
            msg = receiver.read_by_id(message_id=message_id)
            receiver.messages.remove(msg)
            print(f"Сообщение с ID {message_id} успешно удалено!")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def delete_post(self, profile_id: int, post_id: int) -> None:
        try:
            profile = self.read_by_id_user(profile_id)
            post_del = profile.read_by_id(post_id=post_id)
            for comment_id in post_del.comments:
                self.delete_comment(comment_id, post_id)

            profile.posts.remove(post_del)
            print(f"Пост с ID {
                  post_id} и все его комментарии успешно удалены!")
        except InvalidIdException as err:
            print(f"Ошибка: {err}")

    def delete_friend(self, profile_id: int, friend_id: int) -> None:
        try:
            profile = self.read_by_id_user(profile_id=profile_id)
            friend = profile.read_by_id(friend_id=friend_id)
            profile.friends.remove(friend)
            other_profile = self.read_by_id_user(profile_id=friend_id)
            mutual_friend = other_profile.read_by_id(friend_id=profile_id)
            other_profile.friends.remove(mutual_friend)
            print(f"Дружба между пользователями с ID {
                  profile_id} и {friend_id} разорвана.")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def to_json(self, filename: str) -> None:
        if ".json" not in filename:
            raise InvalidTypeFileException(filename)
        data = []
        for profile in self.arr:
            profile_data = profile.to_format()
            data.append(profile_data)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Данные успешно сохранены в файл {filename}.")

    def from_json(self, filename: str) -> None:
        if ".json" not in filename:
            raise InvalidTypeFileException(filename)
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            for user_data in data:
                user = User(
                    id=user_data["user"]["id"],
                    name=user_data["user"]["name"],
                    surname=user_data["user"]["surname"]
                )
                profile = Profile(user)
                for photo_data in user_data.get("photos", []):
                    photo = Photo(profile.user.id, photo_data["file_name"])
                    profile.photos.append(photo)

                for video_data in user_data.get("videos", []):
                    video = Video(profile.user.id, video_data["file_name"])
                    profile.videos.append(video)

                for post_data in user_data.get("posts", []):
                    post = Post(profile.user.id, post_data["text"])
                    profile.posts.append(post)

                for message_data in user_data.get("messages", []):
                    message = Message(
                        sender_id=message_data["sender_id"],
                        receiver_id=message_data["receiver_id"],
                        text=message_data["text"]
                    )
                    profile.messages.append(message)

                for comment_data in user_data.get("comments", []):
                    comment = Comment(
                        post_id=comment_data["post_id"],
                        user_id=comment_data["user_id"],
                        content=comment_data["content"]
                    )
                    profile.comments.append(comment)

                for friend_data in user_data.get("friends", []):
                    friend = Friend(
                        user_id=friend_data["user_id"], friend_id=friend_data["friend_id"])
                    profile.friends.append(friend)

                for group_data in user_data.get("groups", []):
                    group = Group(group_data["name"], group_data["members"])
                    profile.groups.append(group)

                self.arr.append(profile)
        print(f"Данные загружены из файла {filename}.")

    def from_xml(self, filename: str) -> None:
        if not filename.endswith(".xml"):
            raise InvalidTypeFileException(filename)
        tree = ET.parse(filename)
        root = tree.getroot()

        for user_element in root.findall("user"):
            user = User(
                id=int(user_element.find("id").text),
                name=user_element.find("name").text,
                surname=user_element.find("surname").text
            )
            profile = Profile(user)
            for photo_element in user_element.findall("photos/photo"):
                photo = Photo(profile.user.id, photo_element.text)
                profile.photos.append(photo)

            for video_element in user_element.findall("videos/video"):
                video = Video(profile.user.id, video_element.text)
                profile.videos.append(video)

            for post_element in user_element.findall("posts/post"):
                post = Post(profile.user.id, post_element.text)
                profile.posts.append(post)

            for message_element in user_element.findall("messages/message"):
                message = Message(
                    sender_id=int(message_element.find("sender_id").text),
                    receiver_id=int(message_element.find("receiver_id").text),
                    text=message_element.text
                )
                profile.messages.append(message)

            for comment_element in user_element.findall("comments/comment"):
                comment = Comment(
                    post_id=int(comment_element.find("post_id").text),
                    user_id=int(comment_element.find("user_id").text),
                    content=comment_element.text
                )
                profile.comments.append(comment)

            for friend_element in user_element.findall("friends/friend"):
                friend = Friend(
                    user_id=int(friend_element.find("user_id").text),
                    friend_id=int(friend_element.find("friend_id").text)
                )
                profile.friends.append(friend)

            for group_element in user_element.findall("groups/group"):
                group = Group(
                    group_element.find("name").text,
                    [member.text for member in group_element.findall(
                        "members/member")]
                )
                profile.groups.append(group)

            self.arr.append(profile)
        print(f"Данные загружены из файла {filename}.")

    def to_xml(self, filename: str) -> None:
        if not filename.endswith(".xml"):
            raise InvalidTypeFileException(filename)
        root = ET.Element("profiles")

        for profile in self.arr:
            user_element = ET.SubElement(root, "user")
            ET.SubElement(user_element, "id").text = str(profile.user.id)
            ET.SubElement(user_element, "name").text = profile.user.name
            ET.SubElement(user_element, "surname").text = profile.user.surname

            photos_element = ET.SubElement(user_element, "photos")
            for photo in profile.photos:
                ET.SubElement(photos_element, "photo").text = photo.file_name

            videos_element = ET.SubElement(user_element, "videos")
            for video in profile.videos:
                ET.SubElement(videos_element, "video").text = video.file_name

            posts_element = ET.SubElement(user_element, "posts")
            for post in profile.posts:
                ET.SubElement(posts_element, "post").text = post.text

            messages_element = ET.SubElement(user_element, "messages")
            for message in profile.messages:
                message_element = ET.SubElement(messages_element, "message")
                ET.SubElement(message_element, "sender_id").text = str(
                    message.sender_id)
                ET.SubElement(message_element, "receiver_id").text = str(
                    message.receiver_id)
                message_element.text = message.text

            comments_element = ET.SubElement(user_element, "comments")
            for comment in profile.comments:
                comment_element = ET.SubElement(comments_element, "comment")
                ET.SubElement(comment_element, "post_id").text = str(
                    comment.post_id)
                ET.SubElement(comment_element, "user_id").text = str(
                    comment.user_id)
                comment_element.text = comment.content

            friends_element = ET.SubElement(user_element, "friends")
            for friend in profile.friends:
                friend_element = ET.SubElement(friends_element, "friend")
                ET.SubElement(friend_element, "user_id").text = str(
                    friend.user_id)
                ET.SubElement(friend_element, "friend_id").text = str(
                    friend.friend_id)

            groups_element = ET.SubElement(user_element, "groups")
            for group in profile.groups:
                group_element = ET.SubElement(groups_element, "group")
                ET.SubElement(group_element, "name").text = group.name
                members_element = ET.SubElement(group_element, "members")
                for member in group.members:
                    ET.SubElement(members_element, "member").text = member

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        print(f"Данные успешно сохранены в файл {filename}.")
