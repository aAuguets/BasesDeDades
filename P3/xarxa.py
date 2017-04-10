#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
def menu():
    """
    """
    print "1. Anadir COCHE."
    print "2. Quitar COCHE."
    print "3. Plazas dispobibles."
    print "4. Comprueba Estado de la plaza."
    print "5. Comprueba vehiculo."
    print "6. Vehiculos de un solo color."
    print "7. Vehiculos de una sola marca."
    print "8. Help."
    print "9. Exit"

def add_car():
    """
    """
    try:
        guardar_dades(demana_place(),demana_matri(),demana_color(),demana_brand(),data())
    except:
        "ERROR"
        return 0
def del_car():
    print "que coche quiere quitar (P/N)?"

try:
    #creamos una basse de datos
    db = lite.connect('xarxa.db')
    cursor= db.cursor()
    cursor.execute()
