#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


def crear_bd():
    """
    Crear la nostra base de dades
    """
    try:
        con=lite.connect('practica3.db')
        cur=con.cursor()
        cur.executescript("""
            PRAGMA foreign_keys = ON;
            DROP TABLE IF EXISTS CLIENTS;
            DROP TABLE IF EXISTS CENTRES;
            DROP TABLE IF EXISTS COMANDES;
            DROP TABLE IF EXISTS VENEDORS;
            DROP TABLE IF EXISTS PRODUCTES;

            CREATE TABLE CLIENTS(
                NIF PRIMARY KEY,
                RAOSOCIAL,
                ADREÇA,
                TELEFON,
                DESCOMPTE,
            );
            CREATE TABLE CENTRES(
                CODI PRIMARY KEY,
                CIUTAT,
                ZONA,
                );
            CREATE TABLE COMANDES(
                NUMCOMANDA PRIMARY KEY,
                CODIPRODUCTE ,
                CODIVENEDOR,
                NIF,
                DATA,
                UNITATS,
            );
            CREATE TABLE VENEDORS(
                CODI PRIMARY KEY,
                NOM ,
                EDAT ,
                CODICENTRE ,
            );
            CREATE TABLE PRODUCTES(
                CODI PRIMARY KEY,
                DESCRIP ,
                PREU ,
                ESTOC ,
            );
        """)
        con.commit()
        con.close()
        return True
    except:
        print "ERROR Crear"
        return False


def EliminaProducto(producto):
    """
    Funcio que elimina el producte de la taula de productes
    """
    i=False
    try:
        con=lite.connect('practica3.db')
        cur=con.cursor()
        cur.execute("DELETE FROM PRODUCTES WHERE CODI=?",(producto,))
        con.commit()
        i=True
    except:
        print "ERROR DELETE"
    con.close()
    return i

def Product_Sense_Stock():
    """
    Funcio que retorna una lista on cada element es un producte sense stock.
    """
    lista=[]
    try:
        con=lite.connect('practica3.db')
        cur=con.cursor()
        cur.execute("SELECT CODI FROM PRODUCTES WHERE ESTOC=0")
        rows=cur.fetchall()
        for row in rows:
            lista.append(row[0])
    except:
        print "ERROR Product_Sense_Stock"
    con.close()
    return lista


def ModificaBonificacio():
    """
    Funcio que modifica els tres primers clients de la base de dades,
    que rebran una bonificacio de l 1,5%  en les seves compres.
    """
    i=False
    try:
        con=lite.connect('practica3')
        cur=con.cursor()
        cur.execute("SELECT NIF FROM CLIENTS LIMIT 3")
        rows=cur.fetchall()
        for row in rows:
            cur.execute("UPDATE CLIENTS SET DESCOMPTE WHERE NIF=?"(row[0]))
        con.commit()
        i=True
    except:
        print "ERROR ModificaBonificacio"

    con.close()
    return i
