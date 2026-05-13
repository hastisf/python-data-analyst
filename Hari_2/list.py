#LIST
print("List")
index =[0,      1,        2,      3,       4,     5]
nama = ["Ani", "Budi", "Cyana", "Dedi", "Ella", "Farah", ]
nilai = [85, 90, 78, 92, 72, 89]
mix = [1, "Python", True, 3.14]

#Index
print("Index")
print(nilai[0])
print(nama[-1])  #amnil data dari paling belakang
print("\n") #artinya enter
print("Print dengan Index")
print(f"Nama {nama[1]} mendapatkan nilai {nilai[1]}")

for z in range(3): #3 berarti pengulangan 3x
    print(z) #z adalah index
    print(f"Nama {nama[z]} mendapatkan nilai {nilai[z]}")
    
    
#Pakai Len
print("\n")
print("Len")
print("Print dengan Index")
print(f"panjang data dari nama = {len(nama)}")

for z in range(len(nama)): #3 berarti pengulangan 3x
    print(z) #z adalah index
    print(f"Nama {nama[z]} mendapatkan nilai {nilai[z]}")
    

#Slicing
print("\n")
print("Slicing")
nama_slice_3_tengah = nama[2:5] #dari index ke 2 sampai data ke 5 (index 4 atau n-1)
nilai_slice_3_tengah = nilai[2:5]
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#Ubah Elemen
print("\n")
print("Ubah Nama")
nama_slice_3_tengah[0] = "Cyandika"
nilai_slice_3_tengah[0] = 95  #awalnya 85 jadi 95
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#Insert
print("\n")
print("Insert")
nilai_slice_3_tengah.insert(1,85)
nama_slice_3_tengah.insert(1, "Diana")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#Append
print("\n")
print("Append")
nama_slice_3_tengah.append("Zara")
nilai_slice_3_tengah.append(100)
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#Sort
print("\n")
print("Sort") #mengurutkan nama
nama_slice_3_tengah.sort()
print(nama_slice_3_tengah)

#Pop
print("\n")
print("Pop")  #paling belakang hilang
nama_slice_3_tengah.pop()
print(nama_slice_3_tengah)

#Reverse
print("\n")
print("Reverse")  #dibalik urutannya
nama_slice_3_tengah.reverse()
print(nama_slice_3_tengah)