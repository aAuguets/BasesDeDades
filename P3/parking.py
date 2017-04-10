#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import datetime

def crear_bd():
     db = lite.connect('parking.db')
     cursor= db.cursor()
     
     # definimos nuestra base de datos(los campos)
     cursor.executescript("""
     DROP TABLE IF EXISTS PK;
     CREATE TABLE PK(
     PLACE INTEGER UNIQUE NOT NULL,
     NP CHAR(7) PRIMARY KEY,
     COLOR CHAR(7),

     BRAND CHAR (10),
     DATA CHAR(19)
     ); """)
     #actualizo la base de datos
     db.commit()
     db.close()

def menu():
    """
    """
    print "0. Crear Base de datos."
    print "1. Anadir COCHE."
    print "2. Quitar COCHE."
    print "3. Plazas dispobibles."
    print "4. Comprueba Estado de la plaza."
    print "5. Comprueba vehiculo."
    print "6. Vehiculos de un solo color."
    print "7. Vehiculos de una sola marca."
    print "8. Retorna segundos que un coche lleva en el parking."
    print "9. Retorna Dias que coche lleva en un parking."
    print "10. Cost de un coche dins parking."
    print "8. Help."
    print "9. Exit"
    
    
def add_elementos():

    con=lite.connect('parking.db')
    cursor=con.cursor()
    cursor.executescript("""
    INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) VALUES (23 , '1234ASD', 'Red','Opel', strftime('%s', 'now'));
    INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) VALUES (0 , '1234ASQ', 'Red', 'Ferrari', strftime('%s','now'));
    INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) VALUES (2 , '1234ASE', 'Blue', 'Tata', strftime('%s','now'));
    INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) VALUES (3 , '1234ASU', 'Blue', 'Toyota', strftime('%s','now'));
    INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) VALUES (1 , '1234ASI', 'Black', 'Opel', strftime('%s','now'));
    INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) VALUES (6 , '1234ASK', 'White', 'Renault', strftime('%s','now'));
    INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) VALUES (25 , '1234ASL', 'White', 'Honda', strftime('%s','now'));
    INSERT INTO PK (PLACE,NP,COLOR,BRAND, DATA) VALUES (22 , '1234ASB', 'Blue', 'Honda', strftime('%s','now'));
    """)
    
def add_car():
    """
    """
    try:
        conect=lite.connect('parking.db')
        cursor=conect.cursor()
        plaza=5
        matricula= "pla56324"#raw_input("matricula")
        color="rojo"#raw_input("color?")
        marca="fiat"#raw_input("marca?")
        hora="lala"
        cursor.execute('''
        INSERT INTO PK(PLACE,NP,COLOR,BRAND,DATA)
        VALUES(?,?,?,?,?)''',(plaza,matricula,color,marca,hora))
        conect.commit()
        conect.close()
    except:
        print "ERROR 1"
        

def del_car():
    try:
        conect=lite.connect('parking.db')
        cursor=conect.cursor()
        plaza=1
        cursor.execute('''DELETE FROM PK WHERE PLACE = ? ''',(plaza,))
        conect.commit()
        conect.close()
                      
    except:
        print "ERR del" 
    

def muestra_tabla():
    try:
        conect=lite.connect('parking.db')
        cursor=conect.cursor()
        for row in cursor.execute('SELECT * from PK'):
            print('{0}:{1}:{2}:{3}:{4}'.format(row[0],row[1],row[2],row[3],row[4])) 
        conect.close()
    except:
        print "ERR mostrar tabla"


def plazas_vacias():
     """
     """
     con=lite.connect('parking.db')
     cursor=con.cursor()
     cursor.execute('SELECT (30-count(*)) FROM PK where place NOT NULL')
     for i in cursor:
          print i[0]
     con.close()

def precio_cotxe():
     """
     """
     con=lite.connect('parking.db')
     cursor=con.cursor()
     cursor.execute('SELECT ((sfrftime('%s','now')-DATA)/60) from PK')
     for i in cursor:
          print i
     con.close()
     
if __name__=='__main__':
     menu()
     opcio=raw_input("Introduce una opcion")
     while opcio != '9':
          if opcio=="0":
               crear_bd()
               menu()
               opcio=raw_input("Introduce una opcion")
          elif opcio=="1":
               add_elementos()
               menu()
               opcio=raw_input("Introduce una opcion")
          elif opcio=="2":
               add_car()
               menu()
               opcio=raw_input("Introduce una opcion")
          elif opcio=="3":
               print "añade"
               muestra_tabla()
               menu()
               opcio=raw_input("Introduce una opcion")
          elif opcio=="4":
               del_car()
               menu()
               opcio=raw_input("Introduce una opcion")
          elif opcio=="5":
               print "las plazas vacias son: "
               plazas_vacias()
          
               menu()
               opcio=raw_input("Introduce una opcion")
          else:
               print "WRONG OPTION"
               menu()
               opcio=raw_input("Introduce una opcion")
    
     
        


