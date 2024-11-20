#!/usr/bin/env python3
""" a module that contains the User model :) """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    A model for User db
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(length=250))
    hashed_password = Column(String(length=250))
    session_id = Column(String(length=250))
    reset_token = Column(String(length=250))
for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
