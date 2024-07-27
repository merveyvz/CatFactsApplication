from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Base

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)
