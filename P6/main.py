from Tkinter import *
from bd import *
import ttk
win = Tk()

def mostra_tree(tree):
    info_contactes = contactes_bd()
    for i in range(len(info_contactes)):
        tree.insert('','end',text=''.format(info_contactes[i][0]), values=(info_contactes[i][0],info_contactes[i][1]))
    return 0

def Finestra_gestor():
    win.title('Gestor de Contactes')
    #imatge
    f1_i = Frame(win, relief = 'raised')
    f1_i.pack(fill = BOTH)
    photo1 = PhotoImage(file = 'dipse.gif')
    label1_i = Label(f1_i,image = photo1)
    label1_i.pack( side = LEFT, expand = "yes")

    #Contactes
    fc = LabelFrame(f1_i, text="Nou Registre: ")
    fc.pack(side = RIGHT)
    labelc_nom1 = Label(fc, text = 'Nom: ').grid(row = 1, column = 1)
    labelc_nom2 = Entry(fc).grid(row = 1, column = 2)

    labelc_telf1 = Label(fc, text = 'Telefon: ').grid(row = 2,column = 1)
    labelc_telf2 = Entry(fc).grid(row = 2,column = 2)

    labelc_send = Button(fc, text = 'Afegir Contacte').grid(row=3,column=2)

    #mostrar Contactes
    f2 = Frame(win, relief = 'raised')
    f2.pack(fill = BOTH)
    label2_mc = Button(f2,text = 'Mostrar contactes')
    label2_mc.pack(side = LEFT)
    label2_mc = Label(f2, text = '' ,fg='red')
    label2_mc.pack(side = LEFT)


    #Treeview
    f3 = Frame(win)
    f3.pack(fill = BOTH)
    tree = ttk.Treeview(f3)
    tree["columns"]=("one","two","three")
    tree["show"] = 'headings'
    tree.column("one", width=150)
    tree.column("two", width=100)
    tree.column("three", width=200)
    tree.heading("one", text="Nom")
    tree.heading("two", text="Telefon")
    tree.heading("three", text="email")
    tree.pack()

    #Botonera footer
    f4 = Frame(win)
    f4.pack(fill = BOTH)
    label4_b1 = Button(f4,text = 'Eliminar seleccionat').grid(row = 1,column = 1)
    label4_b2 = Button(f4,text = 'Modificar seleccionat').grid(row = 1,column = 2)
    label4_b3 = Button(f4,text = 'Sortir', command = quit).grid(row = 1, column=4)
    label4_b4 = Button(f4,text = 'Funcio_extradeede').grid(row = 1, column=3)
    win.resizable(width=False, height=False)
    mostra_tree(tree)
    win.mainloop()


if(crear_bd()):
    contactes_bd()
    Finestra_gestor()
