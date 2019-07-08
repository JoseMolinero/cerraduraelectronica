#!/usr/bin/env python3

import RPi.GPIO as GPIO
import mysql.connector
import MySQLdb
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print('<div class="container"><div class="row"><div class="jumbotron"><h1 align="center">Ya puede retirar el NFC</h1></div></div>')
finally:
        GPIO.cleanup()

con = mysql.connector.connect(host="localhost",
                     user="pepe",
                     passwd="pepemolinero",
                     db="kiosko")

cursor = con.cursor()

exe="select puerta from nfc where pass="
exe1=('"'+text+'"')
exe2=(exe+exe1)
cursor.execute(exe2)
query=cursor.fetchall()

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

if(len(query)==0):
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
	print('<div class="container"><div class="modal-body">No tiene ninguna puerta asignada</div></div>')
else:
	for num in query:
		print('<div class="container"><div class="modal-body">Recoja sus pertenencias en la puerta '+str(num[0])+'<br>Gracias por confiar en Grupo EOS Iberica</div></div>')
		puerta=num[0]

puerta=str(puerta)
cerra=("select cerradura from puertas where id="+puerta)
cursor.execute(cerra)
consulta=cursor.fetchall()

for cer in consulta:
	cerradura=(int(cer[0]))
	GPIO.setup(cerradura,GPIO.OUT)
	GPIO.output(cerradura,GPIO.HIGH)
	GPIO.output(26,GPIO.HIGH)
	time.sleep(1);
	GPIO.output(cerradura,GPIO.LOW)
	GPIO.output(26,GPIO.LOW)
	time.sleep(1);
	GPIO.cleanup()

borrar='delete from nfc where pass='
borrar1=(borrar+exe1)
print('Clave borrada')
cursor.execute(borrar1)
cursor.execute('update puertas set estado="libre" where id='+str(num[0]))

con.commit()
con.close()
