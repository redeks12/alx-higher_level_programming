#!/usr/bin/python3

import sys

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# from model_state import State

engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]),
    pool_pre_ping=True,
)
Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(
        Integer, primary_key=True, nullable=False, unique=True, autoincrement=True
    )
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker()
session = Session()

states = session.query(State).all()
for state in states:
    print("{}: {}".format(state.id, state.name))
