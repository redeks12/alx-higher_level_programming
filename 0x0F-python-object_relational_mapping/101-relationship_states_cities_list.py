#!/usr/bin/python3
"""this lists all the states in the given database"""

import sys

from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("     {}: {}".format(city.id, city.name))
