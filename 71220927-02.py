#input
inch=int(input('Masukan dalam ukuran dalam inc = '))

#Proses
fot=inch//12
inc=inch-(fot*12)
yrd=fot//3
foot=fot-(yrd*3)
mil=yrd//1760
yrd=yrd-(mil*1760)
#hasil
print(inch,"inch = ",mil,"mile",yrd,"yard",foot,'feet',inc,"inch")
