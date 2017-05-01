# -*- coding: utf-8 -*-
from urllib2 import urlopen
from csv import reader

def getDadesAccidents():
    """
    Llistat de les persones que han estat involucrades en un accident gestionats per la Guàrdia Urbana a la ciutat de Barcelona
    i que han sofert algun tipus de lesió ( ferit lleu, ferit greu o mort). Inclou descripció de la persona
    (conductor, passatger o vianant), sexe, edat, vehicle associat a la persona i si la causa ha sigut del vianant.
    """
    data=[]
    f=urlopen("http://opendata-ajuntament.barcelona.cat/data/dataset/87aa433e-fef8-4ff4-8f9a-d66e9beefff6/resource/08afa8b9-c2fd-4a11-a416-e8650b7fb838/download/2016_accidents_persones_gu_bcn_.csv")
    j=reader(f)
    i=0
    for element in j:
        valor=[]
        if i==0:
            pass
        elif i<100:
            if element[20]=='Desconegut':

                element[20] = 0
            else:
                pass
            valor=[element[0][:11],element[2],element[4],element[6],element[9],element[13],element[14],element[15],element[16],element[18],element[19],int(element[20])]
            #print element , len(element)# el primer elemento es la capcelera
            data.append(valor)
        else: break
        i+=1
    return data
def getDadesVehicles():
    data=[]
    f=urlopen("http://opendata-ajuntament.barcelona.cat/data/dataset/317e3743-fb79-4d2f-a128-5f12d2c9a55a/resource/b49e7402-65ed-49c8-8d03-a6cade73bad6/download/2016_accidents_vehicles_gu_bcn_.csv")
    j=reader(f)
    i=0
    for element in j:
        valor=[]
        if i==0:
            pass
        elif i<100:
            if element[22]=='Desconegut':
                element[22] = 0
            else:
                pass
            valor=[element[0],element[2],element[4],element[6],element[9],element[13],element[14],element[15],element[17],element[19],element[21],int(element[22])]
            data.append(valor)
        else: break
        i+=1
    return data

def getDadesCausalitat():
    data=[]
    f=urlopen("http://opendata-ajuntament.barcelona.cat/data/dataset/719b1054-4166-4692-b63e-622b621b4293/resource/1c647e80-fbdf-4f87-af48-3085fcc9a4a5/download/2016_accidents_causes_gu_bcn_.csv")
    j=reader(f)
    i=0
    for element in j:
        valor=[]
        if i==0:
            pass
        elif i<100:
            valor=[element[0],element[17]]
            data.append(valor)
        else: break
        i+=1
    return data
