from urllib2 import urlopen
from csv import reader

#Acces a dades bigdata http://opendata.bcn.cat/opendata/ca
f=urlopen("http://opendata.bcn.cat/opendata/ca/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2014_omissions-sexe.csv&name=opendata_2014_omissions-sexe.csv")
j=reader(f)
for i in j:
    print i


#Acces a dades bigdata opendata.manresa.cat
#Acces a dades poblacio per nacionalitat
f=urlopen("http://tecckan01.tecnogeo.es/dataset/e9f600ff-983a-4861-95d1-a748c372a33a/resource/fafe5db6-9375-44ff-af51-283dfb0af6b8/download/2014.csv")
j=reader(f)
for i in j:
    print i

