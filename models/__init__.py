from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.programer import Programmer
from models.program import Program
from models.programer_program import programer_program

engine = create_engine('mysql+pymysql://root:lozinka@localhost:3306/programmers')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db = Session()