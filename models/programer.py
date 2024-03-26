from sqlalchemy import Column, Integer, String
from models.base import Base
from sqlalchemy.orm import relationship

class Programmer(Base):
    __tablename__ = 'programmers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    git = Column(String(500))
    email = Column(String(255))
    password = Column(String(255))

    programs = relationship('Program', secondary='programer_program', back_populates='programers')

