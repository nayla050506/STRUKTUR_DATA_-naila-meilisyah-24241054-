# 1. Input nama customer dan tanggal belanja, simpan dalam tuple
nama = input("Masukkan nama customer: ")
tanggal = input("Masukkan tanggal belanja (contoh: 14-07-2025): ")
data_customer = (nama, tanggal)

# 2. Input jumlah barang yang akan dibeli
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

# 3. Input data tiap barang, simpan dalam dictionary
daftar_belanja = []  # 4. List untuk menyimpan semua dictionary barang

for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}")
    nama_barang = input("Nama barang: ")
    harga_satuan = float(input("Harga satuan: "))
    qty = int(input("Jumlah (QTY): "))
    
    # Membuat dictionary untuk barang ini
    barang = {
        "nama_barang": nama_barang,
        "harga_satuan": harga_satuan,
        "qty": qty,
        "total": harga_satuan * qty
    }
    
    daftar_belanja.append(barang)  # Menambahkan ke list

# 5. Tampilkan data customer, daftar belanja, dan total bayar
print("\n===== STRUK BELANJA =====")
print(f"Nama Customer : {data_customer[0]}")
print(f"Tanggal       : {data_customer[1]}")
print("\nDaftar Belanja:")

total_bayar = 0
for i, item in enumerate(daftar_belanja, start=1):
    print(f"{i}. {item['nama_barang']} - {item['qty']} x {item['harga_satuan']} = {item['total']}")
    total_bayar += item["total"]

print(f"\nTotal Bayar: Rp {total_bayar:,.2f}")