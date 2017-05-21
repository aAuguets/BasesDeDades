from Tkinter import *
from bd import *
import ttk
import tkMessageBox as tkmb
import tkFileDialog
from PIL import Image, ImageTk

#me genero una variable global de si e cambiado o no de imagen
cambio=False

def mostra_tree():
    contingut = tree.get_children()
    for i in contingut:
        tree.delete(i)
    info_contactes = contactes_bd()
    #print info_contactes
    for i in range(len(info_contactes)):
        tree.insert('','end',text=''.format(info_contactes[i][0]), values=(info_contactes[i][0],info_contactes[i][1], info_contactes[i][2]))

def insereix_contacte():

    n = nom.get()
    t = telf.get()
    m = mail.get()
    #print n, t, m
    if (n!= '' and t!='' and m!='' ):
        if(afegeix_usuari(n, t, m)):
            mostra_tree()
            Message(f1, text='Contacte afegit', width=200, fg='green').grid(row=1, column=1)
        else:
            Message(f1, text='Error. Mail repetit', width=200, fg='red').grid(row=1, column=1)
    else:
        Message(f1, text='Errror, introduce algun campo', width=200, fg='red').grid(row=1, column=1)
def elimina_contacte():
    dadestree = tree.focus()
    mail = tree.item(dadestree)['values'][2]
    if(del_contacte(mail)):
        mostra_tree()
        Message(f1, text='Contacte Eliminat', width=200, fg='green').grid(row=1, column=1)
    else:
        Message(f1, text='Error. No eliminat', width=200, fg='red').grid(row=1, column=1)

def actualitza_dades():
    global mailm, telf_n, ventana,nom_n, fotolabel, img_n,cambio
    te= telf_n.get()
    nomn=nom_n.get()
    if (cambio==True):
        cambio=False
    #img_n tiene que ser el filename de la nueva imagen
        if(actualitza(mailm, te , 'perfil1.jpg', nomn)):
            print "si que hemos cambiado imagen, actualiza bien"
            mostra_tree()
            Message(f1, text='Contacte Actualitzat', width=200, fg='green').grid(row=1, column=1)
        else:
            Message(f1, text='Error. No Actualitzat', width=200, fg='red').grid(row=1, column=1)
    else:
        print ""
        if(actualitza(mailm, te,'', nomn)):
            print " No hemos cambiado la imagen, actualiza bien"
            mostra_tree()
            Message(f1, text='Contacte Actualitzat', width=200, fg='green').grid(row=1, column=1)
        else:
            Message(f1, text='Error. No Actualitzat', width=200, fg='red').grid(row=1, column=1)

    ventana.destroy()

def modifica_contacte():

    global mailm, telf_n, ventana, nom_n
    dadestree = tree.focus()
    mailm = tree.item(dadestree)['values'][2]
    telf = tree.item(dadestree)['values'][1]
    nom = tree.item(dadestree)['values'][0]
    #Frame finestra emergent
    ventana = Toplevel()
    ventana.title('Modifica contacte')
    #primero cogemos la imagen
    #print perfil_foto
    #fe = Frame(top)
    #fd=Frame(fe)
    #fe.pack(side=RIGHT)
    #fe.pack()
    #perfil_foto = PhotoImage(file = 'new.gif')
    #path="homer.jpg"
    #cogemos la img de ba BD y lo mostramos en el frame(ventana)
    path=returnIMG(mailm)
    print "leemos image BD"
    with open('perfil1.jpg',"w+b") as f:
        f.write(path)
    f.close()
    img=ImageTk.PhotoImage(Image.open('perfil1.jpg'))
    PhotoIm = Label(ventana,image = img)
    PhotoIm.image=img
    PhotoIm.place(x=0,y=0)
    PhotoIm.grid(row=0,column=0)

    frameiz=LabelFrame(ventana)
    frameiz.grid(row=0,column=2)
    Label(frameiz, text="Nom: ").grid(row=0)
    n=Entry(frameiz)
    n.insert(0,nom)
    n.config(state=DISABLED)
    n.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    Label(frameiz, text="Nom nou: ").grid(row=1)
    nom_n = StringVar()
    Entry(frameiz, textvariable=nom_n).grid(row=1, column=1)

    Label(frameiz, text="Telf vell: ").grid(row=2)
    t0=Entry(frameiz)
    t0.insert(0,telf)
    t0.config(state=DISABLED)
    t0.grid(row=2, column=1, padx=5, pady=5)

    Label(frameiz, text="Telf nou: ").grid(row=3)
    telf_n = StringVar()
    Entry(frameiz, textvariable=telf_n).grid(row=3, column=1)

    Label(frameiz, text="Mail: ").grid(row=4)
    t0=Entry(frameiz)
    t0.insert(0,mailm)
    t0.config(state=DISABLED)
    t0.grid(row=4, column=1, padx=5, pady=5)
    #botones
    Button(ventana, text="Actualitza dades", command = actualitza_dades).grid(row=2, column=2)
    Button(ventana, text="Afegeix imatge", command = afegir_image).grid(row=2, column=0)
    #ventana.mainloop()

def sort_contactes_tree():
    contingut = tree.get_children()
    for i in contingut:
        tree.delete(i)

    info_contactes = sort_contactes()
    #print info_contactes
    for i in range(len(info_contactes)):
        tree.insert('','end',text=''.format(info_contactes[i][0]), values=(info_contactes[i][0],info_contactes[i][1], info_contactes[i][2]))

def sortida():
    global E
    con=lite.connect('gest_cont.db')
    cur=con.cursor()
    cur.execute("SELECT * from CONTACTES;")
    rows=cur.fetchall()
    f=open('dades.txt','w')
    for element in rows:
        f.write(str(element))
    f.close()
    if tkmb.askokcancel("Exit", "vols sortir?"):
        root.destroy()

def afegir_image():
    """
    funcion que lee la imagen y la guarda la nueva imagen en perfil1.jpg
    """
    global img_n, cambio
    cambio=True
    fileImage=tkFileDialog.askopenfilename()
    with open(fileImage,"rb") as i:
        img_n=i.read()
    with open('perfil1.jpg',"w+b") as f:
        f.write(img_n)
    f.close()
    i.close()
    print "afegir imatge bien! modificamos perfil1.jpg"
    #es necesario esto?
    #foto2=PhotoImage(image='perfil1.jpg')
    #fotolabel.config(image=foto2)

def mostra_contacte():
    """
    global mailm, telfn, top, img
    dadestree = tree.focus()
    mailm = tree.item(dadestree)['values'][2]
    print mailm
    telf = tree.item(dadestree)['values'][1]
    nom = tree.item(dadestree)['values'][0]
    ventana= Toplevel()
    ventana.title("Info Contacte")
    myframe4=Frame(ventana)
    info=LabelFrame(ventana,text="info_contactes",padx=10,pady=10)
    info.grid(row=0,column=1)
    #imagen en la ventana
    #perfil_foto=returnIMG(mailm)
    print perfil_foto
    with open("perfil.gif","w+b") as i:
        i.read(perfil_foto)
    foto=PhotoImage(file='perfil.gif')
    labelfoto=Label(Ventana,image=foto)
    labelfoto.grid(row=0,column=1)

    Label(info, text="Nom: ").grid(row=0)

    n=Entry(info)
    n.insert(0,nom)
    n.config(state=DISABLED)
    n.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    Label(info, text="Telf: ").grid(row=1)
    t0=Entry(info)
    t0.insert(0,telf)
    t0.config(state=DISABLED)
    t0.grid(row=1, column=1, padx=5, pady=5)

    Label(info, text="Mail: ").grid(row=2)
    t1=Entry(info)
    t1.insert(0,mailm)
    t1.config(state=DISABLED)
    t1.grid(row=2, column=1, padx=5, pady=5)


    Button(ventana, text="Afegeix imatge", command = afegir_image).grid(row=3, column=1)
    Button(ventana, text="Actualitza contacte", command = actualitza_dades).grid(row=3, column=2)
    """
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

Button(f1, text="Mostra Contacte", command = sort_contactes_tree).grid(row=1, column=0)

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

Button(ff, text="Elimina selecionat", command = elimina_contacte).grid(row=1, column=0)
Button(ff, text="Modifica selecionat", command = modifica_contacte).grid(row=1, column=1)
Button(ff, text="EXTRA UNKNOWN").grid(row=1, column=2)
Button(ff, text="Sortir",  command= sortida).grid(row=1, column=3)
root.resizable(width=False, height=False)


mostra_tree()
root.mainloop()
