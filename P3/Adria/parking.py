#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import datetime

def crear_bd():
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
                placa INT,
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
    con = lite.connect('parking.db')
    cur = con.cursor()
    if(_formatMatriculaValid(matricula)):
        try:
            cur.execute("INSERT INTO cotxes(id_cotxe, color, marca) values (?,?,?);", (matricula, color, marca))
            cur.execute("INSERT INTO parking(id_cotxe, placa, entrada) values (?,?, DATETIME('now'));",(matricula, posicio))
            con.commit()
        except lite.IntegrityError:
            print "Error. <Ja dins.>"
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
            print "El cotxe amb matricula",matricula," es troba a la plaça", row[0]
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
            print "El cotxe amb matricula",matricula," te aquesta informació:\n","\tMatr.: %s\n\tColor: %s\n\tMarca: %s" % (row[0], row[1], row[2])
        except:
            pass
        con.close()
    else:
        print("Format matricula invalid per buscar la seva informació.")

#TESTS d'execucio.
#crear_bd()
add_car("9999AAA", 1, "BLAU", "DEP")
add_car("1111AAA", 2, "BLAU", "DEP")
add_car("11111EE", 3, "BLAU", "DEP")
posicioAlParking("9999AAA")
matriculaAlParking(2)
matriculaAlParking(99)
infoCotxeMatricula("9999AAA")
