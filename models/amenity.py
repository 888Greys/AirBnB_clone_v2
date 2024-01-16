#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        __tablename__: SQL table
        name: input name
        place_amenities: relationship to between Place & Amenity
    """

    __tabe__ = 'amenities':
    name = Column(String(128), nullable=False)
