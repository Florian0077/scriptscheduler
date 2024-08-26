import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

# Configuration de la base de données
DB_NAME = "database.db"
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), DB_NAME))
engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()
