from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# excecuting the chinook dataBase
db = create_engine("postgresql:///chinook")

# grab metadata and return subclass to map all back to us
Base = declarative_base()


# create a class-Based model for the 'Programmer' table schema

class Programmer(Base):
    __tablename__ = 'Programmer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# Set instance of sessionmaker to use 'db'

Session = sessionmaker(db)

# Open session by using the Session subclass above & stores result

session = Session()

# Create dataBase using the declarative_Base subclass 'Base'

Base.metadata.create_all(db)

# Create a table of 'Ada Lovelace'
ada_lovelace = Programmer(
    first_name='Ada',
    last_name='Lovelace',
    gender='F',
    nationality='British',
    famous_for='First Programmer'

)

alan_turing = Programmer(
    first_name='Alan',
    last_name='Turin',
    gender='M',
    nationality='British',
    famous_for='Modern Computing'

)

grace_hopper = Programmer(
    first_name='Grace',
    last_name='Hopper',
    gender='F',
    nationality='USA',
    famous_for='Compiler & COBOL language'

)

maraget_halimton = Programmer(
    first_name='Margaret',
    last_name='Hamilton',
    gender='F',
    nationality='USA',
    famous_for='Software Engineering & Code for the Apollo 11'

)

bill_gates = Programmer(
    first_name='Bill',
    last_name='Gates',
    gender='M',
    nationality='USA',
    famous_for='Microsoft'

)

bill_gates = Programmer(
    first_name='Bill',
    last_name='Gates',
    gender='M',
    nationality='USA',
    famous_for='Microsoft'

)

tim_berners_lee = Programmer(
    first_name='Tim',
    last_name='Berners Lee',
    gender='M',
    nationality='British',
    famous_for='World Wide Web'

)

frank_arellano = Programmer(
    first_name='Frank',
    last_name='Arellano',
    gender='M',
    nationality='Venezuelan',
    famous_for='Software Engineering'

)

# add each instace of our programmers to our session

# session.add(ada_lovelace) # already commited
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(maraget_halimton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(frank_arellano)


# Update DataBases, specific

# programmer_update = session.query(Programmer).filter_by(id=7).first()
# programmer_update.famous_for = "World President"

# Update DataBase, general

people = session.query(Programmer)
for person in people:
    if person.gender == "F":
        person.gender = "Female"
    elif person.gender == "M":
        person.gender = "Male"
    else:
        print('Gender undefined')
    session.commit()

# commit session to the dataBase

# session.commit()

# query the dataBase to find our creation

programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + ' ' + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
