from sqlalchemy import Column, Integer, Float, Date, Table, ForeignKey
from models.base import Base

programer_program = Table('programer_program', Base.metadata,
                          Column('programer_id', Integer, ForeignKey(
                              'programmers.id'), primary_key=True),
                          Column('program_id', Integer, ForeignKey(
                              'programs.id'), primary_key=True),
                          Column('price', Float),
                          Column('date', Date),
                          )
