import json
from mongoengine import *


with open('prod.json', 'r') as config:
    loaded_cfg = json.load(config)
    mongodb_cfg = loaded_cfg['mongodb']


class DbConfig:
    def __init__(self, db: str):
        self.connect = connect(db=db, host=mongodb_cfg['host'], port=mongodb_cfg['port'],
                               username=mongodb_cfg['username'], password=mongodb_cfg['password'])
