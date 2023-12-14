from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create engine to connect to database
engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/warehouse")
