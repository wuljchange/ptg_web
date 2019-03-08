from mongoengine import *
from ..config.config import DbConfig

Config = DbConfig('user')


class User(Document):
    photo = ImageField()
    name = StringField(max_length=50, required=True)
    password = StringField(min_length=6, max_length=15, required=True)
    email = EmailField(required=True)
    introduction = StringField(max_length=1000)


class Session(Document):
    uid = StringField()
    token = StringField()
    created = DateTimeField()
    meta = {
        'indexes': [
            {
                'fields': [created],
                'expireAfterSeconds': 7200
            }
        ]
    }

