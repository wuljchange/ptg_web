import uuid
from sanic import Blueprint
from sanic.request import Request
from sanic.response import json
from sanic.log import logger
from arrow.arrow import datetime
from .models import User, Session
from ..comm.helper import encrypt_password, authenticate
import json as js


user = Blueprint('user', '')


@user.route('/login', methods=['POST'])
async def login(request: Request):
    data = js.load(request.json)
    username = data.get('username', '')
    password = data.get('password', '')
    response = User.objects.get(name=username)
    if not response:
        return json({'alert': ['User not registered']}, 403)
    if response.password != encrypt_password(password):
        return json({'alert': ['Password does not match']}, 403)
    token = uuid.uuid4().hex
    sess = Session(uid=str(response.id), token=token, created=datetime.utcnow())
    sess.save()
    logger.info('login success')
    return json({'token': token})


@user.route('/register', methods=['POST'])
async def register(request: Request):
    data = js.load(request.json)
    response = User.objects.get(name=data.get('username', ''))
    if response:
        return json({'alert': ['User already registered']}, 403)
    token = uuid.uuid4().hex
    data['password'] = encrypt_password(data['password'])
    user = User(**data)
    user.save()
    sess = Session(uid=user.id, token=token, created=datetime.utcnow())
    sess.save()
    logger.info('register success')
    return json({'token': token})


@user.route('/logout', methods=['POST'])
async def logout(request: Request):
    token = request.cookies.get('token')
    Session.objects(token=token).delete()
    return json(True)


@user.route('/modify', methods=['POST'])
async def modify(request: Request):
    data = js.load(request.json)
    user = User.objects(name=data.pop('username'))
    user.update(**data)
    user.reload()
    return json(True)
