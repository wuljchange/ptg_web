from sanic.request import Request
from ..user.models import Session, User
import hashlib


def authenticate(request: Request):
    token = request.cookies.get('token', '')
    if Session.objects(token=token):
        response = Session.objects.get(token=token)
        return response
    else:
        return None


def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()