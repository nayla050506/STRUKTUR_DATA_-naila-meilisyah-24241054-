# Variabel global untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambahkan mahasiswa
def create():
    nama = input("Masukkan nama mahasiswa: ")
    data_mahasiswa.append(nama)
    print("Data berhasil ditambahkan.\n")

# Fungsi untuk menampilkan semua data mahasiswa
def read():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.\n")
    else:
        print("Daftar Mahasiswa:")
        for i, nama in enumerate(data_mahasiswa):
            print(f"{i}. {nama}")
        print()

# Fungsi untuk mengubah nama mahasiswa berdasarkan indeks
def update():
    read()
    try:
        index = int(input("Masukkan indeks mahasiswa yang ingin diubah: "))
        if 0 <= index < len(data_mahasiswa):
            nama_baru = input("Masukkan nama baru: ")
            data_mahasiswa[index] = nama_baru
            print("Data berhasil diperbarui.\n")
        else:
            print("Indeks tidak valid.\n")
    except ValueError:
        print("Masukkan angka yang valid.\n")

# Fungsi untuk menghapus data mahasiswa berdasarkan indeks
def delete():
    read()
    try:
        index = int(input("Masukkan indeks mahasiswa yang ingin dihapus: "))
        if 0 <= index < len(data_mahasiswa):
            del data_mahasiswa[index]
            print("Data berhasil dihapus.\n")
        else:
            print("Indeks tidak valid.\n")
    except ValueError:
        print("Masukkan angka yang valid.\n")

# Fungsi utama
def main():
    while True:
        print("Menu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            create()
        elif pilihan == "2":
            read()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            delete()
        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            exit()
        else:
            print("Pilihan tidak valid.\n")

# Menjalankan program
main()