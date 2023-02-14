import socket
import sys

sys.path.insert(0, "../log")
import log


class TcpIpServer:

    def __init__(self, server_ipv4: str, server_port: int, clients_limit: int = 10):
        self._ipv4 = server_ipv4
        self._port = server_port
        self.sock = None
        self.running = False
        self.clients = 0
        self._clients_limit = clients_limit
        self.newlisteningsock(self._ipv4, self._port)

    def newlisteningsock(self, server_ipv4: str, server_port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to a public host, and a well-known port
        self.sock.bind((server_ipv4, server_port))
        print(f'\nStarting up on {server_ipv4}:{server_port}')
        print('--------------------------------')
        # Become a server socket for 5 simultaneous connexion requests
        self.sock.listen(5)
        self.running = True

    def listeningforclients(self) -> None:
        while self.running and self.clients < self._clients_limit:
            # Accept connections from outside
            print(f'\nWaiting for a connection')
            print('...\n')
            client_connection, client_ipv4 = self.sock.accept()
            self.clients += 1
            # Now do something with the client socket
            self._receiveddata(client_connection, client_ipv4)

    def _receiveddata(self,
                      client_connection,
                      client_address: str,
                      chunk_len: int = 16
                      ) -> None:
        i_chunk = 0
        chunks = []
        try:
            log.info(f'[CONNECTION] from {client_address}')
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
            log.info(f'[RECEIVED] from {client_address}, amount: {amount_received}, by: {chunk_len} chunks')
            # Clean up the connection
            print(f'> Close the connection with {client_address}')
            client_connection.shutdown(1)

    def closeserver(self) -> None:
        try:
            self.sock.shutdown(1)
            self.sock.close()
            print(f'Stop the server nicely.')
            self.running = False
        except Exception as err:
            log.warning(f'[ERROR] Server doesn\'t stop [{err}]')
