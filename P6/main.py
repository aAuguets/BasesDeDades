from Tkinter import *
from bd import *
import ttk


def mostra_tree():
    info_contactes = contactes_bd()
    #print info_contactes
    for i in range(len(info_contactes)):
        tree.insert('','end',text=''.format(info_contactes[i][0]), values=(info_contactes[i][0],info_contactes[i][1], info_contactes[i][2]))

def insereix_contacte():

    n = nom.get()
    t = telf.get()
    m = mail.get()
    #print n, t, m
    afegeix_usuari(n, t, m)
    
    Message(f1, text='Contacte afegit', width=200, fg='green').grid(row=1, column=1)


root = Tk()
crear_bd()

root.title("Gestor de contactes")

# FRAME 1
f1 = Frame(root)
f1.pack()
photo1 = PhotoImage(file = 'dipse.gif')
label1 = Label(f1,image = photo1)
label1.grid(row=0, column=0)

#fc - frame contactes
fc = LabelFrame(f1, text="Nou Registre", padx=10, pady=10)
fc.grid(row=0, column=1)

# Frame contactes
Label(fc, text="Nom: ").grid(row=0)
Label(fc, text="Telefon:").grid(row=1)
nom = StringVar()

Entry(fc, textvariable=nom).grid(row=0, column=1)
telf = StringVar()
Entry(fc, textvariable=telf).grid(row=1, column=1)

Label(fc, text="Email: ").grid(row=2)
mail = StringVar()
Entry(fc, textvariable=mail).grid(row=2, column=1)

Button(fc, text="Afegeix Contacte", command = insereix_contacte).grid(row=3, column=1)

Button(f1, text="Mostra Contactes").grid(row=1, column=0)

# FRAME 2
f2 = Frame(root)
f2.pack()

#Treeview
tree = ttk.Treeview(f2)
tree["columns"]=("one","two", "three")
tree["show"]='headings'
tree.column("one", width=150 )
tree.column("two", width=100)
tree.column("three", width=175)
tree.heading("one", text="Nom")
tree.heading("two", text="Telefon")
tree.heading("three", text="Mail")
tree.pack()

# ff - Footer Frame
ff = Frame(root)
ff.pack(side=BOTTOM)

Button(ff, text="Elimina selecionat").grid(row=1, column=0)
Button(ff, text="Modifica selecionat").grid(row=1, column=1)
Button(ff, text="EXTRA UNKNOWN").grid(row=1, column=2)
Button(ff, text="Sortir",  command= exit).grid(row=1, column=3)
root.resizable(width=False, height=False)


mostra_tree()
root.mainloop()
