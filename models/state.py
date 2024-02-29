#!/usr/bin/python3
"""
Defines the State class
"""
from models.base_models import BaseModel


class State(BaseModel):
    """Represent a state

    Attribute:
        name (str): The name of the state

    """
    name = ""