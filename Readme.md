# Instructions to get started with app

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python seed.py
$ python app.py
```
# Some Core Functionality
<hr>
## added a blog post
![](https://dl.dropboxusercontent.com/s/5fvlzhl74u5ibgs/Screen%20Shot%202020-12-14%20at%2012.56.04%20AM.png?dl=1)

## updated a blog post
![](https://dl.dropboxusercontent.com/s/e2rddb62yfdxtqr/Screen%20Shot%202020-12-14%20at%2012.57.35%20AM.png?dl=1)

## added a reader to a blog post
![](https://dl.dropboxusercontent.com/s/e6zqw8isf0tuxws/Screen%20Shot%202020-12-14%20at%201.03.03%20AM.png?dl=1)

## added a tag to a blog post

![](https://dl.dropboxusercontent.com/s/uswet7uso8eydwc/Screen%20Shot%202020-12-14%20at%201.05.33%20AM.png?dl=1)

## recorded the history of an article so you can comeback to it later

![](https://dl.dropboxusercontent.com/s/8afgnzrujt4gt6o/Screen%20Shot%202020-12-14%20at%201.10.32%20AM.png?dl=0)

## Class Visualization along with above

![](https://dl.dropboxusercontent.com/s/9vkakja36iaig1g/Screen%20Shot%202020-12-14%20at%201.47.47%20AM.png?dl=0)

![](https://dl.dropboxusercontent.com/s/qmh4jo04f4mqz3f/Screen%20Shot%202020-12-14%20at%201.49.43%20AM.png?dl=0)

![](https://dl.dropboxusercontent.com/s/9lf7xs5tnex880d/Screen%20Shot%202020-12-14%20at%201.50.37%20AM.png?dl=0)

## Blog Post Visual
![](https://dl.dropboxusercontent.com/s/aa6w3xl21riva1a/Screen%20Shot%202020-12-14%20at%201.59.02%20AM.png?dl=0)

## Main Page Visual

![](https://dl.dropboxusercontent.com/s/9rlqlr9vngo06li/Screen%20Shot%202020-12-14%20at%202.00.41%20AM.png?dl=0)
# Synopsis
<hr>
- I elected to build a Blog Back End in Flask
- The main functionality that exists is the ability to Create, Read ,Update and Destroy content
# In a client such as postman you can visit the following Routes

### Available Routes

# CRUD on Blogs
## /blogs  and /blogs/<id> method Get, POST, PUT, Delete Create a Blog
### params
        - title
        - subtitle
        - user
        - category


# Create and Read Users
## /users and /user/<id> methods GET and POST
### params
        - name


# Categories CRUD
## /categories /categories/<id> methods GET, POST, PUT, DELETE
### params
        - name

# Other

## /blog/<id>/addTag  Creates a New Tag and adds it to a blog
### params
      - name

## /<id>/blog/addTag/<tag_id>Takes an existing tag and adds it to a blog

## /reader/<id>/blog/<blog_id>  Reader reads a blog

### /blog/<id>/save Adds a blog History entry to save progress
