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

cursor.execute("update puertas set estado='libre'")

cursor.execute("delete from nfc")


con.commit()
con.close()
