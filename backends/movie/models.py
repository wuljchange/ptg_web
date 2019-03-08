from mongoengine import *
from arrow.arrow import datetime
from ..config.config import DbConfig
from ..user.models import User


Config = DbConfig('movie')


class Genre(Document):
    name = StringField(max_length=20, required=True)
    meta = {
        'ordering': ['name'],
        'collection': 'movie_genre'
    }


class Role(Document):
    name = StringField(max_length=20, required=True)
    meta = {
        'ordering': ['name'],
        'collection': 'movie_role'
    }


class Country(Document):
    name = StringField(max_length=30, required=True)
    meta = {
        'ordering': ['name'],
        'collection': 'movie_country'
    }


class Person(Document):
    name = StringField(max_length=50, required=True)
    date_of_birth = DateTimeField()
    photo = ImageField(required=True)
    role = ListField(ReferenceField(Role))
    country = ReferenceField(Country)
    introduction = StringField(max_length=1000)
    date_added = DateTimeField(default=datetime.utcnow())
    meta = {
        'ordering': ['-date_added'],
        'collection': 'movie_person'
    }


class Movie(Document):
    title = StringField(max_length=50, required=True)
    year = IntField()
    introduction = StringField(max_length=1000)
    cover = ImageField(required=True)
    rating = FloatField(default=0)
    trailer = URLField()
    link_to_watch = URLField()
    duration = IntField(required=True)
    likes = IntField(default=0)
    collections = IntField(default=0)
    director = ListField(ReferenceField(Person))
    genres = ListField(ReferenceField(Genre))
    countries = ListField(ReferenceField(Country))
    key_actors = ListField(ReferenceField(Person))
    meta = {
        'ordering': ['-likes', '-collections'],
        'collection': 'movie_movie'
    }


class Comment(Document):
    author = ReferenceField(User, reverse_delete_rule=CASCADE, required=True)
    content = StringField(max_length=1000)
    comment_time = DateTimeField(default=datetime.utcnow())
    grade = IntField(default=5)
    movie = ReferenceField(Movie, reverse_delete_rule=CASCADE)
    up_votes = IntField(default=0)
    reply = ReferenceField('self')
    meta = {
        'ordering': ['up_votes', '-comment_time'],
        'collection': 'movie_comment'
    }