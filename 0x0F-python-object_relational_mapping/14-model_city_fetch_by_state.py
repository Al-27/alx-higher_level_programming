#!/usr/bin/python3
"""
this is a doc
"""
import sys
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from model_state import *
from model_city import *

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    res = session.query(City,State).join(State).filter(City.state_id == State.id).all()
    for c, s in res:
        print(f"{s.name}: ({c.id}) {c.name}")