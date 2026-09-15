<<<<<<< HEAD
# Tes 1
# /************************************/


# /===== Data Model =====/

# Menyimpan seluruh data dokter
data = [
    {
        "id": "DR-0001",
        "nama": "Andi Pratama",
        "gelar": "Sp.PD",
        "poli": "Penyakit Dalam",
        "telp": "0215551001",
        "ruang": "PD-001",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "jam": "08.00 - 14.00"
    },
    {
        "id": "DR-0002",
        "nama": "Budi Santoso",
        "gelar": "Sp.PD",
        "poli": "Penyakit Dalam",
        "telp": "0215551001",
        "ruang": "PD-001",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "jam": "15.00 - 21.00"
    },
    {
        "id": "DR-0003",
        "nama": "Citra Lestari",
        "gelar": "Sp.A",
        "poli": "Anak",
        "telp": "0215551002",
        "ruang": "A-101",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Kamis", "Sabtu"],
        "jam": "08.00 - 14.00"
    },
    {
        "id": "DR-0004",
        "nama": "Dina Maharani",
        "gelar": "Sp.OG",
        "poli": "Obgyn",
        "telp": "0215551004",
        "ruang": "O-301",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "jam": "15.00 - 21.00"
    },
    {
        "id": "DR-0005",
        "nama": "Eko Firmansyah",
        "gelar": "Sp.JP",
        "poli": "Jantung",
        "telp": "0215551005",
        "ruang": "J-401",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Jumat", "Sabtu"],
        "jam": "08.00 - 14.00"
    },
    {
        "id": "DR-0006",
        "nama": "Fajar Nugraha",
        "gelar": "Sp.S",
        "poli": "Saraf",
        "telp": "0215551006",
        "ruang": "-",
        "status": "Tidak Aktif",
        "hari": "Tidak ada jadwal",
        "jam": "Tidak ada jadwal"
    },
    {
        "id": "DR-0007",
        "nama": "Gita Permata",
        "gelar": "Sp.M",
        "poli": "Mata",
        "telp": "0215551009",
        "ruang": "M-801",
        "status": "Aktif",
        "hari": ["Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"],
        "jam": "14.00 - 20.00"
    }
]


# /===== Function Tambahan =====/


def pilih_poli():
    # Menampilkan 10 pilihan poli
    print("\n=== PILIH POLI ===")
    print("1. Penyakit Dalam")
    print("2. Anak")
    print("3. Bedah")
    print("4. Obgyn")
    print("5. Jantung")
    print("6. Saraf")
    print("7. Umum")
    print("8. Gigi")
    print("9. Mata")
    print("10. THT")

    # Menyimpan pilihan user
    pilihan = input("Pilih poli: ")

    # Data poli, gelar, kode ruang, dan telp
    daftar_poli = {
        "1": ("Penyakit Dalam", "Sp.PD", "PD", "0215551001"),
        "2": ("Anak", "Sp.A", "A", "0215551002"),
        "3": ("Bedah", "Sp.B", "B", "0215551003"),
        "4": ("Obgyn", "Sp.OG", "O", "0215551004"),
        "5": ("Jantung", "Sp.JP", "J", "0215551005"),
        "6": ("Saraf", "Sp.S", "S", "0215551006"),
        "7": ("Umum", "dr.", "U", "0215551007"),
        "8": ("Gigi", "drg.", "G", "0215551008"),
        "9": ("Mata", "Sp.M", "M", "0215551009"),
        "10": ("THT", "Sp.THT", "T", "0215551010")
    }

    # Mengambil data berdasarkan pilihan
    return daftar_poli.get(pilihan)


def pilih_status():
    # Menampilkan pilihan status
    print("\n=== PILIH STATUS ===")
    print("1. Aktif")
    print("2. Tidak Aktif")

    # Menyimpan pilihan user
    pilihan = input("Pilih status: ")

    # Mengembalikan status
    if pilihan == "1":
        return "Aktif"

    elif pilihan == "2":
        return "Tidak Aktif"

    return None


def pilih_hari():
    # Menampilkan pilihan hari
    print("\n=== PILIH HARI ===")
    print("1. Senin")
    print("2. Selasa")
    print("3. Rabu")
    print("4. Kamis")
    print("5. Jumat")
    print("6. Sabtu")
    print("7. Minggu")

    # Menyimpan pilihan user
    pilihan = input("Pilih hari: ")

    # Daftar hari
    daftar_hari = {
        "1": "Senin",
        "2": "Selasa",
        "3": "Rabu",
        "4": "Kamis",
        "5": "Jumat",
        "6": "Sabtu",
        "7": "Minggu"
    }

    # Mengembalikan hari
    return daftar_hari.get(pilihan)


def pilih_5_hari():
    # Menyimpan lima hari kerja
    hari_kerja = []

    print("\n=== PILIH 5 HARI KERJA ===")

    # User harus memilih tepat 5 hari
    for i in range(5):

        print("\nHari ke-", i + 1)

        # Memanggil pilihan hari
        hari = pilih_hari()

        # Mengecek pilihan
        if hari is None:
            return None

        # Mencegah hari yang sama
        if hari in hari_kerja:
            print("Data anda tidak valid. Hari sudah dipilih.")
            return None

        # Menambahkan hari ke list
        hari_kerja.append(hari)

    # Mengembalikan 5 hari
    return hari_kerja


def pilih_jam():
    # Menampilkan pilihan shift
    print("\n=== PILIH JADWAL JAM ===")
    print("1. 08.00 - 14.00")
    print("2. 15.00 - 21.00")

    # Menyimpan pilihan user
    pilihan = input("Pilih jadwal jam: ")

    # Daftar shift
    daftar_jam = {
        "1": "08.00 - 14.00",
        "2": "15.00 - 21.00"
    }

    # Mengembalikan jam
    return daftar_jam.get(pilihan)


def cek_id(id_dokter):
    # Mengecek apakah ID sudah digunakan
    for dokter in data:

        # Membandingkan ID
        if dokter["id"] == id_dokter:
            return True

    return False


def buat_id():
    # Membuat ID dokter secara otomatis
    nomor = 1

    # Mencari nomor ID yang belum digunakan
    while True:

        # Membuat ID seperti DR-0001
        id_baru = "DR-" + str(nomor).zfill(4)

        # Mengecek ID
        if not cek_id(id_baru):
            return id_baru

        # Menaikkan nomor
        nomor += 1


def pilih_ruang(poli, kode, hari, jam, id_lama=None):
    # Membuat 3 ruang berdasarkan kode poli
    if kode == "PD":
        daftar_ruang = ["PD-001", "PD-002", "PD-003"]

    elif kode == "A":
        daftar_ruang = ["A-101", "A-102", "A-103"]

    elif kode == "B":
        daftar_ruang = ["B-201", "B-202", "B-203"]

    elif kode == "O":
        daftar_ruang = ["O-301", "O-302", "O-303"]

    elif kode == "J":
        daftar_ruang = ["J-401", "J-402", "J-403"]

    elif kode == "S":
        daftar_ruang = ["S-501", "S-502", "S-503"]

    elif kode == "U":
        daftar_ruang = ["U-601", "U-602", "U-603"]

    elif kode == "G":
        daftar_ruang = ["G-701", "G-702", "G-703"]

    elif kode == "M":
        daftar_ruang = ["M-801", "M-802", "M-803"]

    elif kode == "T":
        daftar_ruang = ["T-901", "T-902", "T-903"]

    else:
        return None

    # Menyimpan ruang yang tersedia
    ruang_tersedia = []

    # Mengecek setiap ruang
    for ruang in daftar_ruang:

        # Menyimpan jumlah dokter dalam ruang
        jumlah = 0

        # Mengecek seluruh data dokter
        for dokter in data:

            # Melewati data lama saat update
            if dokter["id"] == id_lama:
                continue

            # Mengecek poli dan ruang yang sama
            if (
                dokter["poli"] == poli
                and dokter["ruang"] == ruang
                and dokter["status"] == "Aktif"
            ):

                jumlah += 1

                # Ruang tidak boleh memiliki shift yang sama
                if dokter["jam"] == jam:
                    jumlah = 2

        # Ruang tersedia jika belum penuh
        if jumlah < 2:

            # Mengecek kembali agar shift tidak sama
            bentrok = False

            for dokter in data:

                if dokter["id"] == id_lama:
                    continue

                if (
                    dokter["poli"] == poli
                    and dokter["ruang"] == ruang
                    and dokter["status"] == "Aktif"
                    and dokter["jam"] == jam
                ):
                    bentrok = True

            # Hanya masukkan ruang yang tidak bentrok
            if not bentrok:
                ruang_tersedia.append(ruang)

    # Jika tidak ada ruang
    if len(ruang_tersedia) == 0:
        print("\nTidak ada ruang yang tersedia.")
        return None

    # Menampilkan ruang yang tersedia
    print("\n=== RUANG TERSEDIA ===")

    for i in range(len(ruang_tersedia)):
        print(i + 1, ".", ruang_tersedia[i])

    # Memilih ruang
    pilihan = input("Pilih ruang: ")

    # Validasi pilihan
    if not pilihan.isdigit():
        return None

    pilihan = int(pilihan)

    # Mengecek nomor pilihan
    if pilihan < 1 or pilihan > len(ruang_tersedia):
        return None

    # Mengembalikan ruang
    return ruang_tersedia[pilihan - 1]


def tampilkan_tabel(hasil):
    # Menampilkan data dokter dalam tabel
    print("\n" + "=" * 150)

    # Menampilkan judul kolom
    print(
        f"{'ID':<10}"
        f"{'Nama Dokter':<22}"
        f"{'Gelar':<10}"
        f"{'Poli':<20}"
        f"{'Telp Poli':<15}"
        f"{'Ruang':<10}"
        f"{'Status':<15}"
        f"{'Jadwal Hari':<40}"
        f"{'Jadwal Jam'}"
    )

    print("-" * 150)

    # Menampilkan setiap dokter
    for dokter in hasil:

        # Jika hari berbentuk list
        if isinstance(dokter["hari"], list):

            # Menggabungkan hari menjadi satu teks
            hari = ", ".join(dokter["hari"])

        else:

            # Untuk dokter tidak aktif
            hari = dokter["hari"]

        # Menampilkan satu baris data
        print(
            f"{dokter['id']:<10}"
            f"{dokter['nama']:<22}"
            f"{dokter['gelar']:<10}"
            f"{dokter['poli']:<20}"
            f"{dokter['telp']:<15}"
            f"{dokter['ruang']:<10}"
            f"{dokter['status']:<15}"
            f"{hari:<40}"
            f"{dokter['jam']}"
        )

    print("=" * 150)


def cari_data():
    # Menampilkan pilihan pencarian
    print("\n=== CARI DATA ===")
    print("1. Berdasarkan Nama")
    print("2. Berdasarkan Poli")
    print("3. Berdasarkan Status")
    print("4. Berdasarkan Jadwal Hari")
    print("5. Berdasarkan Jadwal Jam")

    # Menyimpan pilihan pencarian
    pilihan = input("Pilih pencarian: ")

    # Menyimpan kata kunci
    kata = input("Masukkan kata kunci: ").strip().lower()

    # Menyimpan hasil pencarian
    hasil = []

    # Mengecek setiap dokter
    for dokter in data:

        # Cari berdasarkan nama
        if pilihan == "1":

            # Pencarian sebagian nama
            if kata in dokter["nama"].lower():
                hasil.append(dokter)

        # Cari berdasarkan poli
        elif pilihan == "2":

            if kata == dokter["poli"].lower():
                hasil.append(dokter)

        # Cari berdasarkan status
        elif pilihan == "3":

            if kata == dokter["status"].lower():
                hasil.append(dokter)

        # Cari berdasarkan hari
        elif pilihan == "4":

            if isinstance(dokter["hari"], list):

                for hari in dokter["hari"]:

                    if kata == hari.lower():
                        hasil.append(dokter)
                        break

            elif kata == dokter["hari"].lower():

                hasil.append(dokter)

        # Cari berdasarkan jam
        elif pilihan == "5":

            if kata == dokter["jam"].lower():
                hasil.append(dokter)

        else:

            print("Data anda tidak valid.")
            return []

    # Mengembalikan hasil
    return hasil


# /===== Feature Program =====/


def read():
    # Fitur mencari dan menampilkan data
    print("\n=== CARI DAN TAMPILKAN DATA JADWAL DOKTER ===")

    # Pilihan tampilan
    print("1. Tampilkan Seluruh Data")
    print("2. Cari Data")

    # Menyimpan pilihan user
    pilihan = input("Pilih menu: ")

    # Menampilkan seluruh data
    if pilihan == "1":

        # Konfirmasi
        yakin = input(
            "\nApakah anda yakin ingin menampilkan seluruh data? (y/n): "
        )

        if yakin.lower() != "y":
            print("Data anda tidak valid.")
            return

        # Mengecek data kosong
        if len(data) == 0:
            print("Belum ada data dokter.")
            return

        # Menampilkan data
        tampilkan_tabel(data)

        print("\nData di atas berhasil ditampilkan.")

    # Mencari data
    elif pilihan == "2":

        # Konfirmasi
        yakin = input(
            "\nApakah anda yakin ingin mencari data? (y/n): "
        )

        if yakin.lower() != "y":
            print("Data anda tidak valid.")
            return

        # Menjalankan pencarian
        hasil = cari_data()

        # Mengecek hasil
        if len(hasil) == 0:
            print("\nData tidak ditemukan.")
            return

        # Menampilkan hasil
        print("\n=== HASIL PENCARIAN ===")
        tampilkan_tabel(hasil)

        print("\nData di atas berhasil ditemukan.")

    else:

        print("Data anda tidak valid.")


def create():
    # Fitur menambah data jadwal dokter
    print("\n=== TAMBAH DATA JADWAL DOKTER ===")

    # User hanya mengetik nama
    nama = input("Nama dokter: ").strip().title()

    # Validasi nama
    if nama == "":
        print("Data anda tidak valid.")
        return

    # Memilih poli
    pilihan = pilih_poli()

    # Validasi poli
    if pilihan is None:
        print("Data anda tidak valid.")
        return

    # Mengambil data otomatis dari poli
    poli = pilihan[0]
    gelar = pilihan[1]
    kode = pilihan[2]
    telp = pilihan[3]

    # Status dokter baru otomatis aktif
    status = "Aktif"

    # Memilih 5 hari kerja
    hari = pilih_5_hari()

    # Validasi hari
    if hari is None:
        print("Data anda tidak valid.")
        return

    # Memilih shift
    jam = pilih_jam()

    # Validasi jam
    if jam is None:
        print("Data anda tidak valid.")
        return

    # Memilih ruang yang tersedia
    ruang = pilih_ruang(
        poli,
        kode,
        hari,
        jam
    )

    # Validasi ruang
    if ruang is None:
        print("Data anda tidak valid.")
        return

    # Membuat ID otomatis
    id_dokter = buat_id()

    # Membuat dictionary dokter baru
    dokter_baru = {
        "id": id_dokter,
        "nama": nama,
        "gelar": gelar,
        "poli": poli,
        "telp": telp,
        "ruang": ruang,
        "status": status,
        "hari": hari,
        "jam": jam
    }

    # Menampilkan data sebelum konfirmasi
    print("\n=== DATA YANG AKAN DITAMBAHKAN ===")
    tampilkan_tabel([dokter_baru])

    # Konfirmasi penambahan
    yakin = input(
        "\nApakah anda yakin ingin menambah data berikut? (y/n): "
    )

    if yakin.lower() != "y":
        print("Data anda tidak valid. Penambahan dibatalkan.")
        return

    # Menambahkan data ke list
    data.append(dokter_baru)

    # Afirmasi berhasil
    print("\nData berikut berhasil ditambahkan:")
    tampilkan_tabel([dokter_baru])


def update():
    # Fitur mengubah data jadwal dokter
    print("\n=== UBAH DATA JADWAL DOKTER ===")

    # Mencari data berdasarkan nama terlebih dahulu
    nama_cari = input(
        "Masukkan nama dokter yang ingin diubah: "
    ).strip().lower()

    # Menyimpan hasil nama
    hasil_nama = []

    # Mencari nama yang mengandung kata kunci
    for dokter in data:

        if nama_cari in dokter["nama"].lower():
            hasil_nama.append(dokter)

    # Mengecek hasil
    if len(hasil_nama) == 0:
        print("Data anda tidak valid. Dokter tidak ditemukan.")
        return

    # Menampilkan hasil nama
    print("\n=== HASIL PENCARIAN NAMA ===")
    tampilkan_tabel(hasil_nama)

    # Jika lebih dari satu, user memilih ID
    id_cari = input(
        "\nMasukkan ID dokter yang ingin diubah: "
    ).strip().upper()

    # Mencari dokter berdasarkan ID
    dokter = None

    for item in hasil_nama:

        if item["id"] == id_cari:
            dokter = item
            break

    # Validasi ID
    if dokter is None:
        print("Data anda tidak valid. ID tidak ditemukan.")
        return

    # Menampilkan data lama
    print("\n=== DATA LAMA ===")
    tampilkan_tabel([dokter])

    # Input nama baru
    nama = input("Nama dokter baru: ").strip().title()

    # Validasi nama
    if nama == "":
        print("Data anda tidak valid.")
        return

    # Memilih poli baru
    pilihan = pilih_poli()

    # Validasi poli
    if pilihan is None:
        print("Data anda tidak valid.")
        return

    # Mengambil data otomatis
    poli = pilihan[0]
    gelar = pilihan[1]
    kode = pilihan[2]
    telp = pilihan[3]

    # Memilih status
    status = pilih_status()

    # Validasi status
    if status is None:
        print("Data anda tidak valid.")
        return

    # Jika dokter aktif
    if status == "Aktif":

        # Memilih 5 hari
        hari = pilih_5_hari()

        if hari is None:
            print("Data anda tidak valid.")
            return

        # Memilih shift
        jam = pilih_jam()

        if jam is None:
            print("Data anda tidak valid.")
            return

        # Memilih ruang
        ruang = pilih_ruang(
            poli,
            kode,
            hari,
            jam,
            dokter["id"]
        )

        if ruang is None:
            print("Data anda tidak valid.")
            return

    else:

        # Dokter tidak aktif tidak memiliki ruang
        ruang = "-"

        # Dokter tidak aktif tidak memiliki jadwal
        hari = "Tidak ada jadwal"
        jam = "Tidak ada jadwal"

    # Menyiapkan data baru
    data_baru = {
        "id": dokter["id"],
        "nama": nama,
        "gelar": gelar,
        "poli": poli,
        "telp": telp,
        "ruang": ruang,
        "status": status,
        "hari": hari,
        "jam": jam
    }

    # Menampilkan perubahan
    print("\n=== DATA SETELAH DIUBAH ===")
    tampilkan_tabel([data_baru])

    # Konfirmasi perubahan
    yakin = input(
        "\nApakah anda yakin ingin mengubah data berikut? (y/n): "
    )

    if yakin.lower() != "y":
        print("Data anda tidak valid. Perubahan dibatalkan.")
        return

    # Mengubah data lama
    dokter["nama"] = nama
    dokter["gelar"] = gelar
    dokter["poli"] = poli
    dokter["telp"] = telp
    dokter["ruang"] = ruang
    dokter["status"] = status
    dokter["hari"] = hari
    dokter["jam"] = jam

    # Afirmasi berhasil
    print("\nData berikut berhasil diubah:")
    tampilkan_tabel([dokter])


def delete():
    # Fitur menghapus data jadwal dokter
    print("\n=== HAPUS DATA JADWAL DOKTER ===")

    # Mencari berdasarkan nama terlebih dahulu
    nama_cari = input(
        "Masukkan nama dokter yang ingin dihapus: "
    ).strip().lower()

    # Menyimpan hasil pencarian
    hasil_nama = []

    # Mencari nama yang mengandung kata kunci
    for dokter in data:

        if nama_cari in dokter["nama"].lower():
            hasil_nama.append(dokter)

    # Mengecek hasil
    if len(hasil_nama) == 0:
        print("Data anda tidak valid. Dokter tidak ditemukan.")
        return

    # Menampilkan hasil
    print("\n=== HASIL PENCARIAN NAMA ===")
    tampilkan_tabel(hasil_nama)

    # Meminta ID dokter
    id_cari = input(
        "\nMasukkan ID dokter yang ingin dihapus: "
    ).strip().upper()

    # Mencari dokter
    dokter = None

    for item in hasil_nama:

        if item["id"] == id_cari:
            dokter = item
            break

    # Validasi ID
    if dokter is None:
        print("Data anda tidak valid. ID tidak ditemukan.")
        return

    # Menampilkan data yang akan dihapus
    print("\n=== DATA YANG AKAN DIHAPUS ===")
    tampilkan_tabel([dokter])

    # Konfirmasi penghapusan
    yakin = input(
        "\nApakah anda yakin ingin menghapus data berikut? (y/n): "
    )

    if yakin.lower() != "y":
        print("Data anda tidak valid. Penghapusan dibatalkan.")
        return

    # Menyimpan data sebelum dihapus
    data_hapus = dokter.copy()

    # Menghapus data dari list
    data.remove(dokter)

    # Afirmasi berhasil
    print("\nData berikut berhasil dihapus:")
    tampilkan_tabel([data_hapus])


# /===== Main Program =====/


def main():
    # Fungsi utama program
    while True:

        # Judul program
        print("\n" + "=" * 60)
        print("              RAFFY HOSPITAL")
        print("       PENCATATAN DATA JADWAL DOKTER")
        print("=" * 60)

        # Menu utama
        print("1. Cari dan Tampilkan Data Jadwal Dokter")
        print("2. Tambah Data Jadwal Dokter")
        print("3. Ubah Data Jadwal Dokter")
        print("4. Hapus Data Jadwal Dokter")
        print("5. Keluar Program")

        # Input menu
        input_user = input("\nPilih menu: ")

        # Menjalankan fitur cari
        if input_user == "1":
            read()

        # Menjalankan fitur tambah
        elif input_user == "2":
            create()

        # Menjalankan fitur ubah
        elif input_user == "3":
            update()

        # Menjalankan fitur hapus
        elif input_user == "4":
            delete()

        # Keluar program
        elif input_user == "5":

            # Konfirmasi keluar
            yakin = input(
                "\nApakah anda yakin ingin keluar dari program? (y/n): "
            )

            if yakin.lower() == "y":

                # Pesan penutup
                print("\n" + "=" * 60)
                print(" Terima kasih telah menggunakan Raffy Hospital.")
                print(" Pencatatan Data Jadwal Dokter")
                print(" Semoga layanan kami membantu Anda.")
                print("=" * 60)

                # Menghentikan program
                break

            else:

                print("Data anda tidak valid.")

        else:

            # Jika menu tidak tersedia
            print("Data anda tidak valid.")


# Menjalankan fungsi main
if __name__ == "__main__":
=======
# /************************************/


# /===== Data Model =====/

# Menyimpan seluruh data dokter
data = [
    {
        "id": "DR-0001",
        "nama": "Andi Pratama",
        "gelar": "Sp.PD",
        "poli": "Penyakit Dalam",
        "telp": "0215551001",
        "ruang": "PD-001",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "jam": "08.00 - 14.00"
    },
    {
        "id": "DR-0002",
        "nama": "Budi Santoso",
        "gelar": "Sp.PD",
        "poli": "Penyakit Dalam",
        "telp": "0215551001",
        "ruang": "PD-001",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "jam": "15.00 - 21.00"
    },
    {
        "id": "DR-0003",
        "nama": "Citra Lestari",
        "gelar": "Sp.A",
        "poli": "Anak",
        "telp": "0215551002",
        "ruang": "A-101",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Kamis", "Sabtu"],
        "jam": "08.00 - 14.00"
    },
    {
        "id": "DR-0004",
        "nama": "Dina Maharani",
        "gelar": "Sp.OG",
        "poli": "Obgyn",
        "telp": "0215551004",
        "ruang": "O-301",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "jam": "15.00 - 21.00"
    },
    {
        "id": "DR-0005",
        "nama": "Eko Firmansyah",
        "gelar": "Sp.JP",
        "poli": "Jantung",
        "telp": "0215551005",
        "ruang": "J-401",
        "status": "Aktif",
        "hari": ["Senin", "Selasa", "Rabu", "Jumat", "Sabtu"],
        "jam": "08.00 - 14.00"
    },
    {
        "id": "DR-0006",
        "nama": "Fajar Nugraha",
        "gelar": "Sp.S",
        "poli": "Saraf",
        "telp": "0215551006",
        "ruang": "-",
        "status": "Tidak Aktif",
        "hari": "Tidak ada jadwal",
        "jam": "Tidak ada jadwal"
    },
    {
        "id": "DR-0007",
        "nama": "Gita Permata",
        "gelar": "Sp.M",
        "poli": "Mata",
        "telp": "0215551009",
        "ruang": "M-801",
        "status": "Aktif",
        "hari": ["Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"],
        "jam": "14.00 - 20.00"
    }
]


# /===== Function Tambahan =====/


def pilih_poli():
    # Menampilkan 10 pilihan poli
    print("\n=== PILIH POLI ===")
    print("1. Penyakit Dalam")
    print("2. Anak")
    print("3. Bedah")
    print("4. Obgyn")
    print("5. Jantung")
    print("6. Saraf")
    print("7. Umum")
    print("8. Gigi")
    print("9. Mata")
    print("10. THT")

    # Menyimpan pilihan user
    pilihan = input("Pilih poli: ")

    # Data poli, gelar, kode ruang, dan telp
    daftar_poli = {
        "1": ("Penyakit Dalam", "Sp.PD", "PD", "0215551001"),
        "2": ("Anak", "Sp.A", "A", "0215551002"),
        "3": ("Bedah", "Sp.B", "B", "0215551003"),
        "4": ("Obgyn", "Sp.OG", "O", "0215551004"),
        "5": ("Jantung", "Sp.JP", "J", "0215551005"),
        "6": ("Saraf", "Sp.S", "S", "0215551006"),
        "7": ("Umum", "dr.", "U", "0215551007"),
        "8": ("Gigi", "drg.", "G", "0215551008"),
        "9": ("Mata", "Sp.M", "M", "0215551009"),
        "10": ("THT", "Sp.THT", "T", "0215551010")
    }

    # Mengambil data berdasarkan pilihan
    return daftar_poli.get(pilihan)


def pilih_status():
    # Menampilkan pilihan status
    print("\n=== PILIH STATUS ===")
    print("1. Aktif")
    print("2. Tidak Aktif")

    # Menyimpan pilihan user
    pilihan = input("Pilih status: ")

    # Mengembalikan status
    if pilihan == "1":
        return "Aktif"

    elif pilihan == "2":
        return "Tidak Aktif"

    return None


def pilih_hari():
    # Menampilkan pilihan hari
    print("\n=== PILIH HARI ===")
    print("1. Senin")
    print("2. Selasa")
    print("3. Rabu")
    print("4. Kamis")
    print("5. Jumat")
    print("6. Sabtu")
    print("7. Minggu")

    # Menyimpan pilihan user
    pilihan = input("Pilih hari: ")

    # Daftar hari
    daftar_hari = {
        "1": "Senin",
        "2": "Selasa",
        "3": "Rabu",
        "4": "Kamis",
        "5": "Jumat",
        "6": "Sabtu",
        "7": "Minggu"
    }

    # Mengembalikan hari
    return daftar_hari.get(pilihan)


def pilih_5_hari():
    # Menyimpan lima hari kerja
    hari_kerja = []

    print("\n=== PILIH 5 HARI KERJA ===")

    # User harus memilih tepat 5 hari
    for i in range(5):

        print("\nHari ke-", i + 1)

        # Memanggil pilihan hari
        hari = pilih_hari()

        # Mengecek pilihan
        if hari is None:
            return None

        # Mencegah hari yang sama
        if hari in hari_kerja:
            print("Data anda tidak valid. Hari sudah dipilih.")
            return None

        # Menambahkan hari ke list
        hari_kerja.append(hari)

    # Mengembalikan 5 hari
    return hari_kerja


def pilih_jam():
    # Menampilkan pilihan shift
    print("\n=== PILIH JADWAL JAM ===")
    print("1. 08.00 - 14.00")
    print("2. 15.00 - 21.00")

    # Menyimpan pilihan user
    pilihan = input("Pilih jadwal jam: ")

    # Daftar shift
    daftar_jam = {
        "1": "08.00 - 14.00",
        "2": "15.00 - 21.00"
    }

    # Mengembalikan jam
    return daftar_jam.get(pilihan)


def cek_id(id_dokter):
    # Mengecek apakah ID sudah digunakan
    for dokter in data:

        # Membandingkan ID
        if dokter["id"] == id_dokter:
            return True

    return False


def buat_id():
    # Membuat ID dokter secara otomatis
    nomor = 1

    # Mencari nomor ID yang belum digunakan
    while True:

        # Membuat ID seperti DR-0001
        id_baru = "DR-" + str(nomor).zfill(4)

        # Mengecek ID
        if not cek_id(id_baru):
            return id_baru

        # Menaikkan nomor
        nomor += 1


def pilih_ruang(poli, kode, hari, jam, id_lama=None):
    # Membuat 3 ruang berdasarkan kode poli
    if kode == "PD":
        daftar_ruang = ["PD-001", "PD-002", "PD-003"]

    elif kode == "A":
        daftar_ruang = ["A-101", "A-102", "A-103"]

    elif kode == "B":
        daftar_ruang = ["B-201", "B-202", "B-203"]

    elif kode == "O":
        daftar_ruang = ["O-301", "O-302", "O-303"]

    elif kode == "J":
        daftar_ruang = ["J-401", "J-402", "J-403"]

    elif kode == "S":
        daftar_ruang = ["S-501", "S-502", "S-503"]

    elif kode == "U":
        daftar_ruang = ["U-601", "U-602", "U-603"]

    elif kode == "G":
        daftar_ruang = ["G-701", "G-702", "G-703"]

    elif kode == "M":
        daftar_ruang = ["M-801", "M-802", "M-803"]

    elif kode == "T":
        daftar_ruang = ["T-901", "T-902", "T-903"]

    else:
        return None

    # Menyimpan ruang yang tersedia
    ruang_tersedia = []

    # Mengecek setiap ruang
    for ruang in daftar_ruang:

        # Menyimpan jumlah dokter dalam ruang
        jumlah = 0

        # Mengecek seluruh data dokter
        for dokter in data:

            # Melewati data lama saat update
            if dokter["id"] == id_lama:
                continue

            # Mengecek poli dan ruang yang sama
            if (
                dokter["poli"] == poli
                and dokter["ruang"] == ruang
                and dokter["status"] == "Aktif"
            ):

                jumlah += 1

                # Ruang tidak boleh memiliki shift yang sama
                if dokter["jam"] == jam:
                    jumlah = 2

        # Ruang tersedia jika belum penuh
        if jumlah < 2:

            # Mengecek kembali agar shift tidak sama
            bentrok = False

            for dokter in data:

                if dokter["id"] == id_lama:
                    continue

                if (
                    dokter["poli"] == poli
                    and dokter["ruang"] == ruang
                    and dokter["status"] == "Aktif"
                    and dokter["jam"] == jam
                ):
                    bentrok = True

            # Hanya masukkan ruang yang tidak bentrok
            if not bentrok:
                ruang_tersedia.append(ruang)

    # Jika tidak ada ruang
    if len(ruang_tersedia) == 0:
        print("\nTidak ada ruang yang tersedia.")
        return None

    # Menampilkan ruang yang tersedia
    print("\n=== RUANG TERSEDIA ===")

    for i in range(len(ruang_tersedia)):
        print(i + 1, ".", ruang_tersedia[i])

    # Memilih ruang
    pilihan = input("Pilih ruang: ")

    # Validasi pilihan
    if not pilihan.isdigit():
        return None

    pilihan = int(pilihan)

    # Mengecek nomor pilihan
    if pilihan < 1 or pilihan > len(ruang_tersedia):
        return None

    # Mengembalikan ruang
    return ruang_tersedia[pilihan - 1]


def tampilkan_tabel(hasil):
    # Menampilkan data dokter dalam tabel
    print("\n" + "=" * 150)

    # Menampilkan judul kolom
    print(
        f"{'ID':<10}"
        f"{'Nama Dokter':<22}"
        f"{'Gelar':<10}"
        f"{'Poli':<20}"
        f"{'Telp Poli':<15}"
        f"{'Ruang':<10}"
        f"{'Status':<15}"
        f"{'Jadwal Hari':<40}"
        f"{'Jadwal Jam'}"
    )

    print("-" * 150)

    # Menampilkan setiap dokter
    for dokter in hasil:

        # Jika hari berbentuk list
        if isinstance(dokter["hari"], list):

            # Menggabungkan hari menjadi satu teks
            hari = ", ".join(dokter["hari"])

        else:

            # Untuk dokter tidak aktif
            hari = dokter["hari"]

        # Menampilkan satu baris data
        print(
            f"{dokter['id']:<10}"
            f"{dokter['nama']:<22}"
            f"{dokter['gelar']:<10}"
            f"{dokter['poli']:<20}"
            f"{dokter['telp']:<15}"
            f"{dokter['ruang']:<10}"
            f"{dokter['status']:<15}"
            f"{hari:<40}"
            f"{dokter['jam']}"
        )

    print("=" * 150)


def cari_data():
    # Menampilkan pilihan pencarian
    print("\n=== CARI DATA ===")
    print("1. Berdasarkan Nama")
    print("2. Berdasarkan Poli")
    print("3. Berdasarkan Status")
    print("4. Berdasarkan Jadwal Hari")
    print("5. Berdasarkan Jadwal Jam")

    # Menyimpan pilihan pencarian
    pilihan = input("Pilih pencarian: ")

    # Menyimpan kata kunci
    kata = input("Masukkan kata kunci: ").strip().lower()

    # Menyimpan hasil pencarian
    hasil = []

    # Mengecek setiap dokter
    for dokter in data:

        # Cari berdasarkan nama
        if pilihan == "1":

            # Pencarian sebagian nama
            if kata in dokter["nama"].lower():
                hasil.append(dokter)

        # Cari berdasarkan poli
        elif pilihan == "2":

            if kata == dokter["poli"].lower():
                hasil.append(dokter)

        # Cari berdasarkan status
        elif pilihan == "3":

            if kata == dokter["status"].lower():
                hasil.append(dokter)

        # Cari berdasarkan hari
        elif pilihan == "4":

            if isinstance(dokter["hari"], list):

                for hari in dokter["hari"]:

                    if kata == hari.lower():
                        hasil.append(dokter)
                        break

            elif kata == dokter["hari"].lower():

                hasil.append(dokter)

        # Cari berdasarkan jam
        elif pilihan == "5":

            if kata == dokter["jam"].lower():
                hasil.append(dokter)

        else:

            print("Data anda tidak valid.")
            return []

    # Mengembalikan hasil
    return hasil


# /===== Feature Program =====/


def read():
    # Fitur mencari dan menampilkan data
    print("\n=== CARI DAN TAMPILKAN DATA JADWAL DOKTER ===")

    # Pilihan tampilan
    print("1. Tampilkan Seluruh Data")
    print("2. Cari Data")

    # Menyimpan pilihan user
    pilihan = input("Pilih menu: ")

    # Menampilkan seluruh data
    if pilihan == "1":

        # Konfirmasi
        yakin = input(
            "\nApakah anda yakin ingin menampilkan seluruh data? (y/n): "
        )

        if yakin.lower() != "y":
            print("Data anda tidak valid.")
            return

        # Mengecek data kosong
        if len(data) == 0:
            print("Belum ada data dokter.")
            return

        # Menampilkan data
        tampilkan_tabel(data)

        print("\nData di atas berhasil ditampilkan.")

    # Mencari data
    elif pilihan == "2":

        # Konfirmasi
        yakin = input(
            "\nApakah anda yakin ingin mencari data? (y/n): "
        )

        if yakin.lower() != "y":
            print("Data anda tidak valid.")
            return

        # Menjalankan pencarian
        hasil = cari_data()

        # Mengecek hasil
        if len(hasil) == 0:
            print("\nData tidak ditemukan.")
            return

        # Menampilkan hasil
        print("\n=== HASIL PENCARIAN ===")
        tampilkan_tabel(hasil)

        print("\nData di atas berhasil ditemukan.")

    else:

        print("Data anda tidak valid.")


def create():
    # Fitur menambah data jadwal dokter
    print("\n=== TAMBAH DATA JADWAL DOKTER ===")

    # User hanya mengetik nama
    nama = input("Nama dokter: ").strip().title()

    # Validasi nama
    if nama == "":
        print("Data anda tidak valid.")
        return

    # Memilih poli
    pilihan = pilih_poli()

    # Validasi poli
    if pilihan is None:
        print("Data anda tidak valid.")
        return

    # Mengambil data otomatis dari poli
    poli = pilihan[0]
    gelar = pilihan[1]
    kode = pilihan[2]
    telp = pilihan[3]

    # Status dokter baru otomatis aktif
    status = "Aktif"

    # Memilih 5 hari kerja
    hari = pilih_5_hari()

    # Validasi hari
    if hari is None:
        print("Data anda tidak valid.")
        return

    # Memilih shift
    jam = pilih_jam()

    # Validasi jam
    if jam is None:
        print("Data anda tidak valid.")
        return

    # Memilih ruang yang tersedia
    ruang = pilih_ruang(
        poli,
        kode,
        hari,
        jam
    )

    # Validasi ruang
    if ruang is None:
        print("Data anda tidak valid.")
        return

    # Membuat ID otomatis
    id_dokter = buat_id()

    # Membuat dictionary dokter baru
    dokter_baru = {
        "id": id_dokter,
        "nama": nama,
        "gelar": gelar,
        "poli": poli,
        "telp": telp,
        "ruang": ruang,
        "status": status,
        "hari": hari,
        "jam": jam
    }

    # Menampilkan data sebelum konfirmasi
    print("\n=== DATA YANG AKAN DITAMBAHKAN ===")
    tampilkan_tabel([dokter_baru])

    # Konfirmasi penambahan
    yakin = input(
        "\nApakah anda yakin ingin menambah data berikut? (y/n): "
    )

    if yakin.lower() != "y":
        print("Data anda tidak valid. Penambahan dibatalkan.")
        return

    # Menambahkan data ke list
    data.append(dokter_baru)

    # Afirmasi berhasil
    print("\nData berikut berhasil ditambahkan:")
    tampilkan_tabel([dokter_baru])


def update():
    # Fitur mengubah data jadwal dokter
    print("\n=== UBAH DATA JADWAL DOKTER ===")

    # Mencari data berdasarkan nama terlebih dahulu
    nama_cari = input(
        "Masukkan nama dokter yang ingin diubah: "
    ).strip().lower()

    # Menyimpan hasil nama
    hasil_nama = []

    # Mencari nama yang mengandung kata kunci
    for dokter in data:

        if nama_cari in dokter["nama"].lower():
            hasil_nama.append(dokter)

    # Mengecek hasil
    if len(hasil_nama) == 0:
        print("Data anda tidak valid. Dokter tidak ditemukan.")
        return

    # Menampilkan hasil nama
    print("\n=== HASIL PENCARIAN NAMA ===")
    tampilkan_tabel(hasil_nama)

    # Jika lebih dari satu, user memilih ID
    id_cari = input(
        "\nMasukkan ID dokter yang ingin diubah: "
    ).strip().upper()

    # Mencari dokter berdasarkan ID
    dokter = None

    for item in hasil_nama:

        if item["id"] == id_cari:
            dokter = item
            break

    # Validasi ID
    if dokter is None:
        print("Data anda tidak valid. ID tidak ditemukan.")
        return

    # Menampilkan data lama
    print("\n=== DATA LAMA ===")
    tampilkan_tabel([dokter])

    # Input nama baru
    nama = input("Nama dokter baru: ").strip().title()

    # Validasi nama
    if nama == "":
        print("Data anda tidak valid.")
        return

    # Memilih poli baru
    pilihan = pilih_poli()

    # Validasi poli
    if pilihan is None:
        print("Data anda tidak valid.")
        return

    # Mengambil data otomatis
    poli = pilihan[0]
    gelar = pilihan[1]
    kode = pilihan[2]
    telp = pilihan[3]

    # Memilih status
    status = pilih_status()

    # Validasi status
    if status is None:
        print("Data anda tidak valid.")
        return

    # Jika dokter aktif
    if status == "Aktif":

        # Memilih 5 hari
        hari = pilih_5_hari()

        if hari is None:
            print("Data anda tidak valid.")
            return

        # Memilih shift
        jam = pilih_jam()

        if jam is None:
            print("Data anda tidak valid.")
            return

        # Memilih ruang
        ruang = pilih_ruang(
            poli,
            kode,
            hari,
            jam,
            dokter["id"]
        )

        if ruang is None:
            print("Data anda tidak valid.")
            return

    else:

        # Dokter tidak aktif tidak memiliki ruang
        ruang = "-"

        # Dokter tidak aktif tidak memiliki jadwal
        hari = "Tidak ada jadwal"
        jam = "Tidak ada jadwal"

    # Menyiapkan data baru
    data_baru = {
        "id": dokter["id"],
        "nama": nama,
        "gelar": gelar,
        "poli": poli,
        "telp": telp,
        "ruang": ruang,
        "status": status,
        "hari": hari,
        "jam": jam
    }

    # Menampilkan perubahan
    print("\n=== DATA SETELAH DIUBAH ===")
    tampilkan_tabel([data_baru])

    # Konfirmasi perubahan
    yakin = input(
        "\nApakah anda yakin ingin mengubah data berikut? (y/n): "
    )

    if yakin.lower() != "y":
        print("Data anda tidak valid. Perubahan dibatalkan.")
        return

    # Mengubah data lama
    dokter["nama"] = nama
    dokter["gelar"] = gelar
    dokter["poli"] = poli
    dokter["telp"] = telp
    dokter["ruang"] = ruang
    dokter["status"] = status
    dokter["hari"] = hari
    dokter["jam"] = jam

    # Afirmasi berhasil
    print("\nData berikut berhasil diubah:")
    tampilkan_tabel([dokter])


def delete():
    # Fitur menghapus data jadwal dokter
    print("\n=== HAPUS DATA JADWAL DOKTER ===")

    # Mencari berdasarkan nama terlebih dahulu
    nama_cari = input(
        "Masukkan nama dokter yang ingin dihapus: "
    ).strip().lower()

    # Menyimpan hasil pencarian
    hasil_nama = []

    # Mencari nama yang mengandung kata kunci
    for dokter in data:

        if nama_cari in dokter["nama"].lower():
            hasil_nama.append(dokter)

    # Mengecek hasil
    if len(hasil_nama) == 0:
        print("Data anda tidak valid. Dokter tidak ditemukan.")
        return

    # Menampilkan hasil
    print("\n=== HASIL PENCARIAN NAMA ===")
    tampilkan_tabel(hasil_nama)

    # Meminta ID dokter
    id_cari = input(
        "\nMasukkan ID dokter yang ingin dihapus: "
    ).strip().upper()

    # Mencari dokter
    dokter = None

    for item in hasil_nama:

        if item["id"] == id_cari:
            dokter = item
            break

    # Validasi ID
    if dokter is None:
        print("Data anda tidak valid. ID tidak ditemukan.")
        return

    # Menampilkan data yang akan dihapus
    print("\n=== DATA YANG AKAN DIHAPUS ===")
    tampilkan_tabel([dokter])

    # Konfirmasi penghapusan
    yakin = input(
        "\nApakah anda yakin ingin menghapus data berikut? (y/n): "
    )

    if yakin.lower() != "y":
        print("Data anda tidak valid. Penghapusan dibatalkan.")
        return

    # Menyimpan data sebelum dihapus
    data_hapus = dokter.copy()

    # Menghapus data dari list
    data.remove(dokter)

    # Afirmasi berhasil
    print("\nData berikut berhasil dihapus:")
    tampilkan_tabel([data_hapus])


# /===== Main Program =====/


def main():
    # Fungsi utama program
    while True:

        # Judul program
        print("\n" + "=" * 60)
        print("              RAFFY HOSPITAL")
        print("       PENCATATAN DATA JADWAL DOKTER")
        print("=" * 60)

        # Menu utama
        print("1. Cari dan Tampilkan Data Jadwal Dokter")
        print("2. Tambah Data Jadwal Dokter")
        print("3. Ubah Data Jadwal Dokter")
        print("4. Hapus Data Jadwal Dokter")
        print("5. Keluar Program")

        # Input menu
        input_user = input("\nPilih menu: ")

        # Menjalankan fitur cari
        if input_user == "1":
            read()

        # Menjalankan fitur tambah
        elif input_user == "2":
            create()

        # Menjalankan fitur ubah
        elif input_user == "3":
            update()

        # Menjalankan fitur hapus
        elif input_user == "4":
            delete()

        # Keluar program
        elif input_user == "5":

            # Konfirmasi keluar
            yakin = input(
                "\nApakah anda yakin ingin keluar dari program? (y/n): "
            )

            if yakin.lower() == "y":

                # Pesan penutup
                print("\n" + "=" * 60)
                print(" Terima kasih telah menggunakan Raffy Hospital.")
                print(" Pencatatan Data Jadwal Dokter")
                print(" Semoga layanan kami membantu Anda.")
                print("=" * 60)

                # Menghentikan program
                break

            else:

                print("Data anda tidak valid.")

        else:

            # Jika menu tidak tersedia
            print("Data anda tidak valid.")


# Menjalankan fungsi main
if __name__ == "__main__":
>>>>>>> b654990a8af144626f096f3b07d700c93bf4e31f
    main()