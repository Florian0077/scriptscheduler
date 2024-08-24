from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.triggers.cron import CronTrigger
import importlib.util
import sys
from models import Log, Script
from database import db_session
from apscheduler.jobstores.base import JobLookupError
import os
import logging
import subprocess
import sys

# logging.getLogger("apscheduler").setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO)


class Scheduler:
    def __init__(self):
        executors = {
            "default": ThreadPoolExecutor(
                10
            )  # Utiliser un thread pool pour exécuter des tâches non bloquantes
        }
        self.scheduler = BackgroundScheduler(executors=executors)
        self.scheduler.start()
        self.load_existing_jobs()

    def load_existing_jobs(self):
        active_scripts = Script.query.filter_by(active=True).all()
        for script in active_scripts:
            self.add_job(script)

    def add_job(self, script):
        # Essayez de supprimer le job existant s'il existe, en ignorant les erreurs
        try:
            self.scheduler.remove_job(str(script.id))
        except JobLookupError:
            # Le job n'existait pas, ce n'est pas un problème
            pass

        job = self.scheduler.add_job(
            self.execute_script,
            CronTrigger.from_crontab(script.schedule),
            args=[script],
            id=str(script.id),
        )
        return job

    def remove_job(self, script):
        try:
            self.scheduler.remove_job(str(script.id))
        except JobLookupError:
            # Le job n'existe pas, donc il n'y a rien à supprimer
            print(
                f"Le job avec l'ID {script.id} n'existe pas, impossible de le supprimer."
            )

    def execute_script(self, script):
        try:
            result = subprocess.run(
                [sys.executable, script.path],
                capture_output=True,
                text=True,
                check=True,
            )
            output = result.stdout
            error = result.stderr

            log = Log(
                script_id=script.id,
                status="success",
                message=f"Script exécuté avec succès. Sortie: {output}",
            )
            if error:
                log.message += f" Erreurs: {error}"
        except subprocess.CalledProcessError as e:
            log = Log(
                script_id=script.id,
                status="error",
                message=f"Erreur lors de l'exécution: {e.output}",
            )
        except Exception as e:
            log = Log(script_id=script.id, status="error", message=str(e))

        db_session.add(log)
        db_session.commit()
