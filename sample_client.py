import socket

IP = '66.228.50.204'
PORT = 2323
MESSAGE = 'c'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (IP, PORT))
recived = sock.recv(1024)

print recived
