# Input
nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukan harga barang: "))         
jumlah_barang = int(input("Masukkkan jumlah barang: "))
diskon_barang = float(input("Masukkan diskon barang: "))

   # proses
total_harga_sebelum_diskon = jumlah_barang * harga_barang
hitung_total_diskon = (diskon_barang/100) * total_harga_sebelum_diskon
total_bayar = total_harga_sebelum_diskon - hitung_total_diskon
sisa_bagi = total_bayar / 3
    
    # Output
print(f"Anda membeli {jumlah_barang} {nama_barang} dengan harga satuan {harga_barang}, total sebelum diskon adalah {total_harga_sebelum_diskon},total diskon adalah {hitung_total_diskon}, dan total yang harus dibayar adalah {total_bayar}.")
print(f"dibagi dengan 3 sisanya {sisa_bagi}")
