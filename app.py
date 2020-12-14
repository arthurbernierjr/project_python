from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INIT DB

db = SQLAlchemy(app)

# INIT Marshmallow

ma = Marshmallow(app)

@app.route('/', methods=['GET'])

def get():
    return jsonify({'msg': 'hello world'})

#***********MODELS********
tags_blogs = db.Table('tags_blogs',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id')))

readers_blogs = db.Table('readers_blogs',
    db.Column('reader_id', db.Integer, db.ForeignKey('reader.id')),
    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id')))
# Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
# Categories
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Readers
class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Blogs
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    sub_title = db.Column(db.String(255))
    body = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", backref="blogs")
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship("Category", backref="blogs")
    readers = db.relationship("Reader", secondary="readers_blogs", backref="blogs")

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tagged_blogs = db.relationship("Blog", secondary="tags_blogs", backref="tags")

# BlogHistory
class BlogHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    sub_title = db.Column(db.String(255))
    body = db.Column(db.String)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    blog = db.relationship("Blog", backref="history")

# Init Schemas
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    blogs = ma.auto_field()

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category

class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag

class ReaderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reader

class BlogHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BlogHistory

class BlogSchema(ma.SQLAlchemyAutoSchema):
    history = ma.Nested(BlogHistorySchema, many=True)
    class Meta:
        model = Blog
        include_fk = True
    readers = ma.auto_field()
    tags = ma.auto_field()
    # id = ma.auto_field()
    # title = ma.auto_field()
    # sub_title = ma.auto_field()
    # body = ma.auto_field()
    # categories = ma.auto_field()
    # tags = ma.auto_field()
    # history = ma.auto_field()
    # readers = ma.auto_field()

blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
reader_schema = ReaderSchema()
readers_schema = ReaderSchema(many=True)
blog_history_schema = BlogHistorySchema()
blog_histories_schema = BlogHistorySchema(many=True)

# Primary Routes

# Create
@app.route('/users', methods=['POST'])
def add_user():
    name = request.json['name']
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@app.route('/blogs', methods=['POST'])
def add_product():
    title = request.json['title']
    sub_title = request.json['sub_title']
    body = request.json['body']
    user_id = request.json['user']
    user = User.query.get(user_id)
    category_id = request.json['category']
    category = Category.query.get(category_id)

    new_blog = Blog(title=title, sub_title=sub_title, body=body, user=user, category=category)

    db.session.add(new_blog)
    db.session.commit()
    return blog_schema.jsonify(new_blog)

# Read
@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route('/blogs', methods=['GET'])
def getBlogs():
    all_blogs = Blog.query.all()
    result = blogs_schema.dump(all_blogs)
    return jsonify(result)

@app.route('/blogs/<id>', methods=['GET'])
def get_blog(id):
    blog = Blog.query.get(id)
    return blog_schema.jsonify(blog)
# Update
@app.route('/blogs/<id>', methods=['PUT'])
def update_blog(id):
    blog = Blog.query.get(id)
    data = request.get_json()
    blog.title = data['title'] if 'title' in data else blog.title
    blog.sub_title = data['sub_title'] if 'sub_title' in data else blog.sub_title
    blog.body = data['body'] if 'body' in data else blog.body

    db.session.commit()
    return blog_schema.jsonify(blog)

# Destroy
@app.route('/blogs/<id>', methods=['DELETE'])
def delete_blog(id):
    blog = Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()

    return blog_schema.jsonify(blog)


# Categories
@app.route('/categories', methods=['POST'])
def add_category():
    name = request.json['name']
    new_category = Category(name=name)
    db.session.add(new_category)
    db.session.commit()
    return category_schema.jsonify(new_category)


@app.route('/categories', methods=['GET'])
def get_categories():
  all_categories = Product.query.all()
  result = categories_schema.dump(all_categories)
  return jsonify(result)

@app.route('/categories/<id>', methods=['GET'])
def get_category(id):
  category = Category.query.get(id)
  return category_schema.jsonify(category)

@app.route('/categories/<id>', methods=['DELETE'])
def delete_category(id):
  category = Category.query.get(id)
  db.session.delete(category)
  db.session.commit()

  return category_schema.jsonify(category)

# Tags
@app.route('/blog/<id>/addTag', methods=['POST'])
def add_new_tag(id):
    blog = Blog.query.get(id)
    name = request.json['name']
    new_tag = Tag(name=name)
    db.session.add(new_tag)
    blog.tags.append(new_tag)
    db.session.commit()
    return blog_schema.jsonify(blog)

@app.route('/blog/<id>/addTag/<tag_id>', methods=['PUT'])
def add_tag(id, tag_id):
    blog = Blog.query.get(id)
    tag = Tag.query.get(tag_id)
    blog.tags.append(tag)
    db.session.commit()
    return blog_schema.jsonify(blog)




# History
@app.route('/blog/<id>/save', methods=['POST'])
def save_blog(id):
    blog = Blog.query.get(id)
    new_history = BlogHistory(title=blog.title, sub_title=blog.sub_title, body=blog.body, blog=blog)
    db.session.add(new_history)
    db.session.commit()
    return blog_schema.jsonify(blog)


# Readers
@app.route('/reader/<id>/blog/<blog_id>', methods=['POST'])
def add_reader(id, blog_id):
    blog = Blog.query.get(blog_id)
    reader = Reader.query.get(id)
    blog.readers.append(reader)
    db.session.commit()
    return blog_schema.jsonify(blog)
# Run Server

if __name__ == '__main__':
    app.run(debug=True)
