import socket
		
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
    request = conn.recv(25)
    print(request)
    response=main1+main2+main3
    if "/main" in request:
        file = open("main.py", "r")
        main = file.read()
        file.close()
        response=part1+main+part2
    conn.send("HTTP/1.1 200 ok\n")
    conn.send("Content-type: text /html\n")		
    conn.send("Connection: close\n\n")		
    conn.sendall(response)	
    conn.close()
    
