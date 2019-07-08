#!/usr/bin/env python3

import RPi.GPIO as GPIO
import mysql.connector
import MySQLdb
import time
from mfrc522 import SimpleMFRC522
from random import choice

cerradura="vacio"
reader = SimpleMFRC522()
longitud = 18
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
text = ""
text = text.join([choice(valores) for i in range(longitud)])

	#ABRIR LA PUERTA Y GUARDAR EL NUMERO DE PUERTA ASIGNADA

try:
	reader.write(text)
	print('<div class="container"><div class="row"><div class="jumbotron"><h1 align="center">Ya puede retirar el NFC</h1></div></div>')
finally:
	GPIO.cleanup()

con = mysql.connector.connect(host="localhost",
                     user="pepe",
                     passwd="pepemolinero",
                     db="kiosko")

cursor = con.cursor()

cursor.execute("select * from puertas where estado='libre'")
resultado=cursor.fetchall()

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

if(len(resultado)==0):
	print('<div class="container"><div class="modal-body">Lo sentimos, no quedan puertas libres</div></div>')
	GPIO.output(26,GPIO.HIGH)
	time.sleep(0.2);
	GPIO.output(26,GPIO.LOW)
	time.sleep(0.2);
	GPIO.output(26,GPIO.HIGH)
	time.sleep(0.2);
	GPIO.output(26,GPIO.LOW)
	time.sleep(0.2);
	GPIO.output(26,GPIO.HIGH)
	time.sleep(0.2);
	GPIO.output(26,GPIO.LOW)
	time.sleep(0.2);
else:
	for registro in resultado:
		cerradura=(registro[2])
		puerta=(str(registro[0]))

exe1=("insert into nfc (puerta,pass) values ("+puerta+",")
exe=(exe1+'"'+text+'")')
cursor.execute(exe)
cursor.execute("update puertas set estado='ocupado' where id="+puerta)

con.commit()
con.close()

if(cerradura!="vacio"):
        cerradura=(int(cerradura))
        GPIO.setup(cerradura,GPIO.OUT)
        GPIO.output(cerradura,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
        time.sleep(1);
        GPIO.output(cerradura,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        time.sleep(1);
        GPIO.cleanup()

print("<div class='container'><div class='modal-body'>Muchas gracias por confiar en Grupo EOS Iberica</div></div>")
