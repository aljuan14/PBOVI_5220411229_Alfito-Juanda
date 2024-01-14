class PerpusItem:
    def __init__(self, judul, subjek):
        self.judul = judul
        self.subjek = subjek

    def lokasi_penyimpanan(self):
        pass

    def info(self):
        pass

    def penuhi_kriteria(self, kriteria):
        return self.judul.lower() == kriteria.lower()


class Buku(PerpusItem):
    def __init__(self, judul, subjek, isbn, pengarang, jumlah_halaman, ukuran):
        super().__init__(judul, subjek)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jumlah_halaman = jumlah_halaman
        self.ukuran = ukuran


class Majalah(PerpusItem):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issue = issue


class Dvd(PerpusItem):
    def __init__(self, judul, aktor, genre):
        # Tambahkan subjek="" untuk memperbaiki inisialisasi
        super().__init__(judul, subjek="")
        self.aktor = aktor
        self.genre = genre


class Katalog:
    def __init__(self):
        self.perpusitems = []

    def cari(self, kriteria):
        for perpusitem in self.perpusitems:
            if perpusitem.penuhi_kriteria(kriteria):
                return perpusitem
        return None

    def tambah(self, perpusitem):
        self.perpusitems.append(perpusitem)

    def hapus(self, perpusitem):
        self.perpusitems.remove(perpusitem)


class Pengarang:
    def __init__(self, nama):
        self.nama = nama


katalog = Katalog()
katalog.tambah(Buku("Janji", "Drama", "001", [
               Pengarang("Tere Liye")], 384, 10))

katalog.tambah(Dvd("ayam", "alif", "thriller"))

buku = katalog.cari("Janji")
dvd = katalog.cari("ayam")


if buku:
    print(f"ditemukan buku dengan judul: {buku.judul}")
else:
    print("Buku tidak ditemukan.")

if dvd:
    print(f"ditemukan dvd dengan judul: {dvd.judul}")
else:
    print("Dvd tidak ditemukan.")
