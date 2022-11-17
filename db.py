from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCAMY_DB='sqlite:///./fake.db'
SQLALCAMY_DB='postgresql://postgres:wedid@localhost:5432/fast'

engine=create_engine(SQLALCAMY_DB)




SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False,)

Base = declarative_base()



def get_db():
    dbs=SessionLocal()
    try:
        yield dbs
    finally:
        dbs.close()
