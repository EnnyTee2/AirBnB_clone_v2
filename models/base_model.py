#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime

import models

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(
        String(60),
        primary_key=True,
        unique=True,
        nullable=False,
        default=str(uuid.uuid4())
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        """Return a dictionary representation of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        dico = self.__dict__.copy()
        dico["__class__"] = str(type(self).__name__)
        dico["created_at"] = self.created_at.isoformat()
        dico["updated_at"] = self.updated_at.isoformat()
        dico.pop("_sa_instance_state", None)
        return dico
    
    

    def delete(self):
        models.storage.delete(self)
        models.storage.save()
