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
    
    state = State(name="California")
    session_add(state,session)
    
    city = City(name="San Francisco", state_id=state.id)
    session_add(city,session)