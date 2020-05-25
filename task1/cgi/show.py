#!/usr/bin/env python3
import cgi
import html

f = open('data.txt', 'r')
text = f.read()
f.close()
print("Content-type:text/html\r\n\r\n")
print("<h2>With escaping: %s</h2>" % html.escape(text))
print("<h2>Without escaping: %s</h2>" % text)
