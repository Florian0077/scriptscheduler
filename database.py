from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

# Configuration de la base de données
engine = create_engine("sqlite:///database.db", echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """
    Initialise la base de données en créant toutes les tables définies dans les modèles.
    """
    # Importation des modèles ici pour éviter l'import circulaire
    from models import Script, Log  # Importer les modèles dans la fonction

    Base.metadata.create_all(engine)
    print("Base de données initialisée avec succès.")


if __name__ == "__main__":
    init_db()
