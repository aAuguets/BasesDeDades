import struct 

format = '7s10s11s'
places = 10
data_size = struct.calcsize(format)
def _creaBD(places):
	f=open('places2.dat','w+')
	for i in range(places):
		prepara = struct.pack(format, 'XXXXXXX','XXXXXXXXXX','XXXXXXXXXX')
		f.seek(i*data_size)
		f.write(prepara)
	f.close()

def _guardaDades(posicio_punter, matricula, color, marca):
	f=open('places2.dat','w+')
	dades_encapsulades = struct.pack(format, matricula, color, marca)
	f.seek(0*data_size)
	f.write(dades_encapsulades)
	f.close()

def _llegeixDades(posicio_punter):
	f=open('places2.dat','r')
	f.seek(posicio_punter*data_size)
	dades = f.read(data_size)
	return struct.unpack(format, dades) #retorna una tupla

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

# def main():
# 	menu()
# 	opcion=raw_input("opcion: ")
# 	while opcion != "6":
#     	if opcion=="0":
#         	confirmar = raw_input("Estas seguro? y/N: ")
#         	if confirmar == "y":
#             	crear_bd()
#             	print "Base de dadas creada. Plazas vacias"
#         	else:
#             	print "Base de dadas nueva No creada."
#         	menu()
#         	opcion=raw_input("opcion: ")
#     	elif opcion=="1":
#         	add_car()
#         	menu()
#         	opcion=raw_input("opcion: ")
#     	elif opcion=="2":
#         	delete_car()
#         	menu()
#         	opcion=raw_input("opcion: ")
#     	elif opcion=="3":
#         	print ls_emptyPlace()
#         	menu()
#        	 	opcion=raw_input("opcion: ")
#     	elif opcion=="4":
#         	estatePlace()
#         	menu()
#         	opcion=raw_input("opcion: ")
#     	elif opcion=="5":
#         	matricula=raw_input("Que matricula quiere comprobar?:")
#         	if comprueba(matricula):
#         	    print "El coche esta dentro del parking, esta en la posicion "+str(comprueba(matricula))
#         	else:
#         	    print "No esta dentro del parking"
#         	menu()
#         	opcion=raw_input("opcion: ")
#     	else:
#         	print "Opcion incorrecta"
#         	menu()
#         	opcion=raw_input("opcion: ")

_creaBD()
_guardaDades(0,'1234qwe','red','dep')
print _llegeixDades(1)

# data_size=struct.calcsize(format)
#f=open('places2.dat','w+')
# f.seek(0*data_size)
# t=struct.pack(format, '3333ABC', 'Orange', 'Jokese')
# f.write(t)
# t=struct.pack(format, '3333JJJ', 'Ora', 'aassasd')
#f.write(t)
"""f.seek(0*data_size)
print "1"
s=f.read(data_size)
r=struct.unpack(format, s)
print "r"
print r"""

# for e in r:
# 	e.strip()
# 	print "e"
# 	print e
