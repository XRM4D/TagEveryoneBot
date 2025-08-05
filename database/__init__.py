from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from settings.config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB

sql_uri = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres/{POSTGRES_DB}"

engine = create_engine(sql_uri)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

def init_db():
    from database.users import User
    from database.chats import Chat
    Base.metadata.create_all(engine)