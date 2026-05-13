import aritmatika as f

print(f.add(10,6))
print(f.bmi(55, 1.59))


berat = (float(input("Masukkan Berat Badan (kg): ")))
tinggi = (float(input("Masukkan Tinggi Badan (cm): ")))

bmi = f.bmi(berat,tinggi)
print("BMI kamu adalah", round(bmi,2))

f.bmi_check(bmi)
