from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql:///practice")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


class Blockchain(Base):
    __tablename__ = "Blockchain"
    id = Column(Integer, primary_key=True)
    bc_name = Column(String)
    bc_supply = Column(String)
    bc_launch_date = Column(String)
    bc_ath = Column(String)

Base.metadata.create_all()

# CRUD (Create, Read, Update, Delete)
# CREATE
bc_bitcoin = Blockchain(
    bc_name="Bitcoin",
    bc_supply="21.000.000",
    bc_launch_date="Jan 3, 2009",
    bc_ath="Nov 10, 2021"
)

bc_ethereum = Blockchain(
    bc_name="Ethereum",
    bc_supply="120.208.383",
    bc_launch_date="Jul 30, 2015",
    bc_ath="Nov 10, 2021"
)

bc_bnb = Blockchain(
    bc_name="Binance Coin",
    bc_supply="157.900.714",
    bc_launch_date="Jul 8, 2017",
    bc_ath="May 10, 2021"
)

bc_frank = Blockchain(
    bc_name="Frank Coin",
    bc_supply="157.900.714",
    bc_launch_date="April 7, 2017",
    bc_ath="April 10, 2021"
)

# session.add(bc_bitcoin)
# session.add(bc_ethereum)
# session.add(bc_bnb)
# session.add(bc_frank)
# session.commit()

# UPDATE DataBases, specific

# update_bc = session.query(Blockchain).filter_by(id=3).first()
# update_bc.bc_supply = bc_bnb.bc_supply
# session.commit()
# UPDATE DataBase, general

# to_change = session.query(Blockchain)
# for update in to_change:
#     tstore = update.bc_ath
#     tstore2 = update.bc_supply
#     if update.id is not None:
#         update.bc_ath = f'{tstore}'
#         print(f'"{update.bc_ath}" - Printed successfully')
#         if update.bc_supply is not None:
#             update.bc_supply = f'Amount: {tstore2}'
#             print(f'"{update.bc_supply}" - Printed successfully')
#     else:
#         print('Data not found!')
#     session.commit()

# DELETE & Defensive programming

# name_bc = input('Blockchain Name: ')

# blockchain_name = session.query(Blockchain).filter_by(bc_name=name_bc).first()

# if blockchain_name is not None:
#     print(f'Blockchain Found: {name_bc}')
#     confirmation = input('Are you sure you want to delete the data? y/n: ')
#     if confirmation.lower() == 'y':
#         session.delete(blockchain_name)
#         session.commit()
#         print('Blockchain Deleted')
#     else:
#         print('Blockchain not deleted')
# else:
#     print('Blockchain not found')

# DELETE all


# READ
bc_networks = session.query(Blockchain)
for bc in bc_networks:
    print(
        bc.id,
        bc.bc_name,
        bc.bc_supply,
        bc.bc_launch_date,
        bc.bc_ath,
        sep=" | "
    )
