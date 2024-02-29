#!/usr/bin/python3
"""City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """attributes of the class City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
