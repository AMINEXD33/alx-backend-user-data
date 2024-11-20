#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        a function that adds a new user to the database
        and returns a User object
        """
        tmp = User(email=email, hashed_password=hashed_password)
        self._session.add(tmp)
        self._session.flush()
        return tmp

    def find_user_by(self, **kwargs) -> User:
        """
        a function that finds a user with some args
        and returns the  User object, or raise an error if the kwargs
        are wrong or no User was found
        """
        keys: list[str] = [
            "id",
            "email",
            "hashed_password",
            "session_id",
            "reset_token",
        ]
        # check keys
        for key in kwargs.keys():
            if key not in keys:
                raise InvalidRequestError
        # try and kind the user with such keys
        potential_user = self.__session.query(User).filter_by(**kwargs).first()
        if potential_user is None:
            raise NoResultFound
        return potential_user
