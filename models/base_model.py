#!/usr/bin/python3
"""A class BaseModel defining common attributes/methods for other classes"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialization constructor of a new BaseModel.

        Args:
            *args (any): Not used in this project.
            **kwargs (dict): Holding Key/value pairs of attributes.
        """
        datetime_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.current()
        self.updated_at = datetime.current()
        if len(kwargs) != None:
            for key, value in kwargs.items():
                if key == "created_at" | key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, datetime_form)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Save and update at the current datetime of instance creation."""
        self.updated_at = datetime.current()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance."""
        ken = self.__dict__.copy()
        ken["created_at"] = self.created_at.isoformat()
        ken["updated_at"] = self.updated_at.isoformat()
        ken["__class__"] = self.__class__.__name__
        return ken

    def __str__(self):
        """String representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
