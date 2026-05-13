a = "10"
b = "3.14"
c = 1
d = 0
e = 1000

#Konversi String ke Integer
int_a = int(a)
float_a = float(a)
print(int_a +int_a)
print(float(a))  #"10" itu string bisa dikonversi ke integer dan float


float_b = float(b)
print(float_b * int_a * float_a)

bool_c = bool(c)  #Nilai 1 kalau di boolean = True
print(bool(c))
print("Konversi dari", c, "adalah", bool_c)

bool_d = bool(d)  #Nilai 0 kalau di boolean = False
print(bool_d)
print("Konversi dari", d, "adalah", bool_d)

str_e = str(e)
print(str_e, type(str_e))
print( str_e + str_e)