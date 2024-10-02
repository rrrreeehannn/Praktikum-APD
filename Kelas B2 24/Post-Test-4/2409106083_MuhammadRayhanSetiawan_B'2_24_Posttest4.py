kesempatan = 3
while kesempatan > 0:
    print("Masukan username")
    username = input()
    password = input("Masukkan password \n")
    
    if username == "rehann" and password == "083":
        ulang = "y"
        while ulang == "y":
            print("Masukan berat dalam Mg")
            beratmg = float(input())
            print("Masukan tinggi badan dalam Km")
            tinggikm = float(input())
            beratkg = beratmg / 100000
            tinggim = tinggikm * 1000
            bmi = beratkg / tinggim ** 2
            if bmi < 18:
                kategori = "berat badan kurang (Underweight)"
                print(f"BMI anda adalah : {bmi}")
                print("kategori: " + kategori)
            else:
                if bmi < 18:
                    kategori = "berat badan normal"
                    print(f"BMI anda adalah : {bmi}")
                    print("kategori: " + kategori)
                else:
                    if bmi < 18:
                        kategori = "berat badan berlebih (Overweight)"
                        print(f"BMI anda adalah : {bmi}")
                        print("kategori: " + kategori)
                    else:
                        kategori = "obesitas"
            print("keluar tidak? y/n")
            ulang = input()
            
            if ulang == "y":
                ulang = "n"
                kesempatan = 0
                print("Anda berhasil keluar")
            else:
                ulang = "y"
    else:
        kesempatan = kesempatan - 1
        print(f"Username atau password anda salah!, Sisa kesempatan login anda {kesempatan}")
