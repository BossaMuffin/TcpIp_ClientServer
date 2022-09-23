import tcpipserver as srv
import logging
import os

HOST_IPV4 = '138.195.237.247'
#HOST_IPV4 = '127.0.0.1'
HOST_PORT = 8080
SEPARATOR = '-------------------------------------\n'

if __name__ == '__main__':
    hostuser = os.getlogin()
    logging.basicConfig(level=logging.DEBUG,
                        filename="tcpipserver.log",
                        filemode="a",
                        format=f"[{hostuser}] - %(asctime)s - %(levelname)s - %(message)s")

    """
    Exemple :
    logging.debug("La fonction a bien été exécutée")
    logging.info("Message d'information général")
    logging.warning("Attention !")
    logging.error("Une erreur est arrivée")
    logging.critical("Erreur critique")
    """

    server = srv.TcpIpServer(HOST_IPV4, HOST_PORT)
    logging.info("Program is starting ...")

    try:
            server.listeningforclients()
            logging.info(f'[LISTENING] server @{HOST_IPV4}:{HOST_PORT}')
            print(SEPARATOR)
    except ConnectionResetError:
            print(f'Catch ConnectionResetError : from client @{HOST_IPV4}:{HOST_PORT}')
            logging.info(f'[CLOSING] interrupt server from client @{HOST_IPV4}:{HOST_PORT}')

    except KeyboardInterrupt:
            print(f'Catch KeyboardInterrupt : asks to close the server socket @{HOST_IPV4}:{HOST_PORT}')
            logging.info(f'[CLOSING] interrupt server by keyboard @{HOST_IPV4}:{HOST_PORT}')

    server.closeserver()