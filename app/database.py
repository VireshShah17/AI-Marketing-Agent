from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session


DATABASE_URL = "sqlite:///./marketing_agent.db" # Using SQLite for simplicity; replace with your database URL as needed
engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread": False}) # Only needed for SQLite; remove for other databases
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine) # Create a configured "Session" class
Base = declarative_base() # Base class for our models


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
