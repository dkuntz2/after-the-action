# from .user import User
from orator import Model
from orator.orm import has_many, belongs_to
import inflection

class _Model(Model):
    __primary_key__ = 'pk'

    @classmethod
    def columns(cls):
        connection = cls.resolve_connection()
        columns = connection.get_schema_manager().list_table_columns(cls.__table__ or inflection.tableize(cls.__name__))
        return {name: column.get_type() for name, column in columns.items()}

    # HACK!!!
    #   Done to allow templates to use column names as a variable
    #       {% set column = 'pk' %}
    #       {{ user[column] }}
    def __getitem__(self, item):
        return getattr(self, item)

class User(_Model):
    @has_many("user_fk")
    def reports(self):
        return Report

class Report(_Model):
    @belongs_to("user_fk")
    def author(self):
        return User
