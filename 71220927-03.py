#input
detik=int(input("Masukan waktu dalam detik : "))
#proses
hari_detik=86400/detik
detikk1=detik%(3600*24)
detikk2=detikk1%(3600)
menitt=detikk2//60
jmm=detikk1//3600
detikk3=detikk2%60
harrri=detik//86400
#output
print(detik,"detik = ",harrri,"hari,",jmm,"jam,",menitt,"menit,",detikk3,"detik")
