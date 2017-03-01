import struct 

format = '7s6s11s'
places = 100
data_size = struct.calcsize(format)
color_list = ["Red", "Green", "Yellow", "Black", "White", "Silver", "Orange", "Blue", "Grey", "Brown", "Beige"]
def _creaBD():
	f=open('places2.dat','w')
	for i in range(places):
		prepara = struct.pack(format, 'XXXXXXX','XXXXXX','XXXXXXXXXX')
		f.seek(i*data_size)
		f.write(prepara)
	f.close()

def _guardaDades(posicio_punter, matricula, color, marca):
	if posicio_punter == -1 or matricula == -1 or color == -1:
		print "ERR"
		return -1
	f=open('places2.dat','r+')
	dades_encapsulades = struct.pack(format, matricula, color, marca)
	f.seek(posicio_punter*data_size)
	f.write(dades_encapsulades)
	f.close()

def _llegeixDades(posicio_punter):
	f=open('places2.dat','r')
	f.seek(posicio_punter*data_size)
	dades = f.read(data_size)
	f.close()
	return struct.unpack(format, dades) #retorna una tupla

def _feplace():
    """
    Find Empty place
    ----------------
    La funcio busca un aparcament lliure i retorna el numero de la placa que ha trobat.
    """
    f=open('places2.dat',"r")
    for i in range(places):
    	f.seek(i*data_size)
    	if f.read(1) == "X":
    		f.close()
    		return i 
    f.close()
    return -1

def _check_numberPlate(np):
    """
    Check Number Plate
    ------------------
    La funcio retorna True o False depenent si la matricula del cotxe es correcte.
    Donem per suposat que totes les matricules del planeta son de 4 digits seguit de 3 lletres.
    """
    return len(np)==7 and np[:4].isdigit() and np[4:].isalpha()

def _demanaMatricula():
	matricula =  raw_input("Number plate (?): ")
	if _check_numberPlate(matricula):
		return matricula
	else:
		return -1

def _demanaColor():
	color = raw_input("Car Color(?): ")
	if color in color_list:
		return color
	else:
		return -1

def _demanaMarca():
	return raw_input("Car Brand(?): ")

def _check_place(placa):
	return len(placa) <= 3 and int(placa) < places and placa.isdigit()

def _demanaPlaca():
	placa = raw_input("placa(?): ")
	if placa == '':
		return _feplace()
	elif placa.isdigit() == False:
		return -1
	elif _check_place(placa):
		f = open('places2.dat',"r")
		f.seek(int(placa)*data_size)
		if f.read(1) == "X":
			f.close()
			return int(placa)
		else:
			f.close()
			print "Fully Place"
			return -1
	else:
		return -1

def add_car():
	if _feplace() == -1:
		print "PARKING FULLY"
		return -1
	_guardaDades(_demanaPlaca(), _demanaMatricula(), _demanaColor(), _demanaMarca())
	return 0

def create_Parking():
	confirm = raw_input("Are you Sure? y/N: ")
	if confirm == "y":
		_creaBD()
		print "New Data Base created."

	else:
		print "Abort. Data Base not created."

def del_car():
	f = open('places2.dat',"r+")
	option = raw_input("Delete by place(P) or Number Plate(N)? (P/N): ")
	if option in "PN":
		if option == "P":
			place=raw_input("place?: ")
			if _check_place(place):
				reset = struct.pack(format, 'XXXXXXX','XXXXXX','XXXXXXXXXX')
				f.seek(int(place)*data_size)
				f.write(reset)
			else:
				print "Incorrect Place"

		elif option=="L":
			NP=raw_input("Number plate?: ")
			if _check_numberPlate(NP):
				for i in range(places):
					if _llegeixDades(i)[0] == NP:
						reset = struct.pack(format, 'XXXXXXX','XXXXXX','XXXXXXXXXX')
						f.seek(i*data_size)
						f.write(reset)
					else:
						print "Car not in Parking"
			else:
				print "matricula incorrecta"
	f.close()

def disponible_Places():
	freeplaces = 0
	for i in range(places):
		if _llegeixDades(i)[0] == 'XXXXXXX':
			freeplaces +=1
	print freeplaces, "remaining"

def check_ParkingPlace():
	place = raw_input("Place to check?: ")
	if _check_place(place):
		dades = _llegeixDades(int(place))
		if dades[0] == 'XXXXXXX':
			print "Empty Place"
		else:
			print "Place FULL! \nCar with LP:   ", dades[0], "\nColor:\t\t", dades[1], "\nBrand:\t\t", dades[2]
	else:
		print "Bad place"
		return -1

def find_car():
	lp = raw_input("LP's car to find?: ")
	if _check_numberPlate(lp):
		for p in range(places):
			data =_llegeixDades(p)
			if data[0] == lp:
				print "Car parked in place", p
				return 0
		print "No car found"
		return -1

	else:
		print "Bad License Plate."
		return -1

def find_car_color():
	color = _demanaColor()
	found = 0
	for p in range(places):
		dades = _llegeixDades(p)
		if color in dades[1]:
			found = 1
			print "Place: ",p,"-> LP:",dades[0], "\tColor:",dades[1], "\tBrand:",dades[2]
	if found == 0:
		print "There are no ", color, "car."
		return -1
	return 0

def find_car_brand():
	brand = _demanaMarca()
	found = 0
	for p in range(places):
		dades = _llegeixDades(p)
		if brand in dades[2]:
			found = 1
			print "Place: ",p ,"-> LP:", dades[0], "\tColor:", dades[1], "\tBrand:", dades[2]

	if found == 0:
		print "There are no ", brand, "car."
		return -1
	return 0

def menu():
    """
    Funcio que te com a proposit printar el menu.
    """
    print "\n MENU \n"
    print "0. crear PARKING."
    print "1. Anadir COCHE."
    print "2. Quitar COCHE."
    print "3. Plazas dispobibles."
    print "4. Comprueba Estado de la plaza."
    print "5. Comprueba vehiculo."
    print "6. Vehiculos de un solo color."
    print "7. Vehiculos de una sola marca."
    print "8. Help."
    print "9. Exit"

def main():
	menu()
	opcion=raw_input("option: ")
	while opcion != "9":
		if opcion == "0":
			create_Parking()
			menu()
			opcion=raw_input("option: ")
		elif opcion=="1":
			add_car()
			menu()
			opcion=raw_input("option: ")
		elif opcion=="2":
			del_car()
			menu()
			opcion=raw_input("option: ")
		elif opcion=="3":
			print disponible_Places()
			menu()
			opcion=raw_input("option: ")
		elif opcion=="4":
			check_ParkingPlace()
			menu()
			opcion=raw_input("option: ")
		elif opcion=="5":			
			find_car()
			menu()
			opcion=raw_input("option: ")
		elif opcion == "6":
			find_car_color()
			menu()
			opcion = raw_input("option: ")
		elif opcion == "7":
			find_car_brand()
			menu()
			opcion = raw_input("option: ")
		elif opcion == "8":
			print "Valid colors:",color_list
			menu()
			opcion = raw_input("option: ")
		else:
			print "Wrong option"
			menu()
			opcion=raw_input("option: ")
main()
