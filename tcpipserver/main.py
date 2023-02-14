import tcpipserver as srv
import sys
from config import read_config
sys.path.insert(0, "../log")
import log

config = read_config("config/config.json")

if __name__ == '__main__':
    server = srv.TcpIpServer(config.HOST_IPV4, config.HOST_PORT, config.CONNEXIONS_LIMIT)
    log.info("[BEGIN] Server script is starting ...")

    try:
        server.listeningforclients()
        log.info(f'[LISTENING] server @{config.HOST_IPV4}:{config.HOST_PORT}')
        print(config.SEPARATOR)
    except ConnectionResetError:
        log.critical(
            f'[CLOSING] ConnectionResetError : interrupt server from client @{config.HOST_IPV4}:{config.HOST_PORT}')
    except KeyboardInterrupt:
        log.critical(f'[CLOSING] KeyboardInterrupt : interrupt server @{config.HOST_IPV4}:{config.HOST_PORT}')

    server.closeserver()
