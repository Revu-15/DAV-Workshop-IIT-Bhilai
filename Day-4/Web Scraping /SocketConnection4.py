import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.faqs.org', 80))

# Using HTTP/1.1 and including the required Host and Connection headers
cmd = 'GET /rfcs/rfc2616.html HTTP/1.1\r\nHost: www.faqs.org\r\nConnection: close\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
