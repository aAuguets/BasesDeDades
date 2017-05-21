import sqlite3 as lite

def crear_bd():
    """
    Crear la nostra base de dades
    """
    try:
        con=lite.connect('gest_cont.db')
        cur=con.cursor()
        #DROP TABLE IF EXISTS CONTACTES;
        cur.executescript("""
            PRAGMA foreign_keys = ON;
            DROP TABLE IF EXISTS CONTACTES;
            CREATE TABLE CONTACTES(
                nom text,
                telefon int,
                mail text,
                foto BLOB,
                primary key(mail)
            );
            CREATE TRIGGER IF NOT EXISTS SAME_NUMBER AFTER INSERT ON CONTACTES
            WHEN (SELECT COUNT(*) FROM CONTACTES WHERE nom= NEW.nom  and TELEFON= NEW.TELEFON ) > 1
            BEGIN
                DELETE FROM CONTACTES WHERE mail=new.mail;
            END;

            CREATE TRIGGER IF NOT EXISTS ACTUALITZA_NO_TELEFON AFTER UPDATE ON CONTACTES
            WHEN NEW.telefon = ''
            BEGIN
            UPDATE CONTACTES SET telefon=OLD.telefon WHERE mail=NEW.mail ;
            END;

            CREATE TRIGGER IF NOT EXISTS ACTUALITZA_NO_NOMBRE AFTER UPDATE ON CONTACTES
            WHEN NEW.nom = ''
            BEGIN
            UPDATE CONTACTES SET nom=OLD.nom WHERE mail=NEW.mail ;
            END;
            CREATE TRIGGER IF NOT EXISTS ACTUALITZA_NO_IMG AFTER UPDATE ON CONTACTES
            WHEN NEW.foto = ''
            BEGIN
            UPDATE CONTACTES SET foto=OLD.foto WHERE mail=NEW.mail;
            END;
        """)
        con.commit()
        con.close()
        return True
    except:
        print "ERROR Crear"
        return False

def contactes_bd():
    con=lite.connect('gest_cont.db')
    cur=con.cursor()
    cur.execute('select * from CONTACTES')
    rows=cur.fetchall()
    con.close()
    return rows
def sort_contactes():
    con=lite.connect('gest_cont.db')
    cur=con.cursor()
    cur.execute('select * from CONTACTES order by nom asc')
    rows=cur.fetchall()
    con.close()
    return rows


def afegeix_usuari(nom, telf, mail):
    try:
        con=lite.connect('gest_cont.db')
        cur=con.cursor()
        with open('perfil.jpg',"rb") as i:
            imatge=i.read()
        imatge_perfil=lite.Binary(imatge)
        cur.execute("INSERT into CONTACTES values(?, ?, ?, ?);",(nom,telf,mail,imatge_perfil,))
        con.commit()
        i.close()
        con.close()
        return True
    except:
        print "Error al afegir usuaris."
        return False

def del_contacte(mail):
    try:
        con=lite.connect('gest_cont.db')
        cur=con.cursor()
        cur.execute("DELETE FROM CONTACTES where mail=?;",(mail,))
        con.commit()
        con.close()
        return True
    except:
        print "Error al Eliminar."
        return False

def returnIMG(mail):
    try:
        con=lite.connect('gest_cont.db')
        cur=con.cursor()
        cur.execute("SELECT foto FROM CONTACTES WHERE mail=? ;",(mail,))
        return cur.fetchall()[0][0]
    except:
        print "ERROR return img"

def actualitza(mail, new_tel,filename_imatge,new_nom):
    try:
        con=lite.connect('gest_cont.db')
        cur=con.cursor()
        if (filename_imatge == '') :
            cur.execute("UPDATE CONTACTES SET telefon = ? , nom = ? where mail=?;",(new_tel,new_nom,mail,))
        else:
            print "abrimos el archivo de la imagen "+str(filename_imatge)
            print str(mail)+str(new_tel)+str(new_nom)
            with open(filename_imatge, "rb")as f:

                data=f.read()
                print "algo"
            nova_imatge_perfil=lite.Binary(data)
            print "bien"
            f.close()
            print "aqui cerramos bienn perfil1,jpg nuevo"
            cur.execute("UPDATE CONTACTES SET telefon = ? , nom = ?, foto= ? where mail=?;",(new_tel,new_nom,nova_imatge_perfil,mail,))

        con.commit()
        con.close()
        return True
    except:
        print "Error al Actualitzar."
        f.close()
        return False
