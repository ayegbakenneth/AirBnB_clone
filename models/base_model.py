#!/usr/bin/python3
"""This is the BaseModel class model."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """This defines the class BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """A constuctor of new BaseModel.

        Arguments:
            *args (any): Not used.
            **kwargs (dict): Key/value pairs of the args.
        """
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, datetime_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """This update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        basemodel_dict = self.__dict__.copy()
        basemodel_dict["created_at"] = self.created_at.isoformat()
        basemodel_dict["updated_at"] = self.updated_at.isoformat()
        basemodel_dict["__class__"] = self.__class__.__name__
        return basemodel_dict

    def __str__(self):
        """This print string representation of the BaseModel instance."""
        name_class = self.__class__.__name__
        return "[{}] ({}) {}".format(name_clas, self.id, self.__dict__)
