# client
import socket
import lldj_client
# creates socket object
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
lldj_ip = lldj_client.get_ip_for("dark")
print ("Our ip resolved with lldj_address service for 'dark' is " + lldj_ip)
host =  lldj_ip # socket.gethostname() # or just use (host = '')
port = 12727

s.connect((host, port))

tm = s.recv(4096) # msg can only be 1024 bytes long

s.close()
print("Server anwser: " + tm.decode('utf-8'))
