#!/usr/bin/python3
"""A State class that also inherit from BaseModel."""
from models.base_model import BaseModel

class State(BaseModel):
    """A state class.

    Public class attributes:
        name (str): The name of the state.
    """

    name = ""
