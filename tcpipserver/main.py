import tcpipserver as srv

#HOST_IPV4 = '138.195.237.247'
HOST_IPV4 = '127.0.0.1'
HOST_PORT = 8080

if __name__ == '__main__':
        server = srv.TcpIpServer(HOST_IPV4, HOST_PORT)
        server.listeningforclients()

        server.closeServer()

