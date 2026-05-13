from datetime import datetime

def sapa():
    print("Hai!!") #harus dengan indent agar mausk dalam fungsi def

def sapa_nama(nama=None): #None = default parameter
    if nama is None:
        print("Silakan masukkan nama")
        return
    print(f"Hai {nama}, Apa kabar?")
    

sapa()
sapa_nama("Hasti")
sapa_nama("")
sapa_nama() #gabisa run karena sapa_nama sudah difungsikan harus input nama

print (datetime.now())