from app import db

db.drop_all()
db.create_all()

reader = Reader(name="Mike")
author = User(name="Arthur")

### In a client such as postman

### Available Routes
