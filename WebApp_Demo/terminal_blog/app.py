from menu import Menu
from database import Database

Database.initialize()
# # post = Post(blog_id="123",
# #             title="Untitled1",
# #             content="Hallelujah",
# #             author="Thang")
# # post.save_to_mongo()
# post = Post.from_mongo("123").title
# print(post)

# blog = Blog(author= "Thang",
#             title= "New title",
#             description= "Sample blog")
# blog.new_post()
# blog.save_to_mongo()
#
# from_db = Blog.get_from_mongo(blog.id)
#
# print("Blog of {}".format(from_db.author))
# print(blog.get_posts())
menu = Menu()
menu.run_menu()