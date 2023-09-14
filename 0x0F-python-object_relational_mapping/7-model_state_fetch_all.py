#!/usr/bin/python3

import sys

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State

# from model_state import State

engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]),
    pool_pre_ping=True,
)

Base.metadata.create_all(bind=engine)
Session = sessionmaker()
session = Session()

states = session.query(State).all()
for state in states:
    print("{}: {}".format(state.id, state.name))
