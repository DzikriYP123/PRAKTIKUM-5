# Kamus untuk menyimpan data mahasiswa
data_mahasiswa = {}

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

# Menampilkan menu utama
def tampilkan_menu():
    print("\nProgram Input Nilai:")
    print("="*60)
# Fungsi untuk menambah data mahasiswa
def tambah_data():
    nim = input("Masukkan NIM mahasiswa: ")
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    
    # Menyimpan data mahasiswa dalam dictionary
    data_mahasiswa[nim] = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    }
    print("Data mahasiswa berhasil ditambahkan.")

# Fungsi untuk mengubah data mahasiswa
def ubah_data():
    nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
    if nim in data_mahasiswa:
        print("Data mahasiswa ditemukan.")
        nama = input("Masukkan nama baru mahasiswa: ")
        tugas = float(input("Masukkan nilai tugas baru: "))
        uts = float(input("Masukkan nilai UTS baru: "))
        uas = float(input("Masukkan nilai UAS baru: "))
        
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        
        # Update data mahasiswa
        data_mahasiswa[nim] = {
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "nilai_akhir": nilai_akhir
        }
        print("Data mahasiswa berhasil diubah.")
    else:
        print("NIM tidak ditemukan.")

# Fungsi untuk menghapus data mahasiswa
def hapus_data():
    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("NIM tidak ditemukan.")

# Fungsi untuk menampilkan seluruh data mahasiswa
def tampilkan_data():
    if not data_mahasiswa:
        print("Data mahasiswa kosong.")
        print("Daftar Nilai.")
        print("="*60)
        print("|No | NIM | NAMA | TUGAS | UTS | UAS | AKHIR |")
        print("="*60)
        print("|         tidak ada data                     |")
        print("="*60)
    else:
        print("\nDaftar Data Mahasiswa:")
        for nim, data in data_mahasiswa.items():
            print("Daftar Nilai.")
            print("="*60)
            print("|No |    NIM    |  NAMA  | TUGAS | UTS | UAS | AKHIR |")
            print("="*60)
            print(f"|1  | {nim} | {data['nama']} | {data['tugas']} | {data['uts']} | {data['uas']} | {data['nilai_akhir']:.2f} | ")
            print("="*60)
            
# Fungsi untuk mencari data mahasiswa
def cari_data():
    nim = input("Masukkan NIM mahasiswa yang dicari: ")
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        print(f"\nNIM: {nim}")
        print(f"Nama: {data['nama']}")
        print(f"Nilai Tugas: {data['tugas']}")
        print(f"Nilai UTS: {data['uts']}")
        print(f"Nilai UAS: {data['uas']}")
        print(f"Nilai Akhir: {data['nilai_akhir']:.2f}")
    else:
        print("NIM tidak ditemukan.")

# Fungsi utama
def main():
    while True:
        tampilkan_menu()
        pilihan = input("[(L)ihat,(T)ambah,(U)bah,(H)apus,(C)ari,(K)eluar]:")
        
        if pilihan == "t":
            tambah_data()
        elif pilihan == "u":
            ubah_data()
        elif pilihan == "h":
            hapus_data()
        elif pilihan == "l":
            tampilkan_data()
        elif pilihan == "c":
            cari_data()
        elif pilihan == "k":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()
