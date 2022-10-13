#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Represents a state for a MySQL database.
    Inherits from the SQLAlchemy Base and links to the MySQL table states.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(
        String(128),
        nullable=False)

    cities = relationship("City", backref="state",
                          cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            _cities = []

            all_cities = models.storage.all(City)

            for city_key in all_cities:
                if all_cities[city_key].state_id == self.id:
                    _cities.append(all_cities[city_key].state_id)

            return _cities
