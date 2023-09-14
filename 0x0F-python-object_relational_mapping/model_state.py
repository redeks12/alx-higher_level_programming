#!/usr/bin/python3
"""Start link class to table in database 
"""

from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id: Mapped[int] = mapped_column(
        nullable=False,
        primary_key=True,
        autoincrement=True,
        unique=True,
    )
    name: Mapped[str] = mapped_column(nullable=False)
