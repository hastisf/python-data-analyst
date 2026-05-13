berat = (float(input("Masukkan Berat Badan (kg): ")))
tinggi = (float(input("Masukkan Tinggi Badan (cm): ")))

#print(berat)
#print(tinggi)

tinggi = tinggi/100

bmi = ((berat)/(tinggi*tinggi))

print ("BMI Kamu =", round(bmi,2), "Yaa")

if bmi >= 30.0:
    print("Obesitas Tingkat 2")
    print("Warning!! Ayok Olahraga!")
elif 25.0 <= bmi <= 29.9: 
    print("Obesitas Tingkat 1")
    print(print("Ayok Olahraga!"))
elif 23.0 <= bmi <= 24.9: 
    print("Overweight")
    print("Dikit Lagi Ideal, Semangat!")
elif 18.5 <= bmi <= 22.9: 
    print("Ideal")
    print("Kamu Kerenn!!")
else:
    print("Underweight")
    print("Makan lebih Banyak Biar Sehat!")
    

       
