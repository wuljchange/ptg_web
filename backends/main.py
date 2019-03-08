from arrow.arrow import datetime
from sanic.log import logger
from sanic import Sanic
from sanic.request import Request
from sanic.response import redirect, json
from .comm.helper import authenticate
from .user.api import user
from .user.models import User, Session
from .movie.api import movie
from .config.config import loaded_cfg


app = Sanic('ptg_web')
app.blueprint(user)
app.blueprint(movie)


@app.listener('after_server_start')
async def notify_server_started(app, loop):
    print('Server start successfully')


@app.listener('after_server_stop')
async def notify_server_stopping(app, loop):
    print('Server stopped successfully')


@app.middleware('request')
async def check_token(request: Request):
    response = authenticate(request)
    if request.path in ['/login', '/register']:
        logger.info('login or register')
    elif response:
        response.update(created=datetime.utcnow())
        logger.info('update {} created value'.format(User.objects.get(pk=response.uid)))
    else:
        return json({'alert': 'please login or register first'}, status=403)


if __name__ == "__main__":
    app.run(host=loaded_cfg['host'], port=loaded_cfg['port'], debug=loaded_cfg['debug'])