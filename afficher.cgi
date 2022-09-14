#!/usr/bin/python3
import cgi, cgitb
import mariadb
import sys

print ("Content-Type: text/html")
print ("")

print("""<!DOCTYPE html>
<html>
<html>
<meta charset="utf-8">
 <body>""")

cgitb.enable()

input_data = cgi.FieldStorage()


# Connect to MariaDB Platform        
try:
    conn = mariadb.connect(
    user="root",
    password="root",
    host="172.18.0.2",
    database="Music2"
    )
    print("\nConnexion a la base établie \n")
except:
    print(f"Error connecting to MariaDB Platform:")
    sys.exit(1)  


# Get Cursor
try:
    cur = conn.cursor()
 #   print("good")
except:
    print("not ok")

cur.execute("SELECT * FROM playlist;")
for line in cur:
    print(line)
    print("""<br>""")


print(""" <form action="download.cgi" method="get">
  <div>
    <label for="uname">Télécharger une musique: </label>
    <input type="text" id="uname" name="name"
           placeholder="Indiquer le titre et le nom d'artiste">
  </div>
  <div>
    <button>Télecharger</button>
  </div>
</form>
 """)

print(""" <form action="index.cgi" method="POST">
   <button>Retour</button>
  </form>""")

print("""</body></html>""")
