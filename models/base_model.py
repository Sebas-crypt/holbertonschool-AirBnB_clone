#!/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Attributes:
        id (str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __init__: Public instance attributes initialization after creation
        __str__: Returns string representation of the class
        save: Updates instance attributes with current datetime and saves to storage
        to_dict: Returns a dictionary containing all keys/values of __dict__ of the instance

    """

    def __init__(self, *args, **kwargs):
        """Public instance attributes initialization after creation

        Args:
            *args (args): arguments
            **kwargs (dict): attribute values

        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, DATE_TIME_FORMAT)
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute 'updated_at' with the current datetime and saves to storage"""
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        map_objects = {}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
