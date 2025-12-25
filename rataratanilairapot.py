print(" ================================== ")
print(" PROGRAM RATA-RATA NILAI SEMESTER ")
print(" ==================================")


jumlah_semester = int(input("Masukkan jumlah semester: "))

for s in range(jumlah_semester):
    print(f"\nSemester {s+1}")
    jumlah_mapel = int(input("Jumlah mata pelajaran: "))
    
    total = 0
    for i in range(jumlah_mapel):
        nilai = float(input(f"Nilai mapel ke-{i+1}: "))
        total += nilai
    
    rata = total / jumlah_mapel
    print("Rata-rata Semester", s+1, ":", round(rata, 2))
 
print(" ====================================")
print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI!")
print(" ==================================== ")