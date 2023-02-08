import socket
from machine import Pin
		
s = socket.socket()
s.bind(('',80))
s.listen(5)
file = open("part1.txt", "r")
part1 = file.read()
file.close()
file = open("part2.txt", "r")
part2 = file.read()
file.close()
file = open("main.py", "r")
main = file.read()
file.close()

while True:
    conn, addr = s.accept() 
    request = conn.recv(2500).decode()
    print(request)
    response="hello world"	
    if "/main" in request:
        response=part1+main+part2
    if "/test" in request:
        tmp=request.split("costycnc",1)[1]
        file = open("main.py", "w")
        file.write(tmp)
        file.close()
        print(tmp)
    if "/ledon" in request:
        led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)
        response=('<p><button onclick="window.location.href ='+"'/ledoff'"+'">OFF</button></p>')
        led.value(0) 
    if "/ledoff" in request:
        led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)
        response=('<p><button onclick="window.location.href ='+"'/ledon'"+'">ON</button></p>')
        led.value(1) 
		
    conn.send("HTTP/1.1 200 ok\n")
    conn.send("Content-type: text /html\n")		
    conn.send("Connection: close\n\n")		
    conn.sendall(response)	
    conn.close()