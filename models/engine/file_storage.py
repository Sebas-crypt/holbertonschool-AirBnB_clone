#!/usr/bin/python3
"""File Storage class"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    This class represents a file storage
    system for objects in the AirBnB clone project.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects currently stored."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage system."""
        key = type(obj).__name__ + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves the objects to a JSON file."""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Loads the objects from a JSON file."""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = {k: BaseModel(**v)
                                  for k, v in json.load(file).items()}
        except Exception:
            pass
