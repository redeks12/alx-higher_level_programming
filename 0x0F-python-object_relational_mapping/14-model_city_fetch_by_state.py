#!/usr/bin/python3
"""this lists all the states in the given database"""

import sys

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
        session.query(State, City.id, City)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for st in cities:
        print(st)
        # print("{}: ({}) {}".format(st.id, st.name))
