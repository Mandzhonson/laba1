from my_exceptions import InvalidIdException


class User:
    _id_counter = 1
    name:str
    surname:str
    id:int
    def __init__(self, name: str, surname: str):
        self.id = User._id_counter
        User._id_counter += 1
        self.name = name
        self.surname = surname

    def to_dict(self):
        return {"id": self.id, "name": self.name, "surname": self.surname}

    def __str__(self):
        return f"ID: {self.id}, Имя: {self.name}, Фамилия: {self.surname}"


class Photo:
    _id_counter = 1
    photo_id: int
    file_name: str
    def __init__(self, file_name: str, photo_id: int = None):
        if photo_id is not None:
            self.photo_id = photo_id
        else:
            self.photo_id = Photo._id_counter
            Photo._id_counter += 1
        self.file_name = file_name

    def to_dict(self):
        return {"photo_id": self.photo_id, "file_name": self.file_name}

    def __str__(self):
        return f"Photo ID: {self.photo_id}, File Name: {self.file_name}"


class Video:
    _id_counter = 1
    video_id: int
    file_name: str
    duration: int
    def __init__(self, file_name: str, duration: int, video_id: int = None):
        if video_id is not None:
            self.video_id = video_id
        else:
            self.video_id = Video._id_counter
            Video._id_counter += 1
        self.file_name = file_name
        self.duration = duration

    def to_dict(self):
        return {"video_id": self.video_id, "file_name": self.file_name, "duration": self.duration}

    def __str__(self):
        return f"Video ID: {self.video_id}, File Name: {self.file_name}, Duration: {self.duration}"


class Post:
    _id_counter = 1
    post_id: int
    content: str
    def __init__(self, content: str, post_id: int = None):
        if post_id is not None:
            self.post_id = post_id
        else:
            self.post_id = Post._id_counter
            Post._id_counter += 1
        self.content = content

    def to_dict(self):
        return {"post_id": self.post_id, "content": self.content}

    def __str__(self):
        return f"Post ID: {self.post_id}, Content: {self.content}"


class Profile:
    def __init__(self, user: User):
        self.user = user
        self.photos = []
        self.videos = []
        self.posts = []

    def read_by_id(self, photo_id=None, video_id=None, post_id=None):
        if photo_id:
            for photo in self.photos:
                if photo.photo_id == photo_id:
                    return photo
            raise InvalidIdException(photo_id)
        elif video_id:
            for video in self.videos:
                if video.video_id == video_id:
                    return video
            raise InvalidIdException(video_id)
        elif post_id:
            for post in self.posts:
                if post.post_id == post_id:
                    return post
            raise InvalidIdException(post_id)
        else:
            raise Exception(
                "Вы не указали ни одного параметра, метод не может работать.")

    def add_photo(self, file_name: str):
        photo = Photo(file_name)
        self.photos.append(photo)
    def update_name_surname(self,new_name:str,new_surname:str)->None:
        self.user.name = new_name
        self.user.surname = new_surname
    def update_photo(self, photo_id: int, new_name: str):
        for photo in self.photos:
            if photo.photo_id == photo_id:
                photo.file_name = new_name
                return
        raise ValueError(f"Фото с ID {photo_id} не найдено.")

    def delete_photo(self, photo_id: int) -> None:
        self.photos = [
            photo for photo in self.photos if photo.photo_id != photo_id]

    def add_video(self, file_name: str, duration: int):
        video = Video(file_name, duration)
        self.videos.append(video)

    def update_video(self, video_id: int, new_name: str) -> None:
        for video in self.videos:
            if video.video_id == video_id:
                video.file_name = new_name
                return
        raise ValueError(f"Видео с ID {video_id} не найдено.")

    def delete_video(self, video_id: int) -> None:
        self.videos = [
            video for video in self.videos if video.video_id != video_id]

    def add_post(self, content: str) -> None:
        post = Post(content)
        self.posts.append(post)

    def update_post(self, post_id: int, new_content: str) -> None:
        for post in self.posts:
            if post.post_id == post_id:
                post.content = new_content
                return
        raise ValueError(f"Пост с ID {post_id} не найден.")

    def delete_post(self, post_id: int) -> None:
        self.posts = [post for post in self.posts if post.post_id != post_id]

    def to_dict(self):
        return {
            "user": self.user.to_dict(),
            "photos": [photo.to_dict() for photo in self.photos],
            "videos": [video.to_dict() for video in self.videos],
            "posts": [post.to_dict() for post in self.posts],
        }
    
    def from_dict(cls, data):
        user_data = data["user"]
        user = User(user_data["name"], user_data["surname"])
        user.id = user_data["id"]
        profile = cls(user)
        profile.photos = [Photo(**photo_data) for photo_data in data["photos"]]
        profile.videos = [Video(**video_data) for video_data in data["videos"]]
        profile.posts = [Post(**post_data) for post_data in data["posts"]]
        return profile

    def __str__(self):
        return (
            f"{self.user}\n"
            f"Фотографии: {', '.join(str(photo) for photo in self.photos)}\n"
            f"Видео: {', '.join(str(video) for video in self.videos)}\n"
            f"Посты: {', '.join(str(post) for post in self.posts)}"
        )
