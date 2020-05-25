#!/usr/bin/python3

with open('data.txt', 'r') as file:
    file.read(text)

print("Content-type:text/html\r\n\r\n")
print("<h1>%s</h1>" % )