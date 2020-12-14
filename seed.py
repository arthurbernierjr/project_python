from app import db, Reader, User, Category
db.drop_all()
db.create_all()

reader = Reader(name="Mike")
author = User(name="Arthur")
category = Category(name="News")
db.session.add(reader)
db.session.add(author)
db.session.add(category)
db.session.commit()
### In a client such as postman

### Available Routes

# CRUD on Blogs
## /blogs  and /blogs/<id> method Get, POST, PUT, Delete Create a Blog
### params
        # title
        # subtitle
        # user
        # category


# Create and Read Users
## /users and /user/<id> methods GET and POST
### params
        # name


# Categories CRUD
## /categories /categories/<id> methods GET, POST, PUT, DELETE
### params
        # name

# Other

## /blog/<id>/addTag  Creates a New Tag and adds it to a blog
### params
## name

## /<id>/blog/addtag/<tag_id>Takes an existing tag and adds it to a blog

## /reader/<id>/blog/<id>  Reader reads a blog

### /blog/<id>/save Adds a blog History entry to save progress
