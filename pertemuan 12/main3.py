from prettytable import PrettyTable

class ProdukOlahraga:
    def __init__(self, nama, harga):
        self.nama = nama
        self._harga = harga

    def get_nama(self):
        return self.nama

    def get_harga(self):
        return self._harga

    def tampilkan_info(self):
        return f"{self.nama} - Rp {self._harga}"

class Pakaian(ProdukOlahraga):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self.ukuran = ukuran

    def get_ukuran(self):
        return self.ukuran

    def tampilkan_info(self):
        return super().tampilkan_info() + f", Ukuran: {self.ukuran}"

class Baju(Pakaian):
    def __init__(self, nama, harga, ukuran, jenis):
        super().__init__(nama, harga, ukuran)
        self.jenis = jenis

    def get_jenis(self):
        return self.jenis

    def tampilkan_info(self):
        return super().tampilkan_info() + f", Jenis: {self.jenis}"

class Celana(Pakaian):
    def __init__(self, nama, harga, ukuran, model):
        super().__init__(nama, harga, ukuran)
        self._model = model

    def get_model(self):
        return self._model

    def tampilkan_info(self):
        return super().tampilkan_info() + f", Model: {self._model}"

class Sepatu(ProdukOlahraga):
    def __init__(self, nama, harga, ukuran_sepatu):
        super().__init__(nama, harga)
        self.ukuran_sepatu = ukuran_sepatu

    def get_ukuran_sepatu(self):
        return self.ukuran_sepatu

    def tampilkan_info(self):
        return super().tampilkan_info() + f", Ukuran Sepatu: {self.ukuran_sepatu}"

class TopiOlahraga(ProdukOlahraga):
    def __init__(self, nama, harga, merk):
        super().__init__(nama, harga)
        self.merk = merk

    def get_merk(self):
        return self.merk

    def tampilkan_info(self):
        return super().tampilkan_info() + f", Merk: {self.merk}"

class KacamataOlahraga(ProdukOlahraga):
    def __init__(self, nama, harga, warna_lensa):
        super().__init__(nama, harga)
        self.warna_lensa = warna_lensa

    def get_warna_lensa(self):
        return self.warna_lensa

    def tampilkan_info(self):
        return super().tampilkan_info() + f", Warna Lensa: {self.warna_lensa}"

class PrettyTableExtended(PrettyTable):
    def items_jadi_baris(self, items):
        for item in items:
            if isinstance(item, ProdukOlahraga):
                self.add_row([item.get_nama(), item.get_harga(), getattr(item, 'ukuran', '')])
            else:
                self.add_row([item.get_nama(), "", ""])

def hitung_diskon(jumlah_item):
    if jumlah_item == 2:
        return 0.1
    elif jumlah_item == 3:
        return 0.2
    elif jumlah_item == 4:
        return 1.0  
    else:
        return 0.0  

def tampilkan_item_tersedia(produk_list):
    print("========== Selamat Datang Di Toko Jaya Empire ==========")
    print("Anda Belanja Kami Bahagia")
    print("Pilih kategori produk:")
    print("1. Baju")
    print("2. Celana")
    print("3. Sepatu")
    print("4. Topi")
    print("5. Kacamata")

def tampilkan_item_kategori(produk_list, kategori):
    t = PrettyTable()
    t.field_names = ["No", "Nama Produk", "Harga", "Ukuran"]

    print(f"\nProduk dalam kategori {kategori}:")
    for i, produk in enumerate(produk_list, start=1):
        if kategori.lower() in produk.get_nama().lower():
            if isinstance(produk, ProdukOlahraga):
                t.add_row([i, produk.get_nama(), produk.get_harga(), getattr(produk, 'ukuran', '')])
            else:
                t.add_row([i, produk.get_nama(), "", ""])

    print(t)

def main():
    produk_list = [
        Baju("Baju Olahraga", 250000, "L", "Kaos"),
        Baju("Baju Kaos", 200000, "M", "Kaos"),
        Celana("Celana Cargo", 300000, "XL", "Jogger Pants"),
        Celana("Celana Jogger Pants", 350000, "S", "Jogger Pants"),
        Baju("Baju Kemeja Olahraga", 400000, "M", "Kemeja"),
        Baju("Baju Kaos Lengan Panjang", 450000, "L", "Kaos Lengan Panjang"),
        Pakaian("Baju Partai", 250000, "L"),
        Pakaian("Baju Kaos kerah", 200000, "M"),
        Pakaian("Celana Olahraga", 300000, "XL"),
        Pakaian("Celana Jogger Pants", 350000, "S"),
        Pakaian("Baju Kemeja Olahraga", 400000, "M"),
        Pakaian("Baju Kaos Lengan Panjang", 450000, "L"),
        Sepatu("Sepatu Lari", 500000, 42),
        Sepatu("Sepatu Basket", 700000, 44),
        Sepatu("Sepatu Super", 700000, 44),
        TopiOlahraga("Topi Baseball", 150000, "Nike"),
        TopiOlahraga("Topi Trucker", 180000, "Adidas"),
        KacamataOlahraga("Kacamata Rabun", 300000, "Hitam"),
        KacamataOlahraga("Kacamata Olahraga", 300000, "Hitam"),
        KacamataOlahraga("Kacamata Renang", 250000, "Biru")
    ]

    belanjaan_user = []

    while True:
        tampilkan_item_tersedia(produk_list)

        while True:
            nomor_kategori = int(input("\nMasukkan nomor kategori produk yang ingin dilihat: "))
            if 1 <= nomor_kategori <= 5:
                break
            else:
                print("Nomor kategori tidak valid. Silakan coba lagi.")
            

        if nomor_kategori == 1:
            kategori_dipilih = "Baju"
        elif nomor_kategori == 2:
            kategori_dipilih = "Celana"
        elif nomor_kategori == 3:
            kategori_dipilih = "Sepatu"
        elif nomor_kategori == 4:
            kategori_dipilih = "Topi"
        elif nomor_kategori == 5:
            kategori_dipilih = "Kacamata"

        tampilkan_item_kategori(produk_list, kategori_dipilih)

        while True:
            nomor_item = int(input("\nMasukkan nomor item yang ingin dibeli: "))
            if 1 <= nomor_item <= len(produk_list):
                break
            else:
                print("Nomor item tidak valid. Silakan coba lagi.")
            

        item_dipilih = produk_list[nomor_item - 1]
        belanjaan_user.append(item_dipilih)

        tambah_lagi = input("\nApakah Anda ingin menambah item lagi? (ya/tidak): ").lower()
        if tambah_lagi != 'ya':
            break

    total_harga = sum([item.get_harga() for item in belanjaan_user])
    jumlah_item = len(belanjaan_user)
    diskon = hitung_diskon(jumlah_item)
    total_harga_diskon = total_harga - (total_harga * diskon)

    print("\n--- Ringkasan Pembelian ---")
    
    t_ringkasan = PrettyTableExtended()
    t_ringkasan.field_names = ["Nama Produk", "Harga", "Ukuran"]
    t_ringkasan.items_jadi_baris(belanjaan_user)
    print(t_ringkasan)

    print("\nJumlah Item:", jumlah_item)
    print("Total Harga (Sebelum Diskon): Rp", total_harga)
    print("Diskon: {:.0%}".format(diskon))
    print("Total Harga yang harus dibayarkan (Setelah Diskon): Rp", total_harga_diskon)

    while True:
        try:
            uang_pembayaran = float(input("\nMasukkan jumlah uang pembayaran: Rp "))
            if uang_pembayaran >= total_harga_diskon:
                break
            else:
                print("Uang pembayaran kurang dari total harga. Silakan coba lagi.")
        except ValueError:
            print("Masukkan jumlah uang yang valid. Silakan coba lagi.")

    kembalian = uang_pembayaran - total_harga_diskon

    if kembalian >= 0:
        print("\n===================== Struk Pembelian =====================")
        
        t_struk = PrettyTableExtended()
        t_struk.field_names = ["Nama Produk", "Harga", "Ukuran"]
        t_struk.items_jadi_baris(belanjaan_user)
        print(t_struk)

        print(f"\nJumlah Item: {jumlah_item}")
        print(f"Total Harga: Rp {total_harga}")
        print(f"Diskon: {diskon * 100}%")
        print(f"Total Setelah Diskon: Rp {total_harga_diskon}")
        print(f"Uang Pembayaran: Rp {uang_pembayaran}")
        print("Kembalian: Rp", kembalian)
        print("Terima kasih atas Pembayarannya Sampai Jumpa Kembali ")
    else:
        print("Mohon maaf, uang pembayaran kurang sebesar Rp", abs(kembalian))

if __name__ == "__main__":
    main()
