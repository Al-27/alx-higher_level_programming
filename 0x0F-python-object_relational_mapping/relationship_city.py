#!/usr/bin/python3
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base

class City(Base):
    """
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,ForeignKey("states.id") )