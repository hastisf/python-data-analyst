hari = input("Hari apa? ")

match hari:
    case "Senin" | "Selasa" | "Rabu":
        print("Hari kerja awal")
    case "Kamis" | "Jumat":
        print("Hari kerja akhir")
    case "Sabtu" | "Minggu":
        print("Weekend")
    case _:
        print("Hari tidak valid")
    
    
nilai = int(input("Masukkan Nilai (1-7): "))

match nilai:
    case 1 | 2 | 3:    # langsung 1 aja tanpa " " karena integer
        print("Hari kerja awal")
    case 4 | 5:
        print("Hari kerja akhir")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Hari tidak valid")