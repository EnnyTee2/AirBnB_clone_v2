#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.city import City
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(
        String(128),
        nullable=False,
    )

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        _cities = []

        all_cities = models.storage.all(City)

        for city_key in all_cities:
            if all_cities[city_key].state_id == self.id:
                _cities.append(all_cities[city_key].state_id)

        return _cities
