#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text = form.getfirst("text", "no")

f = open('data.txt', 'w')
f.write(text)
f.close()
print("Content-type: text/html\n")
print("Good")
