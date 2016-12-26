from models.blog import Blog
from database import Database

class Menu(object):
    def __init__(self):
        # Ask user for author name
        # Check if they've got an account
        # if not, create one
        self.user = raw_input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account(): # this is a private method
            print("Welcome back, {}!".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one(collection= 'blogs',
                                 query= {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = raw_input("Enter blog title: ")
        description = raw_input("Enter blog description: ")
        blog = Blog(author= self.user,
                    title= title,
                    description= description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        # User read or write blogs?
        # if read:
        #   list blogs in database
        #   allow user to pick one
        #   display posts
        # if write:
        #   check if user has blog
        #   if they do, prompt to write a blog
        #   if not, prompt to create a new blog
        user_action = raw_input("Do you want to (r)ead or (w)rite blogs? ").lower()
        if user_action == 'r':
            self._list_blog()
            self._view_blog()
        elif user_action == 'w':
            self.user_blog.new_post()
        else:
            print("We're sad to see you go :(")

    def _list_blog(self):
        blogs = Database.find(collection= 'blogs',
                              query= {})
        for blog in blogs:
            print("ID: {} - Title: {} - Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = raw_input("Enter the ID of blog to read: ")
        blog = Blog.get_from_mongo(blog_to_see)
        posts = blog.get_posts()
        print("Blog of {}".format(blog.author))

        for post in posts:
            print("======================================================================================")
            print("Date: {}\nTitle: {}\n\n{}".format(post['created_date'], post['title'], post['content']))
