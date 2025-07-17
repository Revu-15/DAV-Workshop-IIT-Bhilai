import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('ec2-13-203-231-9.ap-south-1.compute.amazonaws.com', 6970))

# Only use the path after the domain in the GET line
cmd = 'GET / HTTP/1.0\r\nHost: ec2-13-203-231-9.ap-south-1.compute.amazonaws.com\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
