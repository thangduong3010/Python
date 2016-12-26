import uuid
import datetime
from database import Database
from models.post import Post

class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = raw_input("Enter post title: ")
        content = raw_input("Enter post content: ")
        date = raw_input("Enter post date (DDMMYYYY), or leave blank for today: ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")

        post = Post(blog_id=self.id,
                    title= title,
                    content= content,
                    author= self.author,
                    date= date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert('blogs', self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'id': self.id,
            'description': self.description
        }

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'id': id})
        return cls(author= blog_data['author'],
                   title= blog_data['title'],
                   description= blog_data['description'],
                   id= blog_data['id'])