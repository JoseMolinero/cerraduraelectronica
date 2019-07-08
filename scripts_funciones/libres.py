#!/usr/bin/env python3

import RPi.GPIO as GPIO
import mysql.connector
import MySQLdb
from mfrc522 import SimpleMFRC522
from random import choice

con = mysql.connector.connect(host="localhost",
                     user="pepe",
                     passwd="pepemolinero",
                     db="kiosko")

cursor = con.cursor()

cursor.execute("select * from puertas where estado='libre'")
resultado=cursor.fetchall()

if(len(resultado)==0):
	print("No queda ninguna puerta libre")
else:
	for registro in resultado:
		print(registro[0])


con.commit()
con.close()
