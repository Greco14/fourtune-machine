import socket, os
from SocketServer import BaseServer
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from OpenSSL import SSL

FOUR
SQ_SECRET = ''

class SecureHTTPServer(HTTPServer):
    def __init__(self, server_address, HandlerClass):
	BaseServer.__init__(self, server_address, HandlerClass)
	ctx = SSL.Context(SSL.SSLv23_METHOD)
        # server.pem's location (containing the server private key and
        # the server certificate).
	fpem = '/tmp/server.pem'
	ctx.use_privatekey_file (fpem)
	ctx.use_certificate_file(fpem)
	self.socket = SSL.Connection(ctx, socket.socket(self.address_family,
			self.socket_type))
	self.server_bind()
	self.server_activate()


class SecureHTTPRequestHandler(SimpleHTTPRequestHandler):
    def setup(self):
        self.connection = self.request
	self.rfile = socket._fileobject(self.request, "rb", self.rbufsize)
	self.wfile = socket._fileobject(self.request, "wb", self.wbufsize)

def recvCheckIn(HandlerClass = SecureHTTPRequestHandler,
				ServerClass = SecureHTTPServer):
    server_address = ('', 443) # (address, port)
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsockname()
    print "Serving HTTPS on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()

if __name__ == '__main__':
    recvCheckIn()
