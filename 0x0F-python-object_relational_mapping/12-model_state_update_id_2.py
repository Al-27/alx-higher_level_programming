#!/usr/bin/python3
"""
this is a doc
"""
import sys
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from model_state import *

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    id2 = session.query(State).filter(State.id == 2).first()
    id2.name = "New Mexico"
    session.commit()
    