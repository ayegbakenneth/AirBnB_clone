#!/usr/bin/python3
"""The City class."""
from models.base_model import BaseModel

class City(BaseModel):
    """Defines a class city.

    Public class attributes:
        state_id (str): The id of the state.
        name (str): The city name.
    """

    state_id = ""
    name = ""
