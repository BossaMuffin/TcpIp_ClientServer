import os
import logging
from datetime import datetime

now = datetime.now()
today_date = now.strftime("%y%m%d")
hostuser = os.getlogin()

logging.basicConfig(
    filename=f"logs/{today_date}_tcpipserver.log",
    level=logging.DEBUG,
    format=f"[{hostuser}]\t- %(asctime)s\t- %(levelname)s\t\t- %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    filemode="a"
)


def info(msg: str) -> None:
    logging.info(msg)
    print(msg)


def error(msg: str) -> None:
    logging.error(msg)
    print(msg)


def critical(msg: str) -> None:
    logging.critical(msg)
    print(msg)


def warning(msg: str) -> None:
    logging.warning(msg)
    print(msg)


if __name__ == "__main__":
    print("""
        Exemple :
        logging.debug("La fonction a bien été exécutée")
        logging.info("Message d'information général")
        logging.warning("Attention !")
        logging.error("Une erreur est arrivée")
        logging.critical("Erreur critique")
        """)
