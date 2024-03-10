#!/usr/bin/python3
"""FileStorage class defination."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """FileStorage that serializes instances to and from a JSON file.

    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): dictionary - empty but will store all objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        object_storage = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_storage, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        instance_dict = FileStorage.__objects
        instances = {obj: instance_dict[obj].to_dict() for obj in instance_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(instances, f)

    def reload(self):
        """deserializes the JSON file to __objects only if the JSON file (__file_path) exists."""
        try:
            with open(FileStorage.__file_path) as f:
                instances = json.load(f)
                for k in instances.values():
                    class_name = k["__class__"]
                    del k["__class__"]
                    self.new(eval(class_name)(**k))
        except FileNotFoundError:
            return
