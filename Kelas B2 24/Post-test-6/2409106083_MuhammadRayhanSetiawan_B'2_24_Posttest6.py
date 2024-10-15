# Inisialisasi kontak sebagai dictionary
daftar_kontak = {}

while True:
    print("\n=== Aplikasi Daftar Kontak ===")
    print("1. Tampilkan Semua Kontak")
    print("2. Tambah Kontak")
    print("3. Perbarui Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

    pilihan = input("Pilih opsi (1/2/3/4/5): ")

    if pilihan == "1":
        # Tampilkan semua kontak
        if daftar_kontak:
            print("\nDaftar Kontak:")
            for nama, info in daftar_kontak.items():
                print(f"Nama: {nama}, Nomor: {info['nomor']}, Email: {info['email']}")
        else:
            print("\nDaftar kontak kosong.")

    elif pilihan == "2":
        # Tambah kontak baru
        nama = input("Masukkan nama: ")
        if nama in daftar_kontak:
            print("Kontak dengan nama ini sudah ada!")
        else:
            nomor = input("Masukkan nomor telepon: ")
            email = input("Masukkan email: ")
            daftar_kontak[nama] = {'nomor': nomor, 'email': email}
            print(f"Kontak {nama} berhasil ditambahkan.")

    elif pilihan == "3":
        # Perbarui kontak
        nama = input("Masukkan nama kontak yang ingin diperbarui: ")
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

    elif pilihan == "4":
        # Hapus kontak
        nama = input("Masukkan nama kontak yang ingin dihapus: ")
        if nama in daftar_kontak:
            del daftar_kontak[nama]
            print(f"Kontak {nama} berhasil dihapus.")
        else:
            print("Kontak tidak ditemukan.")

    elif pilihan == "5":
        # Keluar dari program
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
