import tcpipclient as cli

# HOST_IPV4 = '138.195.237.247'
HOST_IPV4 = '127.0.0.1'
HOST_PORT = 8080

if __name__ == '__main__':
    """
    """
    messages = ['Hello me', 'Hello Youu', 'Hello world']
    client = cli.TcpIpClient()
    print(f'\nAttend to reach the server @ {HOST_IPV4}:{HOST_PORT}')
    print('-------------------------------------\n')

    for index_msg, message in enumerate(messages):
        client.newconnectedsock(HOST_IPV4, HOST_PORT)

        if client.running:
            print(f'> Want to send the message n°{index_msg+1}')
            client.senddata(message)
            print('')
        else:
            print('> Messages can\'t be send.')
            pass

