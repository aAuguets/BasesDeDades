#!/usr/bin/python

num_final=10
ERR = -1

       
def _check_numberPlate(np):
    """
    Check Number Plate
    ------------------
    La funcio retorna True o False depenent si la matricula del cotxe es correcte.
    Donem per suposat que totes les matricules del planeta son de 4 digits seguit de 3 lletres.
    """
    return len(np)==7 and np[:4].isdigit() and np[4:].isalpha()

def _feplace():
    """
    Find Empty place
    ----------------
    La funcio busca un aparcament lliure i retorna el numero de la placa que ha trobat.
    """
    filein=open('places.dat',"r")
    plaza=0
    for i in range(num_final):
        filein.seek(i*7)
        linea=filein.readline(7)
        if linea =="XXXXXXX":
            filein.close()
            return plaza
        else:
            plaza+=1
    filein.close()
    return ERR
            
def crear_bd():
    """
    Crear Base de Dades
    -------------------
    La funcio crea una nova Base de Dades d'aparcaments. El nou fitxer 'places.dat' consta de 100 aparcaments buits.
    """
    filein=open('places.dat',"w")
    for plazas in range(num_final):
        filein.write("XXXXXXX")
    filein.close()

def add_car():
    """
    Add Car
    -------
    La funcio afegeix un cotxe a la base de dades. Aquesta funcio demana una placa on s'esta aparcant i la matricula.
    En cas que no s'introdueixi placa d'aparcament, aquest cotxe s'aparcara a la primera placa buida.
    """
    filein=open('places.dat',"r+")
    pos=_feplace()
    if pos == ERR:
        print "El parking esta lleno."
        return -1
    else:
        plaza=raw_input("plaza ?:")
        if plaza == '' or _check_plaza(plaza):
            matricula=raw_input("matricula ?:")
            if _check_numberPlate(matricula):
                if comprueba(matricula)==False:
                    if plaza == '':
                        filein.seek(pos*7)
                    else:
                        filein.seek(7*(int(plaza)))
                    filein.write(matricula)
                    print "Coche introducido corectamente"
                else:
                    print "El coche ya esta en el parking"
            else:
                print "Matricula erronia."
        else:
            print "Plaza incorrecta"
    filein.close()
    return 0

def delete_car():
    """
    Delete Car
    ----------
    Aquesta funcio elimina un cotxe de la Base de Dades, deixant la placa buida.
    """
    filein=open('places.dat',"r+")
    opcion=raw_input("Eliminar por plaza o matricula? (P/M)")
    if opcion in "PM":
    #while opcion == "P" or opcion == "M":
        if opcion=="P":
            plaza=raw_input("plaza?")
            if _check_plaza(plaza):
                filein.seek(7*int(plaza))
                filein.write("XXXXXXX")
            else:
                print "Plaza incorecta"
    
        elif opcion=="M":
            matricula=raw_input("matricula?")
            if _check_numberPlate(matricula):
                for i in range(num_final):
                    filein.seek(i*7)
                    if filein.readline(7)==matricula:
                        filein.write("XXXXXXX")
            else:
                print "matricula incorrecta"
    
    filein.close()


def estatePlace():
    plaza=input("plaza a comprobar?")
    filein=open('places.dat','r')
    filein.seek(plaza*7)
    if filein.readline(7)=="XXXXXXX":
        print "Place EMPTY"
    else:
        print "Place FULLY"

    filein.close()
    

def _show_eplaces():
    """
    Show Empty places
    -----------------
    La funcio llista totes les places lliures.
    """
    filein=open('places.dat',"r")
    List = []
    for i in range(num_final):
        filein.seek(i*7)
        if filein.readline(7) =="XXXXXXX":
            List+=[i]
    filein.close()
    return List

def ls_emptyPlace():
    """
    List Empty Place
    ----------------
    La funcio retorna el nombre de places lliures.
    """
    return len(_show_eplaces())

def comprueba(matricula):
    """
    Comprueba Matricula
    -------------------
    Funcion que Retorna True si la matricula ya esta en el parking,
    en caso contrario retorna False. 
    
    """
    filein=open('places.dat','r')
    for i in range(num_final):
        filein.seek(i*7)
        if filein.readline(7) == matricula:
            #print "Se encuentra en la plaza"+ str(i)
            filein.close()
            return i
    filein.close()
    return False
           

    
def menu():
    """
    Funcio que te com a proposit printar el menu.
    """
    print "\n MENU \n"
    print "0. crear PARKING"
    print "1. Anadir COCHE"
    print "2. Quitar COCHE"
    print "3. Plazas dispobibles"
    print "4. Comprueba Estado de la plaza"
    print "5. Comprueba vehiculo"
    print "6. Salir"
    
def _check_plaza(place):
    """
    Comprueba Plaza
    ---------------
    Funcion que retorna True si es una plaza correcta o False si es incorecta
    """
    return len(place) <= 3 and int(place) < num_final and place.isdigit()



menu()
opcion=raw_input("opcion: ")
while opcion != "6":
    if opcion=="0":
        confirmar = raw_input("Estas seguro? y/N: ")
        if confirmar == "y":
            crear_bd()
            print "Base de dadas creada. Plazas vacias"
        else:
            print "Base de dadas nueva No creada."
        menu()
        opcion=raw_input("opcion: ")
    elif opcion=="1":
        add_car()
        menu()
        opcion=raw_input("opcion: ")
    elif opcion=="2":
        delete_car()
        menu()
        opcion=raw_input("opcion: ")
    elif opcion=="3":
        print ls_emptyPlace()
        menu()
        opcion=raw_input("opcion: ")
    elif opcion=="4":
        estatePlace()
        menu()
        opcion=raw_input("opcion: ")
    elif opcion=="5":
        matricula=raw_input("Que matricula quiere comprobar?:")
        if comprueba(matricula):
            print "El coche esta dentro del parking, esta en la posicion "+str(comprueba(matricula))
        else:
            print "No esta dentro del parking"
        menu()
        opcion=raw_input("opcion: ")
    else:
        print "Opcion incorrecta"
        menu()
        opcion=raw_input("opcion: ")
