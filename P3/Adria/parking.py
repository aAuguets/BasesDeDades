#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import datetime

def crear_bd():
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


def add_car(matricula, posicio, color, marca):
    """
    Afegeix un cotxe amb els atributs de la funcio a la base de dades.
    """
    con = lite.connect('parking.db')
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO cotxes(id_cotxe, color, marca) values (?,?,?);", (matricula, color, marca))
        cur.execute("INSERT INTO parking(id_cotxe, placa, entrada) values (?,?, DATETIME('now'));",(matricula, posicio))
        con.commit()
    except lite.IntegrityError:
        print "error"
    con.close()

#TESTS d'execucio.
crear_bd()
add_car("9999AAA", 1, "BLAU", "DEP")
