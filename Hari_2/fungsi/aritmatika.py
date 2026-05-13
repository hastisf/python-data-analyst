def add(a, b):
    total = a + b
    return total  #return untuk mengembalikan

jumlah = add(10, 5)
print(f"Jumlah dari 10 dan 5 = {jumlah}")
print(f"Jumlah dari 10 dan 5 = {add(10, 5)}")

#Tanpa Return
print("\n")
print("Tanpa Return")
def add(a, b):
    total = a + b

print(add(10, 5))  #hasilnya None

#Error Handling
#print("\n")
#print("Error Handling")
#def add(a, b):
 #   total = a + b
#print(add())  # ERROR

#maka menjadi
def add(a = None, b=None):
    if a== None or b == None:
        print("parameter tidak lengkap")
        return
    
    total = a + b
    return total

def substract(a = None, b=None):
    if a== None or b == None:
        print("parameter tidak lengkap")
        return
    
    total = a - b
    return total

def bmi(berat = None, tinggi=None):
    if berat == None or tinggi == None:
        print("parameter tidak lengkap")
        return
    
    total = ((berat)/(tinggi*tinggi/10000))
    return total

def bmi_check(bmi):
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
        

