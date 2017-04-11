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
                FOREIGN KEY(id_cotxe) REFERENCES cotxes(id_cotxe) ON DELETE CASCADE);
        """)

crear_bd()
