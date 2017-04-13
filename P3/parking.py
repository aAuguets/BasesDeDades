#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import datetime
total = 10
max = total
l = []
MAX_PLACES=10
def crear_bd():

    global total

    """
    Crea la nostra base de dades desde zero cada cop que es cridada.
    """
    con = lite.connect('parking.db')
    cur = con.cursor()
    cur.executescript("""
        PRAGMA foreign_keys = ON;
        DROP TABLE IF EXISTS cotxes;
        DROP TABLE IF EXISTS parking;

        CREATE TABLE cotxes(
                id_cotxe CHAR(7) PRIMARY KEY,
                color TEXT,
                marca TEXT);

        CREATE TABLE parking(
                id_cotxe CHAR(7) PRIMARY KEY,
                placa INT UNIQUE,
                entrada datetime,
                sortida datetime,
                FOREIGN KEY(id_cotxe) REFERENCES cotxes(id_cotxe) ON DELETE CASCADE);
        """)
    con.commit()
    con.close()

def _formatMatriculaValid(np):
    """
    Comprova si la matricula te el format correcte (matricula espanyola)
    """
    return len(np)==7 and np[:4].isdigit() and np[4:].isalpha()

def add_car(matricula, posicio, color, marca):
    """
    Afegeix un cotxe amb els atributs de la funcio a la base de dades.
    """
    global max
    con = lite.connect('parking.db')
    cur = con.cursor()
    if(_formatMatriculaValid(matricula)):
        if(max!=0):
            try:
                cur.execute("INSERT INTO cotxes(id_cotxe, color, marca) values (?,?,?);", (matricula, color, marca))
                cur.execute("INSERT INTO parking(id_cotxe, placa, entrada) values (?,?, DATETIME('now'));",(matricula, posicio))
                con.commit()
                max -=1
            except lite.IntegrityError:
                print "Error."
        else:
            print"Parking ple. El cotxe",matricula,"no ha pogut entrar."
    else:
        print("Format matricula invalid.")
    con.close()

def posicioAlParking(matricula):
    """
    Retorna a quina posicio es troba dins el parking aquesta matricula.
    """
    if(_formatMatriculaValid(matricula)):
        con = lite.connect('parking.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT placa FROM parking WHERE id_cotxe=?;",(matricula,))
            row = cur.fetchone()
            if row:
                print "El cotxe amb matricula",matricula," es troba a la plaça", row[0]
            else:
                print "El coche amb matricula",matricula,"no es troba al parking"

        except:
            pass
        con.close()
    else:
        print("Format matricula invalid per buscar la seva posicio.")

def matriculaAlParking(placa):
    """
    Retorna quina matricula hi ha al parking en aquesta placa.
    """
    con = lite.connect('parking.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT id_cotxe FROM parking WHERE placa=?;",(placa,))
        row = cur.fetchone()
        if row:
            print "En la Posicio", placa, " hi ha el cotxe amb matricula", row[0]
        else:
            print "La plaça", placa,"esta buida."
    except:
        pass
    con.close()

def infoCotxeMatricula(matricula):
    """
    Retorna tota informacio del cotxe d'aquesta matricula.
    """
    if(_formatMatriculaValid(matricula)):
        con = lite.connect('parking.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM cotxes WHERE id_cotxe=?;",(matricula,))
            row = cur.fetchone()
            if row:
                print "El cotxe amb matricula",matricula," te aquesta informació:\n","\tMatr.: %s\n\tColor: %s\n\tMarca: %s" % (row[0], row[1], row[2])
            else:
                print "El coche amb matricula: ",matricula," no es troba dintre del Parking"
        except:
            pass
        con.close()
    else:
        print("Format matricula invalid per buscar la seva informació.")

def infoCotxePosicio(placa):
    """
    Retorna info del cotxe que ocupa la plaça.
    """
    con = lite.connect('parking.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM cotxes WHERE id_cotxe in (SELECT id_cotxe FROM parking WHERE placa=?);",(placa,))
        row = cur.fetchone()
        if row:
            print "El cotxe a la placa ",placa," te aquesta informació:\n","\tMatr.: %s\n\tColor: %s\n\tMarca: %s" % (row[0], row[1], row[2])
        else:
            print "La plaça", placa,"esta buida."
    except:
        pass
    con.close()

def del_car(matricula):
    """
    Afegeix un cotxe amb els atributs de la funcio a la base de dades.
    """
    global max
    con = lite.connect('parking.db')
    cur = con.cursor()
    if(_formatMatriculaValid(matricula)):
            try:
                cur.execute("DELETE FROM cotxes WHERE id_cotxe=?",(matricula,))
                cur.execute("DELETE FROM parking WHERE id_cotxe=?",(matricula,))
                con.commit()
                max +=1
            except lite.IntegrityError:
                print "Error.lelele"
    else:
        print("Format matricula invalid.")
    con.close()

def totalPlacesLliures():
    global max
    print max

def placaLliure():
    lliures = []
    con = lite.connect('parking.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT placa FROM parking")
        rows = cur.fetchall()
        for row in rows:
            lliures.append(row[0])
        for i in l:
            if i not in lliures:
                print i
    except lite.IntegrityError:
        pass
    con.close()

def muestra_tabla(taula):
    try:
        conect=lite.connect('parking.db')
        cursor=conect.cursor()
        print "\n\nTaula ",taula
        cursor.execute("SELECT * from {}".format(taula))
        col_names=[cn[0] for cn in cursor.description]
        #print col_names
        rows=cursor.fetchall()
        if len(col_names)==3:
        #print rows
            print "%s \t%-10s \t%s" % (col_names[0],col_names[1],col_names[2])
            for row in rows:
                print "%8s \t%-10s \t%s" %row
        elif len(col_names)==4:
            print "%s \t%-10s \t%s \t\t%s" % (col_names[0],col_names[1],col_names[2],col_names[3])
            for row in rows:
                print "%7s \t%-10s \t%s \t%s" %row
        conect.close()
        print
    except:
        print "ERR mostrar tabla"

def placesBuides():
    """
    Funcio que retorna la quantitat de places buides.
    El nombre total de places es una variable definida al principi
    """
    con=lite.connect('parking.db')
    cursor=con.cursor()
    cursor.execute("SELECT (10-count(*)) FROM parking where placa NOT NULL")
    row=cursor.fetchone()
    if row:
        print "El nombre de places disponibles es:",row[0]
    con.close()

def buscar_cotxe_color(color):
    """
    Funcio que retorna tots els cotxes amb el color=?,'color'
    """
    con=lite.connect('parking.db')
    cur=con.cursor()
    try:
        cur.execute("SELECT id_cotxe FROM cotxes WHERE color=?;",(color,))
        rows=cur.fetchall()
        print "Els cotxes amb el color ",color," son: "
        for row in rows:
            print row[0]
    except:
        print "ERROR"
        pass
    con.close()
def TempsCotxe(matricula):
    """
    Funcion que mostra el temps que porta el cotxe al parking i quan
    ha de pagar abans de marxar.
    """
    con=lite.connect('parking.db')
    cursor=con.cursor()
    try:
        cursor.execute("SELECT (strftime('%s',DATETIME('now'))-strftime('%s',entrada))/60 from parking where id_cotxe=?",(matricula,))
        row=cursor.fetchone()

        if row:
            if row[0] < 60:
                print "El coche amb matricula",matricula," porta", row[0],"minuts"
                print "en total ha de pagar",row[0]*0.5,"€"
            elif 60 < row[0]<3600:
                print "El coche amb matricula",matricula," porta", float(row[0]/60),"Horas"
            else:
                print "El coche amb matricula",maricula ,"Porta ",row[0],
    except:
        print "EEROR NO"
    con.close()

def mostra_nom_taules():
    """
    """
    con=lite.connect('parking.db')
    cur=con.cursor()
    cur.execute("SELECT name FROM sqlite_master where type='table'")
    rows= cur.fetchall()
    print "Les taules que conte  la base de dade son: "
    for row in rows:
        print row[0]
    con.close()

def info_table(table):
    """
    Funcion que mostra la informacio PRAGMA de la taula que se le pasa como
    parametro
    """
    print "\nSCHEMA de la taula ",table, "es: "
    con=lite.connect('parking.db')
    cur=con.cursor()
    cur.execute("PRAGMA table_info({});".format(table))
    data = cur.fetchall()
    for d in data:
        print d[0], d[1], d[2]
    con.close()

def modifica_color_cotxe():
    """
    Funcion que modifica el color del coche que se le pasa como parametro.
    """
    try:
        con=lite.connect('parking.db')
        cur=con.cursor()
        matricula=raw_input("Introduce matricula del cotxe que es vol canviar el color: ")
        if (_formatMatriculaValid(matricula)):
            new_color=raw_input("Nou color del cotxe: ")
            cur.execute("UPDATE cotxes SET color=? WHERE id_cotxe=?" ,(new_color,matricula,))
            con.commit()
            print "Number of rows updated: %d" % cur.rowcount
        else:
            print "Matricula introduia incorrectament"
    except:
        print("EERROR")
        pass
    con.close()


#TESTS d'execucio.
#crear_bd()
#add_car("9999AAA", 1, "BLAU", "DEP")
#add_car("1111AAA", 2, "BLAU", "DEP")
#add_car("1112AAA", 3, "BLAU", "DEP")
#add_car("2222AAA", 4, "BLAU", "DEP")
#add_car("3333AAA", 5, "BLAU", "DEP")
#add_car("4444EEE", 6, "BLAU", "DEP")
#add_car("1234AAA", 7, "BLAU", "DEP")
#add_car("4444AAA", 8, "BLAU", "DEP")
#add_car("5555AAA", 9, "BLAU", "DEP")
#add_car("6666AAA", 10, "BLAU", "DEP")
#muestra_tabla()
#del_car("9999AAA")
#add_car("7777AAA", 1, "BLAU", "DEP")
#add_car("8888EEE", , "BLAU", "DEP")
#posicioAlParking("9999AAA")
#posicioAlParking("1111AAA")
TempsCotxe("1111AAA")
#matriculaAlParking(2)
#matriculaAlParking(99)
infoCotxeMatricula("1111AAA")
#infoCotxePosicio(1)
#placesBuides()
#mostra_nom_taules()
#info_table('parking')
#modifica_color_cotxe()
muestra_tabla('cotxes')
buscar_cotxe_color('BLAU')
