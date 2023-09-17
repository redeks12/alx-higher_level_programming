#!/usr/bin/python3
"""this lists all the states in the given database"""

import sys

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine, join, select
from sqlalchemy.orm import aliased, sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    city_a = aliased(City)
    state_a = aliased(State)
    city = (
        session.query(state_a.name, city_a.id, city_a.name).join(
            state_a, state_a.id == city_a.state_id
        )
    ).all()

    for st in city:
        print(st)
        # print("{}: ({}) {}".format(st.id, st.name))
