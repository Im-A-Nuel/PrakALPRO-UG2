#Input
titik_1X1=int(input("Titik X1 = "))
titik_1Y1=int(input("Titik Y1 = "))
titik_2X2=int(input("Titik X2 = "))
titik_2Y2=int(input("Titik Y2 = "))
#Proses

jarak_duatitik=((titik_2X2-titik_1X1)**2 + (titik_2Y2-titik_1Y1)**2)**0.5
c=round(jarak_duatitik,2)

#Hasil
print("Titik","(",titik_1X1,",",titik_1Y1,")",'dan',"(",titik_2X2,",",titik_2Y2,")",'jaraknya adalah ', c)