import SocketServer

class CheckinCounter(SocketServer.BaseRequestHandler):

    def handle(self):
        status = 0
        data = self.request[0].strip()
	if (data == 'c'):
	    status = 1
        socket = self.request[1]
        socket.sendto(status, self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 2323
    print "Starting server..."
    server = SocketServer.UDPServer((HOST, PORT), CheckinCounter)
    server.serve_forever()
