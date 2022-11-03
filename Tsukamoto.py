def turun(b,a,x):
    if(x<=a):
        nilai = 1
    elif(x>a and x<b):
        nilai = (b-x)/(b-a)
    elif(x>=b):
        nilai = 0

    return nilai
def naik(b,a,x):
    if(x<=a):
        nilai = 0
    elif(x>a and x<b):
        nilai = (x-a)/(b-a)
    elif(x>=b):
        nilai = 1

    return nilai
def agregasi_turun(b,a,alfa):
    nilai = b - (alfa*(b-a))
    return nilai
def agregasi_naik(b,a,alfa):
    nilai = alfa*(b-a) + a
    return nilai
var = int(input("Jumlah variabel: "))

nama_var = []
for i in range(var):
    nama = input("Sebutkan nama variabel: ")
    nama_var.append(nama)
# Jumlah variabel: 3
# Sebutkan nama variabel: permintaan
# Sebutkan nama variabel: persediaan
# Sebutkan nama variabel: produksi

variabel = dict()
for i in nama_var:
    print(i)
    up = int(input("naik : "))
    down = int(input("turun : "))
    variabel.update({i+"_naik":up})
    variabel.update({i+"_turun":down})
    
print(variabel)
# permintaan
# naik : 5000
# turun : 1000
# persediaan
# naik : 600
# turun : 100
# produksi
# naik : 7000
# turun : 2000
# {'permintaan_naik': 5000, 'permintaan_turun': 1000, 'persediaan_naik': 600, 'persediaan_turun': 100, 'produksi_naik': 7000, 'produksi_turun': 2000}

soal = dict()

jml = int(input("Jumlah variabel yang diketahui : "))

for i in range(jml):
    ver = input("Nama variabel : ")
    val = int(input("Nilai : "))   
    soal.update({ver:val})
    
print(soal)

dit = input("Variabel yang ditanyakan : ")
# Jumlah variabel yang diketahui : 2
# Nama variabel : permintaan
# Nilai : 4000
# Nama variabel : persediaan
# Nilai : 300
# {'permintaan': 4000, 'persediaan': 300}
# Variabel yang ditanyakan : produksi

nk = dict()
for i in soal:
    up = naik(variabel[i+"_naik"],variabel[i+"_turun"],soal[i])
    down = turun(variabel[i+"_naik"],variabel[i+"_turun"],soal[i])
    nk.update({i+"_naik":up})
    nk.update({i+"_turun":down})

print(nk)
# {'permintaan_naik': 0.75, 'permintaan_turun': 0.25, 'persediaan_naik': 0.4, 'persediaan_turun': 0.6}
# [R1]   IF permintaan TURUN AND Persediaan BANYAK, THEN Produksi Barang dr;
# [R2]   IF permintaan TURUN AND Persediaan SEDIKIT, THEN Produksi Barang BERKURANG;
# [R3]   IF permintaan NAIK AND Persediaan BANYAK, THEN Produksi Barang BERTAMBAH;
# [R4]   IF permintaan NAIK AND Persediaan SEDIKIT, THEN Produksi Barang BERTAMBAH;

#AGREGASI
alfa = []
z = []

r = int(input("Masukkan jumlah peraturan : "))

for i in range(r):
    kondisi1 = input("Kondisi 1(naik/turun): ")
    kondisi2 = input("Kondisi 2(naik/turun): ")
    kesimpulan = input("Kesimpulan(naik/turun): ")
    #Fire Strength INTERSEKSI (AND)
    a = min(nk[kondisi1],nk[kondisi2]) 
    alfa.append(a)
    if(kesimpulan == "turun"):
        zz = agregasi_turun(variabel[dit+"_naik"],variabel[dit+"_turun"],a)
    elif(kesimpulan == "naik"):
        zz = agregasi_naik(variabel[dit+"_naik"],variabel[dit+"_turun"],a)        
    z.append(zz)
# Masukkan jumlah peraturan : 4
# Kondisi 1(naik/turun): permintaan_turun
# Kondisi 2(naik/turun): persediaan_naik
# Kesimpulan(naik/turun): turun
# Kondisi 1(naik/turun): permintaan_turun
# Kondisi 2(naik/turun): persediaan_turun
# Kesimpulan(naik/turun): turun
# Kondisi 1(naik/turun): permintaan_naik
# Kondisi 2(naik/turun): persediaan_naik
# Kesimpulan(naik/turun): naik
# Kondisi 1(naik/turun): permintaan_naik
# Kondisi 2(naik/turun): persediaan_turun
# Kesimpulan(naik/turun): naik

print(alfa)
print(z)
# [0.25, 0.25, 0.4, 0.6]
# [5750.0, 5750.0, 4000.0, 5000.0]

#DEFUZIFIKASI
df = 0

for i in range(len(alfa)):
    df += alfa[i]*z[i]

defuz = int(df/sum(alfa))

print("Jadi, nilai ",dit," adalah ",defuz)
# Jadi, nilai  produksi  adalah  4983