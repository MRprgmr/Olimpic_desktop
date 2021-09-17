from peewee import *

db = SqliteDatabase('database.db')


class User(Model):
    telegram_id = IntegerField(null=False, unique=True)
    first_name = TextField(null=False)
    last_name = TextField(null=False)
    phone_number = TextField(null=False)
    class_name = TextField(null=False)

    class Meta:
        database = db


db.create_tables([User])
