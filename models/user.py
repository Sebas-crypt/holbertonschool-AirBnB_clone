#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """attributes of the class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
