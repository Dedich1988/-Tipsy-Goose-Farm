from peewee import *

db = SqliteDatabase('bakery.db')

class BaseModel(Model):
    class Meta:
        database = db

class Category(BaseModel):
    name = CharField(unique=True)

class Product(BaseModel):
    name = CharField()
    description = TextField()
    price = DecimalField()
    photo = CharField()
    category = ForeignKeyField(Category, backref='products')

if __name__ == '__main__':
    db.connect()
    db.create_tables([Category, Product])
    db.close()