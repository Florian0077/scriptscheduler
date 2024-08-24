import random
import datetime


def main():
    number = random.randint(1, 100)
    message = f"Nombre aléatoire généré: {number} le {datetime.datetime.now()}"
    print(message)
    with open("random_number_log.txt", "a") as log_file:
        log_file.write(message + "\n")


if __name__ == "__main__":
    main()
