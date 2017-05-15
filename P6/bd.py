import sqlite3 as lite


def crear_bd():
    """
    Crear la nostra base de dades
    """
    try:
        con=lite.connect('gest_cont.db')
        cur=con.cursor()
        cur.executescript("""
            PRAGMA foreign_keys = ON;
            DROP TABLE IF EXISTS CONTACTES;
            CREATE TABLE CONTACTES(
                nom text,
                telefon int,
                mail text,
                primary key(mail)
            );

            insert into CONTACTES values("Adria", 666555444, "adria@auguets.cat");
            insert into CONTACTES values("Pavel", 333222111, "pavel@macu.tela");

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
    cur.execute('select * from contactes')
    rows=cur.fetchall()
    print rows
    return rows
