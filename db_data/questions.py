import datetime
import sqlalchemy
from sqlalchemy import orm
import sqlalchemy.ext.declarative as dec
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class Questions(SqlAlchemyBase, SerializerMixin): # таблица с вопросами-ответами
    __tablename__ = 'questions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    quest = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ans = sqlalchemy.Column(sqlalchemy.String, nullable=True)
