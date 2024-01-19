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
    res = session.query(State).filter(State.name.like("%a%")).all()
    for r in res:
        session.delete(r)
    session.commit()