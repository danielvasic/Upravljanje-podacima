from models import db
from models.program import Program

# program = Program(name='Python', version='3.8.2', description='Programming language')
# db.add(program)
# db.commit()

for program in db.query(Program).all():
    print(program.name, program.version, program.description)