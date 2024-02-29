#!/usr/bin/python3
"""State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """attributes of the class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
