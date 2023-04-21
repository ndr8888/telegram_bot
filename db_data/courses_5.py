import datetime
import sqlalchemy
from sqlalchemy import orm
import sqlalchemy.ext.declarative as dec
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class Courses5(SqlAlchemyBase, SerializerMixin):  # таблица с вопросами-ответами
    __tablename__ = 'courses5'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
