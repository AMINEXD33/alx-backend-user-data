#!/usr/bin/env python3
""" a module that contains the User model :) """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    A model for User db
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True,  autoincrement=True)
    email = Column(String(length=250), nullable=False)
    hashed_password = Column(String(length=250), nullable=True)
    session_id = Column(String(length=250), nullable=True)
    reset_token = Column(String(length=250), nullable=True)
