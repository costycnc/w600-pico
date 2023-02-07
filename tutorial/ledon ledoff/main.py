import socket
from machine import Pin
		
s = socket.socket()
s.bind(('',80))
s.listen(5)

while True:
    conn, addr = s.accept() 
    request = conn.recv(1024)	
    if "/ledon" in request:
        led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)
        led.value(0) 
    if "/ledoff" in request:
        led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)
        led.value(1) 							
    conn.send("HTTP/1.1 200 ok\n")
    conn.send("Content-type: text /html\n")		
    conn.send("Connection: close\n\n")		
    conn.sendall("hello")	
    conn.close()
    
