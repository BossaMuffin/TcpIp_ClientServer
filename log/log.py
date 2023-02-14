#!/usr/bin/env python
# coding: utf-8
# Bossa Muffin log system v1 - 29/09/2022

import os
import logging
from datetime import datetime

HELP = """
        CONFIGURATION :
            filename=f"logs/{today_date}_{__name__}.log",
            level=logging.DEBUG,
            format de message =f"[{hostuser}]\t- %(asctime)s\t- %(levelname)s\t\t- %(message)s",
            filemode="a"
        
        EXEMPLE :
        #log.debug("La fonction a bien été exécutée")   -> [root]	- 27-Sep-22 13:38:24	- DEBUG		- La fonction a bien été exécutée
        log.info("Message d'information général")       -> [root]	- 27-Sep-22 13:38:24	- INFO		- Message d'information général
        log.warning("Attention !")                      -> [root]	- 27-Sep-22 13:38:24	- WARNING	- Attention !
        log.error("Une erreur est arrivée")             -> [root]	- 27-Sep-22 13:38:24	- ERROR		- Une erreur est arrivée
        log.critical("Erreur critique")                 -> [root]	- 27-Sep-22 13:38:24	- CRITICAL	- Erreur critique
        """

now = datetime.now()
today_date = now.strftime("%y%m%d")
hostuser = os.getlogin()

logging.basicConfig(
    filename=f"logs/{today_date}.log",
    level=logging.DEBUG,
    format=f"[{hostuser}]\t- %(asctime)s\t- %(levelname)s\t\t- %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    filemode="a"
)



def info(msg: str) -> None:
    logging.info(msg)
    print(msg)

def debug(msg: str) -> None:
    logging.debug(msg)
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
    print(HELP)
