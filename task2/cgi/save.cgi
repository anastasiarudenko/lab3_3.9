#!/usr/bin/python3

import cgi, cgitb 

form = cgi.FieldStorage() 
text = form.getvalue('text')

with open('data.txt', 'w') as file:
    file.write(text)
print("Good")