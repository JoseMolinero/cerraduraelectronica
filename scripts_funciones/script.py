#!/usr/bin/env python3

import mysql.connector
import MySQLdb

con = mysql.connector.connect(host="localhost",
                     user="pepe",
                     passwd="pepemolinero",
                     db="kiosko")

cursor = con.cursor()

cursor.execute("select puerta from nfc where unix_timestamp(fecha)<(unix_timestamp()-1*3600);")
resultado=cursor.fetchall()
max=(len(resultado))
cont=0


if(len(resultado)==0):
	print("na")
else:
	while cont!=max:
		puerta=(str(resultado[cont])[10:11])
		exe=("update puertas set estado='libre' where id="+puerta+";")
		print(puerta)
		print(exe)
		cursor.execute(exe)
		eje=("delete from nfc where puerta=")
		eje+=puerta
		print(eje)
		cursor.execute(eje)
		cont=cont+1

con.commit()
cursor.close()
con.close()
