daftar_buku = {
     "Buku1" : "Harry Potter",
     "Buku2" : "Percy Jackson",
     "Buku3" : "Twillight"
}    
print(daftar_buku[0])
print(daftar_buku["Buku2"])
print(daftar_buku["Buku3"])


daftar_buku = {}

daftar_buku["novel 1"] = "senyuman pertama di pagi hari airin" 
daftar_buku[1] = "Matahari"
print(daftar_buku)


daftar_buku = dict(Buku1 = "Harry potter", Buku2 = "Percy Jackson")
print (daftar_buku)
print(daftar_buku)
print(daftar_buku.get("buku2"))

nilai = {
    "Matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81,
    "Kimia" : 78,
    "Fisika" : 80
}

for i in nilai:
    print(i)
    
for i, j in nilai.items():
    print(j)
 
 
 
 
nilai ={
    "Matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81,
    "Kimia" : 78,
    "Fisika" : 80
}   
    









nilai ={
    "Matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81,
    "Kimia" : 78,
    "Fisika" : 80
}   
print(nilai)
print()
trasbhin = nilai.pop("Matematika")

print(nilai)
print()
print(type(trasbhin))

del nilai['Fisika'] 
print()
print(nilai)

nilai.clear()

print(nilai) 


nilai ={
    "Matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81,
    "Kimia" : 78,
    "Fisika" : 80
}   
    
print(f"jumlah elemen dari variabel dict nilai adalah {len(nilai)}")

daftar_nilai = nilai.copy() 
print(daftar_nilai)

key = "motor", "mobil", "sepeda"
value = 2 
daftar_kendaraan = dict.fromkeys(key, value)

print(daftar_kendaraan)

Musik = {
"The Chainsmoker" : ["All we Know", "TheParis"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}

for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
        print("") 
        
mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18}
}
for key, value in mahasiswa.items():
    print("ID Mahasiswa : ", key)
    for key_a, value_a in value.items():
        print (key_a, " : ", value_a)
        print("")
print(mahasiswa[111]["Umur"])
    