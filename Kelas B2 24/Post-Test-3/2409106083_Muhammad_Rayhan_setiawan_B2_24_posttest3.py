berat_mg = float(input("Masukkan berat badan mg: "))
tinggi_km = float(input("Masukkan tinggi badan dalam km: "))
# konversi berat mg ke kg 
berat_kg = berat_mg / 100000
# konversi tinggi dari km ke m
tinggi_m = tinggi_km * 1000
# rumus BMI 
bmi = berat_kg / (tinggi_m ** 2)
if bmi < 18.5:
    kategori = "berat badan kurang (Underweight)" 
elif bmi < 24.9:
    kategori = "berat badan normal"
elif bmi < 29.9:
    kategori = "berat badan berlebih (Overweight)" 
else:
    kategori = "Obesitas"  
    
print(f"BMI anda adalah: {bmi:.2f}")
print(f"kategori: {kategori}")