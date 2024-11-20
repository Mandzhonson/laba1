from my_exceptions import InvalidIdException


class User:
    id: int
    name: str
    surname: str

    def __init__(self, id: int, name: str, surname: str) -> None:
        self.id = id
        self.name = name
        self.surname = surname

    def to_format(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname
        }


class Photo:
    photos_id = 1
    photo_id: int
    user_id: int
    file_name: str

    def __init__(self, user_id: int, file_name: str) -> None:
        self.photo_id = Photo.photos_id
        Photo.photos_id += 1
        self.user_id = user_id
        self.file_name = file_name

    def to_format(self):
        return {
            "photo_id": self.photo_id,
            "user_id": self.user_id,
            "file_name": self.file_name
        }


class Video:
    videos_id = 1
    video_id: int
    user_id: int
    file_name: str

    def __init__(self, user_id: int, file_name: str) -> None:
        self.video_id = Video.videos_id
        Video.videos_id += 1
        self.user_id = user_id
        self.file_name = file_name

    def to_format(self):
        return {
            "video_id": self.video_id,
            "user_id": self.user_id,
            "file_name": self.file_name,
        }


class Message:
    msg_id = 1
    message_id: int
    sender_id: int
    receiver_id: int
    text: str

    def __init__(self, sender_id: int, receiver_id: int, text: str) -> None:
        self.message_id = Message.msg_id
        Message.msg_id += 1
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.text = text

    def to_format(self):
        return {
            "message_id": self.message_id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "text": self.text
        }


class Post:
    posts_id = 1
    post_id: int
    user_id: int
    content: str
    comments: list

    def __init__(self, user_id: int, content: str) -> None:
        self.post_id = Post.posts_id
        Post.posts_id += 1
        self.user_id = user_id
        self.content = content
        self.comments = []

    def to_format(self):
        return {
            "post_id": self.post_id,
            "user_id": self.user_id,
            "content": self.content
        }


class Comment:
    comments_id = 1
    post_id: int
    user_id: int
    content: str

    def __init__(self, post_id: int, user_id: int, content: str) -> None:
        self.comment_id = Comment.comments_id
        Comment.comments_id += 1
        self.post_id = post_id
        self.user_id = user_id
        self.content = content

    def to_format(self):
        return {
            "comment_id": self.comment_id,
            "post_id": self.post_id,
            "user_id": self.user_id,
            "content": self.content,
        }


class Friend:
    user_id: int
    friend_id: int

    def __init__(self, user_id: int, friend_id: int) -> None:
        self.user_id = user_id
        self.friend_id = friend_id

    def to_format(self):
        return {
            "user_id": self.user_id,
            "friend_id": self.friend_id,
        }


class Group:
    groups_id = 1
    group_id: int
    group_name: str
    members: int

    def __init__(self, group_name: str, members: list) -> None:
        self.group_id = Group.groups_id
        Group.groups_id += 1
        self.group_name = group_name
        self.members = members

    def to_format(self):
        return {
            "group_id": self.group_id,
            "group_name": self.group_name,
            "members": self.members,
        }


class Profile:
    def __init__(self, id: int, name: str, surname: str) -> None:
        self.user = User(id, name, surname)
        self.photos = []
        self.videos = []
        self.posts = []
        self.messages = []
        self.comments = []
        self.friends = []
        self.groups = []

    def read_by_id(self, photo_id=None, video_id=None, post_id=None, message_id=None, comment_id=None, friend_id=None, group_id=None):
        if photo_id:
            for photo in self.photos:
                if photo.id == photo_id:
                    return photo
            raise InvalidIdException(photo_id)
        elif video_id:
            for video in self.videos:
                if video.id == video_id:
                    return video
            raise InvalidIdException(video_id)
        elif post_id:
            for post in self.posts:
                if post.id == post_id:
                    return post
            raise InvalidIdException(post_id)
        elif message_id:
            for message in self.messages:
                if message.id == message_id:
                    return message
            raise InvalidIdException(message_id)
        elif comment_id:
            for comment in self.comments:
                if comment.id == comment_id:
                    return comment
            raise InvalidIdException(comment_id)
        elif friend_id:
            for friend in self.friends:
                if friend.id == friend_id:
                    return friend
            raise InvalidIdException(friend_id)
        elif group_id:
            for group in self.groups:
                if group.id == photo_id:
                    return group
            raise InvalidIdException(group_id)
        else:
            raise Exception("Вы не указали никакой параметр, метод не может работать")

    def add_photo(self, profile_id: int, file_name: str) -> None:
        photo = Photo(profile_id, file_name)
        self.photos.append(photo)
        print(f"Фото {file_name} успешно добавлено пользователю с ID {
              profile_id}.")

    def add_video(self, profile_id: int, file_name: str) -> None:
        video = Video(profile_id, file_name)
        self.videos.append(video)
        print(f"Видео {video.file_name} успешно добавлено пользователю с ID {
            profile_id}.")

    def add_post(self, profile_id: int, text: str) -> None:
        post = Post(profile_id, text)
        self.posts.append(post)
        print(f"Пост успешно добавлен пользователю с ID {profile_id}.")

    def add_group(self, group_name, members) -> None:
        group = Group(group_name, members)
        self.groups.append(group)
        print(f"Пользователь с ID {self.user.id} оформил подписку на группу {
              group_name} (ID {group.group_id})")

    def update_photo(self, new_name: str, id: int):
        try:
            obj = self.read_by_id(photo_id=id)
            obj.file_name = new_name
            print(f"Название фото с ID {
                  obj.photo_id} изменено: {obj.file_name}")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def update_video(self, new_name: str, id: int):
        try:
            obj = self.read_by_id(video_id=id)
            obj.file_name = new_name
            print(f"Название фото с ID {
                  obj.video_id} изменено: {obj.file_name}")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def update_post(self, new_content: str, id: int):
        try:
            obj = self.read_by_id(post_id=id)
            obj.content = new_content
            print(f"Содержание поста с ID {
                  obj.video_id} изменено: {obj.content}")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def update_comment(self, new_content: str, id: int, post_id: int):
        try:
            obj = self.read_by_id(comment_id=id)
            obj.content = new_content
            post = self.read_by_id(post_id=post_id)
            for comm in post.comments:
                if comm.id == id:
                    comm.text = new_content
                else:
                    raise InvalidIdException(id)
        except InvalidIdException as err:
            print(f"Error: {err}")

    def delete_photo(self, photo_id: int) -> None:
        try:
            photo_del = self.read_by_id(photo_id=photo_id)
            self.photos.remove(photo_del)
            print(f"Фото с ID {photo_id} успешно удалено!")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def delete_video(self, video_id: int) -> None:
        try:
            video_del = self.read_by_id(video_id=video_id)
            self.videos.remove(video_del)
            print(f"Видео с ID {video_id} успешно удалено!")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def delete_comment(self, comment_id: int, post_id: int) -> None:
        try:
            comment_del = self.read_by_id(comment_id=comment_id)
            self.comments.remove(comment_del)
            post = self.read_by_id(post_id=post_id)
            post.comments.remove(comment_del)
            print(f"Комментарий под ID {comment_id} успешно удален!")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def delete_group(self, group_id: int) -> None:
        try:
            group_del = self.read_by_id(group_id=group_id)
            self.groups.remove(group_del)
            print(f"Подписка на группу с ID {group_id} успешно отменена!")
        except InvalidIdException as err:
            print(f"Error: {err}")

    def to_format(self):
        return {
            "user": self.user.to_format(),
            "photos": [photo.to_format() for photo in self.photos],
            "videos": [video.to_format() for video in self.videos],
            "posts": [post.to_format() for post in self.posts],
            "messages": [message.to_format() for message in self.messages],
            "comments": [comment.to_format() for comment in self.comments],
            "friends": [friend.to_format() for friend in self.friends],
            "groups": [group.to_format() for group in self.groups],
        }
