import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

database_url = settings.DATABASE_URL

connect_args = {}

if settings.API_TEST:
    connect_args.update({'check_same_thread': False})
engine = sqlalchemy.create_engine(database_url, connect_args=connect_args)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
metadata = sqlalchemy.MetaData()

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
