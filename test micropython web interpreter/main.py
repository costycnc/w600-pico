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
file = open("main1.txt", "r")
main1 = file.read()
file.close()
file = open("main2.txt", "r")
main2 = file.read()
file.close()
file = open("main3.txt", "r")
main3 = file.read()
file.close()

while True:
    conn, addr = s.accept() 
    request = conn.recv(2500).decode()
    print(request)
    response="hello world"	
    if "/main" in request:
        response=part1+main2+part2
    if "/test" in request:
        tmp=request.split("costycnc")[1]
        file = open("main2.txt", "w")
        file.write(tmp)
        file.close()
        file = open("main.py", "w")
        file.write(main1+tmp+main2)
        file.close()
        print(tmp)
    if "/ledon" in request:
        led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)
        led.value(0) 
    if "/ledoff" in request:
        led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)
        led.value(1) 
		
    conn.send("HTTP/1.1 200 ok\n")
    conn.send("Content-type: text /html\n")		
    conn.send("Connection: close\n\n")		
    conn.sendall(response)	
    conn.close()
		
	
