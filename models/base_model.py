#!/usr/bin/python3
"""creating the base class"""
import uuid
import datetime


class BaseModel:
    """creating an empty class base"""
    def __init__(self, id, created_at, updated_at):
        """initializing the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """returns the str representation"""
        return f"[{class name}] ({self.id}) {self.__dict__}"

    def save(self):
        """updated the current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dict representation"""
        for key, value in kwargs.items():
