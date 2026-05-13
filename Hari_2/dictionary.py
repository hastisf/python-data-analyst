#Dictionary pakai {}
import json #buat bentuk jadi json

data = {
    "nama depan": "alice",
    "nama belakang" : "wonder",
    "alamat" : "bumijo",
    "umur" : 24,
    "hobby" : ["padel", "tennis", 'tenis meja'],
    
}

print(data)
data["alamat"] = "Jogja"

print("\n")
print("setelah diubah")
print(data["alamat"])

#List of Dictionary
print("\n")
print("List of Dictionary")
Bigdata = [
{
    "nama depan": "alice",
    "nama belakang" : "wonder",
    "alamat" : "bumijo",
    "umur" : 24,
    "hobby" : ["padel", "tennis", "tenis meja"],
},
{
    "nama depan": "bob",
    "nama belakang" : "marley",
    "alamat" : "westprog",
    "umur" : 27,
    "hobby" : ["lari", "gym", "basket"],
},
{
    "nama depan": "cyanna",
    "nama belakang" : "astodaya",
    "alamat" : "sleman",
    "umur" : 22,
    "hobby" : ["pilates", "yoga", "gym"],
},
]

print(Bigdata)

print("\n")
print("Append Dasha")
Bigdata.append(
{
    "nama depan": "Dasha",
    "nama belakang" : "Kareem",
    "alamat" : "bantul",
    "umur" : 21,
    "hobby" : ["masak", "baca", "scrolling"],
},
)

print(Bigdata)

#Json
print("\n")
print("Buat Versi Json")
print(json.dumps(Bigdata, indent = 3)) #indent dibuat agar menjorok

