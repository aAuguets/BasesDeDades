import struct

format = '7s10s10s'
data_size=struct.calcsize(format)
f=open('test.dat','w+')
f.seek(0*data_size)
t=struct.pack(format, '3333ABC', 'Orange', 'Jokese')
f.write(t)
f.seek(0*data_size)
print "1"
s=f.read(data_size)
r=struct.unpack(format, s)
print "r"
print r
for e in r:
	e.strip()
	print "e"
	print e