#!/usr/bin/python3

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]),
    pool_pre_ping=True,
)

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()
for state in states:
    print("{}: {}".format(state.id, state.name))
