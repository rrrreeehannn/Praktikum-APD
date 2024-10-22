# Variabel global
daftar_kontak = {}

def tampilkan_kontak():
    """Prosedur untuk menampilkan semua kontak."""
    if daftar_kontak:
        print("\nDaftar Kontak:")
        for nama, info in daftar_kontak.items():
            print(f"Nama: {nama}, Nomor: {info['nomor']}, Email: {info['email']}")
    else:
        print("\nDaftar kontak kosong.")

def tambah_kontak(nama, nomor, email):
    """Fungsi untuk menambah kontak baru."""
    if nama in daftar_kontak:
        print("Kontak dengan nama ini sudah ada!")
    else:
        daftar_kontak[nama] = {'nomor': nomor, 'email': email}
        print(f"Kontak {nama} berhasil ditambahkan.")

def perbarui_kontak(nama):
    """Fungsi untuk memperbarui informasi kontak."""
    if nama in daftar_kontak:
        print("Kontak ditemukan. Pilih informasi yang ingin diperbarui:")
        print("1. Nomor Telepon")
        print("2. Email")
        pilihan_update = input("Masukkan pilihan (1/2): ")

        if pilihan_update == "1":
            nomor_baru = input("Masukkan nomor telepon baru: ")
            daftar_kontak[nama]['nomor'] = nomor_baru
            print(f"Nomor telepon {nama} berhasil diperbarui.")
        elif pilihan_update == "2":
            email_baru = input("Masukkan email baru: ")
            daftar_kontak[nama]['email'] = email_baru
            print(f"Email {nama} berhasil diperbarui.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Kontak tidak ditemukan.")

def hapus_kontak(nama):
    """Fungsi untuk menghapus kontak."""
    if nama in daftar_kontak:
        del daftar_kontak[nama]
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

# Prosedur utama untuk menjalankan aplikasi
def main():
    while True:
        print("\n=== Aplikasi Daftar Kontak ===")
        print("1. Tampilkan Semua Kontak")
        print("2. Tambah Kontak")
        print("3. Perbarui Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == "1":
            tampilkan_kontak()
        elif pilihan == "2":
            nama = input("Masukkan nama: ")
            nomor = input("Masukkan nomor telepon: ")
            email = input("Masukkan email: ")
            tambah_kontak(nama, nomor, email)
        elif pilihan == "3":
            nama = input("Masukkan nama kontak yang ingin diperbarui: ")
            perbarui_kontak(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama kontak yang ingin dihapus: ")
            hapus_kontak(nama)
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()