import SocketServer
import shelve
import os

FILE = '/tmp/checkin'

class CheckinCounter(SocketServer.BaseRequestHandler):

    def handle(self):
        status = '0'
        data = self.request[0].strip()
        s = shelve.open(FILE)
        if not 'checkins' in s:
            s['checkins'] = []
        ci = s['checkins']
        if data == 'c' and len(ci) > 0:
            ci.pop()
            status = '1'
        s['checkins'] = ci
        s.close()
        socket = self.request[1]
        socket.sendto(status, self.client_address)

if __name__ == "__main__":
    HOST, PORT = "", 2323
    print "Starting server..."
    server = SocketServer.UDPServer((HOST, PORT), CheckinCounter)
    server.serve_forever()
