import urllib.request

fhand = urllib.request.urlopen('http://textfiles.com/stories/antcrick.txt')

for line in fhand:
    print(line.decode().strip())
