# from after_action import db
from orator import Model

class User(Model):
    __guarded__ = ['id']
