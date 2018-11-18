import time
import socket

# server

# creating a socket object
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# get local Host machine name
host = '0.0.0.0' # socket.gethostname() # or just use (host == '')
port = 12727

# bind to port
s.bind((host, port))

# Que up to 5 requests
s.listen(5)

while True:
    # establish connection
    clientSocket, addr = s.accept()
    print("got a connection from %s" % str(addr))
    b = bytes('Success!', 'utf-8')
    clientSocket.send(b)
    clientSocket.close()



