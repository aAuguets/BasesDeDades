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
    try:
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
    except:
        print "no se ha pogut crear la BBDD "
def _formatMatriculaValid(np):
    """
    Comprova si la matricula te el format correcte (matricula espanyola)
    """
    return len(np)==7 and np[:4].isdigit() and np[4:].isalpha()
def add_car(matricula, posicio, color, marca):
    """
    Afegeix un cotxe amb els atributs de la funcio a la base de dades.
    En caso de que no se pueda añadir no hace nada
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
    En caso muestra que
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
    return False
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
            print "ERROR"
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

def placaLliure():
    """
    Funcio que retorna la primera plaza lliure
    """
    lliures = []
    con = lite.connect('parking.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT placa FROM parking ORDER BY placa ASC")
        rows = cur.fetchall()
        for row in rows:
            lliures.append(row[0])
        for i in range(len(lliures)+1):
            if i not in lliures:
                result= i
                break
    except lite.IntegrityError:
        pass
    con.close()
    return result
def muestra_tabla(taula):
    try:
        conect=lite.connect('parking.db')
        cursor=conect.cursor()
        print "\n\nTaula ",taula
        if taula=='cotxes':
            cursor.execute("SELECT * from {}".format(taula))
            col_names=[cn[0] for cn in cursor.description]
            print "%s \t%-10s \t%s" % (col_names[0],col_names[1],col_names[2])
            rows=cursor.fetchall()
            for row in rows:
                print "%8s \t%-10s \t%s" %row
        else:
            cursor.execute("SELECT * from {} ORDER BY placa ASC".format(taula))
            col_names=[cn[0] for cn in cursor.description]
            rows=cursor.fetchall()
            print "%s \t%-10s \t%s \t\t%s" % (col_names[0],col_names[1],col_names[2],col_names[3])
            for row in rows:
                print "%7s \t%-10s \t%s \t%s" %row
    except:
        print "ERR mostrar tabla"
        pass
    conect.close()
def placesBuides():
    """
    Funcio que retorna la quantitat de places buides.
    El nombre total de places es una variable definida al principi
    """
    con=lite.connect('parking.db')
    cursor=con.cursor()
    cursor.execute("SELECT ({}-count(*)) FROM parking where placa NOT NULL".format(total))
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
        cur.execute("SELECT color FROM cotxes WHERE color=?;",(color,))
        rows=cur.fetchall()
        print rows
        print "Els cotxes amb el color ",color," son: "
        for row in rows:
            print row[0]
    except:
        print "ERROR"
        pass
    con.close()
def buscar_cotxe_marca(marca):
    con=lite.connect('parking.db')
    cur=con.cursor()
    try:
        cur.execute("SELECT id_cotxe FROM cotxes WHERE marca=?;",(marca,))
        rows=cur.fetchall()
        print "Els cotxes amb la marca ",marca," son: "
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
    Funció que mostra les taules que hiha en la base de dades.
    """
    con=lite.connect('parking.db')
    cur=con.cursor()
    cur.execute("SELECT name FROM sqlite_master where type='table'")
    rows= cur.fetchall()
    if len(rows):
        print "\nLes taules que conte  la base de dade son: "
        for row in rows:
            print "\t\t->",row[0]
    else:
        print "\nNo hiha cap taula en la base de dades."
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
        print "\t",d[0], d[1], d[2]
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
def menu():
    print "\n \t\tMENU \n"
    print "\t0. crear PARKING."
    print "\t1. Anadir COCHE."
    print "\t2. Quitar COCHE."
    print "\t3. Plazas dispobibles del parking."
    print "\t4. Consulta el estado de la plaza."
    print "\t5. Consulta la posicion del cotxe per la matricula."
    print "\t6. Consulta vehiculos de un solo color."
    print "\t7. Consulta vehiculos de una sola marca."
    print "\t8. Muestra las tablas de la base de dades"
    print "\t9. Muestra SCHEMA de una tabla"
    print "\t10. Muestra contingut de una taula."
    print "\t11. Muestra info de un coche per la matricula."
    print "\t12. Muestra info de un coche per la posicio que ocupa al parking."
    print "\t13. Exit"
    print
def demana_dades():
    """
    Funció que demana les dades al usuari, en cas de no introduïr la placa se
    se afegeix en la primera plaça lliure.
    """
    matricula=raw_input("Introdueix matricula :")
    if _formatMatriculaValid(matricula):
        placa=raw_input("Introdueix Posicio Al parking:")
        if placa=='':
            placa=placaLliure()
        color=raw_input("Introdueix color del cotxe:")
        marca=raw_input("Introdueix Marca del cotxe:")

    else:
        print "format de la matricula incorrecta"
        return False
    return matricula , placa , marca, color

#infoCotxeMatricula('1111AAA')
#infoCotxePosicio(1)
if __name__ == '__main__':

    print "Benvingut al PARKING"
    menu()
    #fpf=placaLliure()
    opcion=raw_input("option: ")
    while opcion != "11":
        if opcion == "0":
            print "Les dades anteriors se esborraran "
            crear_bd()
            menu()
            opcion=raw_input("option: ")
        elif opcion == "1":
            matricula,placa,marca,color = demana_dades()
            if placa == "":
                placa = placaLliure()
            add_car(matricula,placa,color,marca)
            menu()
            opcion=raw_input("option: ")

        elif opcion == "2":
            matricula=raw_input("Introdueix la matricula del cotxe que vol treure:")
            if _formatMatriculaValid(matricula):
                TempsCotxe(matricula)
                del_car(matricula)
            else:
                print "Format de la matricula Incorrecta"
            menu()
            opcion=raw_input("option: ")
        elif opcion == "3":
			placesBuides()
			menu()
			opcion=raw_input("option: ")
        elif opcion == "4":
            placa = input("plaça? ")
            while (placa > 10) or (placa < 0):
                print "plaça Incorrecta."
                placa = input("plaça? ")
            matriculaAlParking(placa)
            menu()
            opcion=raw_input("option: ")
        elif opcion == "5":
            matricula=raw_input("Introdueix matricula a consultar")
            if _formatMatriculaValid(matricula) :
                posicioAlParking(matricula)
            else:
                print "Format de la matricula incorrecte"
            menu()
            opcion=raw_input("option: ")
        elif opcion == "6" :
            colo=raw_input("Introdueix el color que desitja buscar:")
            buscar_cotxe_color(colo)
            menu()
            opcion = raw_input("option: ")
        elif opcion == "7":
            marca=raw_input("Introdueix la marca que desitja buscar: ")
            buscar_cotxe_marca(marca)
            menu()
            opcion = raw_input("option: ")
        elif opcion == "8":
            mostra_nom_taules()
            menu()
            opcion = raw_input("option: ")
        elif opcion == "9":
            taula=raw_input("Quina Taula vol veure la info (cotxes/parking)?")
            info_table(taula)
            menu()
            opcion = raw_input("option: ")
        elif opcion == "10":
            taula=raw_input("Quina Taula vol veure el contigut (cotxes/parking)?")
            muestra_tabla(taula)
            menu()
            opcion = raw_input("option: ")
        elif opcion == "11":
            matricula=raw_input("Introdueix matricula a consultar")
            if _formatMatriculaValid(matricula):
                infoCotxeMatricula(matricula)
            menu()
            opcion = raw_input("option: ")
        elif opcion == "12":
            posicio=input("Introdueix posicio a consultar: ")
            infoCotxePosicio(posicio)
            menu()
            opcion = raw_input("option: ")
        else:
			print "Wrong option"
			menu()
			opcion=raw_input("option: ")


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
#TempsCotxe("1111AAA")
#matriculaAlParking(2)
#matriculaAlParking(99)
#infoCotxeMatricula("1111AAA")
#infoCotxePosicio(1)
#placesBuides()
#mostra_nom_taules()
#info_table('parking')
#modifica_color_cotxe()
#muestra_tabla('cotxes')
#buscar_cotxe_color('BLAU')
