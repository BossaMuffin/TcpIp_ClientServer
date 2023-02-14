import sys
import socket
sys.path.insert(0, "../log")
import log


class TcpIpClient:
    def __init__(self,
                 serv_ipv4: str = '127.0.0.1',
                 serv_port: int = 8080,
                 attempts_limit: int = 10):
        """
        :param server_ipv4:
        :param server_port:
        """
        self._serv_ipv4 = serv_ipv4
        self._serv_port = serv_port
        self.sock = None
        self.running = False
        self._attempts_limit = attempts_limit
        self.connexion_attempts = 0

    def newconnectedsock(self, server_ipv4: str, server_port: int) -> None:
        """
        :param server_ipv4:
        :param server_port:
        :return:
        """
        # Create a TCP/IP socket (INET Ipv4, STREAMing)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        try:
            self.sock.connect((server_ipv4, server_port))
            log.info(f'[CONNECTION] @{server_ipv4}:{server_port}')
            self.running = True
        except Exception as error:
            self.connexion_attempts += 1
            log.error(f'[FAIL] Connection failed on {server_ipv4}:{str(server_port)} > [{error}]')

    def senddata(self, data_to_send: str, chunk_len: int = 16) -> None:
        """
        :param data_to_send:
        :param chunk_len:
        :return:
        """
        amount_received = 0
        amount_expected = len(data_to_send)
        i_chunks_expected = amount_expected // chunk_len
        last_chunk_len = amount_expected % chunk_len
        try:
            # Send data
            print(f'> Sending to {self._serv_ipv4}:{self._serv_port}'
                  f'\n    [amount: {amount_expected}'
                  f' = {i_chunks_expected} chunks({chunk_len})'
                  f' + 1 chunk({last_chunk_len}) chars]'
                  f'\n    [message: "{data_to_send}"]')
            # Encode the message to bytes-type then send it
            self.sock.sendall(data_to_send.encode())
            # Look for the response
            while amount_received < amount_expected:
                data_received = self.sock.recv(16)
                amount_received += len(data_received)
                print(f'>> Received {data_received}')

        finally:
            #self.quitconnexion()
            self.sock.shutdown(1)

    def quitconnexion(self) -> None:
        # Clean up the connection
        print(f'> Close the connection nicely')
        self.running = False
        self.sock.close()

