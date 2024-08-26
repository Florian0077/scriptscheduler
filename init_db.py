import logging
from sqlalchemy import inspect
from database import Base, engine
from models import Script, Log  # Importez vos modèles ici

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db():
    try:
        logger.info(f"Modèles importés : Script={Script}, Log={Log}")
        logger.info(
            f"Tables dans les métadonnées avant création : {Base.metadata.tables.keys()}"
        )

        # Création des tables
        logger.info("Tentative de création de toutes les tables...")
        Base.metadata.create_all(bind=engine)

        # Vérification des tables créées
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        logger.info(f"Tables créées : {tables}")

        if not tables:
            logger.warning("Aucune table n'a été créée!")

    except Exception as e:
        logger.error(f"Erreur lors de l'initialisation de la base de données : {e}")
        raise


if __name__ == "__main__":
    init_db()
