#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from html import escape

with open('data.txt', 'r') as file:
text = file.read()
print("<h2>С экранированием: %s</h2>" % escape(text))    
print("<h2>Без экранирования: %s</h2>" % text)