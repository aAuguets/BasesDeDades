# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
from opendata import *

con=lite.connect('accidents.db')
con.text_factory = str

def createDBAccidents():
    try:
        cur=con.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute("DROP TABLE IF EXISTS ACCIDENTS")
        cur.executescript("""
            CREATE TABLE ACCIDENTS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT ,
                EXPEDIENT TEXT,
                NOM_DISTRICTE TEXT,
                NOM_BARRI TEXT,
                NOM_CARRER TEXT,
                DIA_SETMANA TEXT,
                MES TEXT,
                DIA TEXT,
                FRANJA TEXT,
                HORA TEXT,
                TIPO_VEHICLE TEXT,
                SEXE TEXT,
                EDAT INTEGER

            );

        """)
    except lite.Error,e:
        print "eee"
        """
        if con:
            con.rollback()
            print "Errorlaa %s: " % e.args[0]
            sys.exit(1)
            """

def crearDBVehicles():
    """
    """
    try:
        cur=con.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute("DROP TABLE IF EXISTS VEHICLES")
        cur.executescript("""
            CREATE TABLE VEHICLES (
                ID INTEGER PRIMARY KEY AUTOINCREMENT ,
                EXPEDIENT TEXT,
                NOM_DISTRICTE TEXT,
                NOM_BARRI TEXT,
                NOM_CARRER TEXT,
                DIA_SETMANA TEXT,
                MES TEXT,
                DIA TEXT,
                HORA TEXT,
                TIPO_VEHICLE TEXT,
                MARCA TEXT,
                CARNET TEXT,
                ANTIGUITAT INTEGER); """)
    except lite.Error,e:
        print "eee"
        """
        if con:
            con.rollback()
            print "Errorlaa %s: " % e.args[0]
            sys.exit(1)
            """

def crearDBCausalitat():
    try:
        cur=con.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute("DROP TABLE IF EXISTS CAUSALITAT")
        cur.executescript("""
            CREATE TABLE CAUSALITAT(
                ID INTEGER PRIMARY KEY AUTOINCREMENT ,
                EXPEDIENT TEXT,
                CAUSA TEXT); """)
    except lite.Error,e:
        print "eee"
        """
        if con:
            con.rollback()
            print "Errorlaa %s: " % e.args[0]
            sys.exit(1)
            """

def addDataTable(dadesAcc,dadesVehi,dadesCausa):
    with con:
        cur=con.cursor()
        for element in dadesAcc:
            cur.execute("INSERT INTO ACCIDENTS VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?)",tuple(element))
        for element in dadesVehi:
            cur.execute("INSERT INTO VEHICLES VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?)",tuple(element))
        for element in dadesCausa:
            cur.execute("INSERT INTO CAUSALITAT VALUES(NULL,?,?)",tuple(element))
#ID INTEGER AUTOINCREMENT PRIMARY KEY,
createDBAccidents()
crearDBVehicles()
crearDBCausalitat()
dadesA=getDadesAccidents()
dadesV=getDadesVehicles()
dadesCau=getDadesCausalitat()
addDataTable(dadesA,dadesV,dadesCau)
