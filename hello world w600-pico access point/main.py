#inspired from https://maker.pro/forums/threads/w600-pico-webserver.292684/

#create access point
import easyw600 
easyw600.createap(ssid="W600_softAP") 
#create ftp server ( can be manipulate with dos ftp or the free ftp https://filezilla-project.org/
import w600 
w600.run_ftpserver(port=21,username="user",password="12345678") 

# setup the webserver
try:
    import usocket as socket
except:
    import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket, address family type = AF_INET, socket type = SOCK_STREAM
s.bind(('', 80))
s.listen(5) # accept connections. backlog = 5 = max. number of unaccepted connections before refusing new connections



# this is the main loop to handle requests
while True:
    conn, addr = s.accept() # accept connection with a new socket object "conn" to remote address "addr"
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-type: text /html\n")
    conn.send("Connection: close\n\n")
    #response
    conn.sendall("hello world!")
    conn.close()
 