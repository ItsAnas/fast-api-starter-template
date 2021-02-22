from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


# Create engine from database uri
engine = create_engine(
    os.getenv("DATABASE_URI", "postgresql://dev_fixme:password_fixme@localhost:5433/fixme_db")
)

# Create global session
Session = sessionmaker(bind=engine)

# Create individual session
session = Session()

# Create base for table
Base = declarative_base()