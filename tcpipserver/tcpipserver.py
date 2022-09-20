import socket


class TcpIpServer:
    """
    """
    def __init__(self, server_ipv4: str, server_port: int):
        """

        :param server_ipv4:
        :param server_port:
        """
        self.ipv4 = server_ipv4
        self.port = server_port
        self.sock = None
        self.running = False
        self.newlisteningsock(self.ipv4, self.port)

    def newlisteningsock(self, server_ipv4: str, server_port: int):
        """

        :param server_ipv4:
        :param server_port:
        :return:
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to a public host, and a well-known port
        self.sock.bind((server_ipv4, server_port))
        print(f'\nStarting up on {server_ipv4}:{server_port}')
        print('--------------------------------')
        # Become a server socket for 5 simultaneous connexion requests
        self.sock.listen(5)
        self.running = True

    def listeningforclients(self):
        """

        :return:
        """
        while self.running:
            # Accept connections from outside
            print(f'\nWaiting for a connection')
            print('...\n')
            client_connection, client_ipv4 = self.sock.accept()
            # Now do something with the client socket
            self._receiveddata(client_connection, client_ipv4)

    def _receiveddata(self, client_connection, client_address: str, chunk_len: int = 16):
        """

        :param client_connection:
        :param client_address:
        :param chunk_len:
        :return:
        """
        i_chunk = 0
        chunks = []
        try:
            print(f'> Connection from {client_address}')
            # Receive the data in small chunks and retransmit it

            while True:
                data_received = client_connection.recv(chunk_len)
                i_chunk += 1
                print(f'>> Chunk n°{i_chunk} received : "{data_received}"')
                chunks.append(data_received)

                if data_received:
                    print(f'>> Sending data back to the client {client_address} [at chunk n°{i_chunk}]')
                    client_connection.sendall(data_received)
                else:
                    print(f'>> No more data from {client_address} [after {i_chunk} chunks]')
                    break
        finally:
            message_received = b''.join(chunks)
            amount_received = len(message_received)
            i_full_chunks = amount_received // chunk_len
            last_chunk_len = amount_received % chunk_len

            print(f'> Message from {client_address}'
                  f'\n    [amount: {amount_received}'
                  f' = {i_full_chunks} chunks({chunk_len})'
                  f' + 1 chunk({last_chunk_len}) chars]'
                  f'\n    [message: "{message_received}"]')
            # Clean up the connection
            print(f'> Close the connection with {client_address}')
            client_connection.close()


    def closeServer(self):
        """

        :return:
        """
        print(f'Stop the server.')
        try:
            self.sock.close()
            self.running = False
        except Exception as error:
            print(f'Server doesn\'t stop [{error}]')
