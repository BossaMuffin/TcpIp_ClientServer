import sys
import tcpipclient as cli
from time import sleep
from config import read
sys.path.insert(0, "../log")
import log

__ATTEMPTS_BUFFER_MIN: int = 1

config = read("config/config.json")


def runmessagessender(client,
                      __buffer: int=config.ATTEMPTS_BUFFER,
                      messages=None) -> None:
    if messages is None:
        messages = [
            'Hello Me.',
            'Helloo YooU :)',
            'HellooO WooOrld !',
        ]
    index_connexion = 0
    try_to_connect = True
    while try_to_connect:

        for index_msg, message in enumerate(messages):
            sleep(__buffer)
            index_connexion += 1

            if client.connexion_attempts >= client._attempts_limit or client._attempts_limit < 1:
                print(config.SEPARATOR)
                log.warning(f'[LIMIT] low(1) or reached limit({client.connexion_attempts}) @{client._serv_ipv4}:{str(client._serv_port)}')
                try_to_connect = False
                break
            else:
                client.newconnectedsock(client._serv_ipv4, client._serv_port)

            if client.running:
                log.info(f'[SENDING] Connexion n°{index_connexion} - message n°{index_msg + 1}')
                client.senddata(message)
                print('')
            else:
                log.error(f'[ERROR] Connexion n°{index_connexion} failed - Messages can\'t be send.')


if __name__ == '__main__':
    log.info("Clients script is starting ...")
    client = cli.TcpIpClient(config.HOST_IPV4, config.HOST_PORT, config.ATTEMPTS_LIMIT)
    log.info(f'\n[CONNECTING] On server @{config.HOST_IPV4}:{config.HOST_PORT}')
    print(config.SEPARATOR)

    if config.ATTEMPTS_BUFFER >= __ATTEMPTS_BUFFER_MIN :
        try:
            runmessagessender(client, config.ATTEMPTS_BUFFER, config.MESSAGES_LIST)
        except ConnectionResetError:
            print(config.SEPARATOR)
            log.critical(f'[CLOSING] ConnectionResetError @{client._serv_ipv4}:{client._serv_port}')
        except KeyboardInterrupt:
            print(config.SEPARATOR)
            log.critical(f'[CLOSING] KeyboardInterrupt @{client._serv_ipv4}:{client._serv_port}')
        client.quitconnexion()
    else:
        log.critical(f'[BUFFER] low({config.ATTEMPTS_BUFFER}) < min({__ATTEMPTS_BUFFER_MIN}) @{client._serv_ipv4}:{str(client._serv_port)}')


