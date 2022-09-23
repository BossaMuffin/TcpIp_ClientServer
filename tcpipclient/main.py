import tcpipclient as cli
from time import sleep
from typing import List

HOST_IPV4 = '138.195.237.247'
#HOST_IPV4 = '127.0.0.1'
HOST_PORT = 8080
ATTEMPTS_LIMIT = 10
ATTEMPTS_BUFFER = 0
MESSAGES_LIST = [
    'Hello Me.',
    'Helloo YooU :)',
    'HellooO WooOrld !',
]
SEPARATOR = '-------------------------------------\n'

def runmessagessender(client,
                      buffer:int = ATTEMPTS_BUFFER,
                      messages:List[str] = [
                          'Hello Me.',
                          'Helloo YooU :)',
                          'HellooO WooOrld !',
                      ]):
    """

    :param client:
    :param dest_ipv4:
    :param dest_port:
    :param messages:
    :return:
    """
    index_connexion = 0
    try_to_connect = True
    while try_to_connect:

        for index_msg, message in enumerate(messages):
            sleep(buffer)
            index_connexion += 1

            if client.connexion_attempts >= client.attempts_limit:
                print(SEPARATOR)
                print(f'Limit of attempts is reached [{client.connexion_attempts}] on {client.serv_ipv4}:{str(client.serv_port)}')
                try_to_connect = False
                break
            else:
                client.newconnectedsock(client.serv_ipv4, client.serv_port)


            if client.running:
                print(f'Connexion n°{index_connexion}')
                print(f'> Want to send the message n°{index_msg + 1}')
                client.senddata(message)
                print('')
            else:
                print(f'Connexion n°{index_connexion} failed')
                print('> Messages can\'t be send.')


if __name__ == '__main__':
    """
    """
    client = cli.TcpIpClient(HOST_IPV4, HOST_PORT, ATTEMPTS_LIMIT)
    print(f'\nAttend to reach the server @{HOST_IPV4}:{HOST_PORT}')
    print(SEPARATOR)
    try:
        runmessagessender(client, ATTEMPTS_BUFFER, MESSAGES_LIST)
        print(SEPARATOR)
        print(f'End of work : asks to interrupt client connexion @{HOST_IPV4}:{HOST_PORT}')
    except KeyboardInterrupt:
        print(SEPARATOR)
        print(f'Catch KeyboardInterrupt : asks to interrupt client connexion @{HOST_IPV4}:{HOST_PORT}')


    client.quitconnexion()
