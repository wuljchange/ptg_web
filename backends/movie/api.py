from sanic import Blueprint
from sanic.response import json
from sanic.request import Request
from sanic.log import logger


movie = Blueprint('movie', '/movie')