#!/usr/bin/python3
import cgi, cgitb

print("Content-Type: text/html")
print(" ")

print("""<!DOCTYPE html>
<html>
<html>
<meta charset="utf-8">
 <body>""")

cgitb.enable()

form=cgi.FieldStorage()

link=form.getValue('name')

print(link)

print("""</body></html>""")

