import SocketServer

class CheckinCounter(SocketServer.BaseRequestHandler):

    def handle(self):
	print "Got Request"
        status = '0'
        data = self.request[0].strip()
	if (data == 'c'):
	    status = '1'
        socket = self.request[1]
	print "Got data: " + status
        socket.sendto(status, self.client_address)

if __name__ == "__main__":
    HOST, PORT = "66.228.50.204", 2323
    print "Starting server..."
    server = SocketServer.UDPServer((HOST, PORT), CheckinCounter)
    server.serve_forever()
