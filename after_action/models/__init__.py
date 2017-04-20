# from .user import User
from orator import Model
from orator.orm import has_many, belongs_to

class _Model(Model):
    __primary_key__ = 'pk'

class User(_Model):
    @has_many("user_fk")
    def reports(self):
        return Report

class Report(_Model):
    @belongs_to("user_fk")
    def author(self):
        return User
