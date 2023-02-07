import socket
		
s = socket.socket()
s.bind(('',80))
s.listen(5)

def web_page():
    file = open("submit.html", "r")
    page = file.read()
    file.close()
    return page

while True:
    conn, addr = s.accept() 
    request = conn.recv(25)
    print(request)	
    conn.send("HTTP/1.1 200 ok\n")
    conn.send("Content-type: text /html\n")		
    conn.send("Connection: close\n\n")		
    conn.sendall(web_page())	
    conn.close()
    
