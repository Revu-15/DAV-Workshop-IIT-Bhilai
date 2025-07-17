import urllib.request

fhand = urllib.request.urlopen('http://icio.us/')

for line in fhand:
    print(line.decode().strip())
