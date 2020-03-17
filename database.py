import sqlalchemy
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

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

metadata.create_all(engine)
