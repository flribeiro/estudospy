import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    print("Server listening on port {}.".format(PORT))
    # server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)
    server.serve_forever()