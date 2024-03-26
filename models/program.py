from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.programer_program import programer_program


class Program(Base):
    __tablename__ = 'programs'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    version = Column(String(255))
    description = Column(String(255))

    programers = relationship('Programmer', secondary='programer_program', back_populates='programs')