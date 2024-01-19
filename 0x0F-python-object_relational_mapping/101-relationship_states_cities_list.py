#!/usr/bin/python3
"""
this is a doc
"""
import sys
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from relationship_state import *
from relationship_city import *

def session_add(obj,sess):
    sess.add(obj)
    sess.commit()

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    
    states = session.query(State).order_by(asc(State.id)).all()
    
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")