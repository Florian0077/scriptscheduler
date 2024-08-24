import datetime
import logging
import os


print(f"Current working directory: {os.getcwd()}")
print(f"Script directory: {os.path.dirname(os.path.abspath(__file__))}")

# Configurez le logger pour qu'il affiche les messages INFO dans la console
logging.basicConfig(level=logging.INFO)


def main():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    message = f"L'heure actuelle est {current_time} (exécuté le {datetime.datetime.now().date()})"
    logging.info(message)

    file_path = "D:\\PYTHON\\scriptscheduler\\current_time_log.txt"

    # Vérifiez si le chemin existe avant d'essayer d'écrire
    if os.path.exists(os.path.dirname(file_path)):
        with open(file_path, "a") as log_file:
            log_file.write(message + "\n")
    else:
        logging.error(
            f"Le répertoire {os.path.dirname(file_path)} n'existe pas ou n'est pas accessible."
        )


if __name__ == "__main__":
    main()
