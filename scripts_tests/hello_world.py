import datetime


def main():
    message = f"Hello World! Exécuté le {datetime.datetime.now()}"
    print(message)
    with open("hello_world_log.txt", "a") as log_file:
        log_file.write(message + "\n")


if __name__ == "__main__":
    main()
