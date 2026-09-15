# ============================================================
# RAFFY HOSPITAL
# PENCATATAN DATA JADWAL DOKTER
# ============================================================


# ============================================================
# DATA AWAL
# ============================================================

data = [
    {
        "id": "DR-PD-001",
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
        "id": "DR-PD-002",
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
        "id": "DR-A-001",
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
        "id": "DR-O-001",
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
        "id": "DR-J-001",
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
        "id": "DR-S-001",
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
        "id": "DR-M-001",
        "nama": "Gita Permata",
        "gelar": "Sp.M",
        "poli": "Mata",
        "telp": "0215551009",
        "ruang": "M-801",
        "status": "Aktif",
        "hari": ["Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"],
        "jam": "15.00 - 21.00"
    }
]


# ============================================================
# DATA MASTER POLI
# ============================================================

# Menyimpan informasi setiap poli
poli_data = {
    "1": {
        "nama": "Penyakit Dalam",
        "gelar": "Sp.PD",
        "kode": "PD",
        "telp": "0215551001"
    },
    "2": {
        "nama": "Anak",
        "gelar": "Sp.A",
        "kode": "A",
        "telp": "0215551002"
    },
    "3": {
        "nama": "Bedah",
        "gelar": "Sp.B",
        "kode": "B",
        "telp": "0215551003"
    },
    "4": {
        "nama": "Obgyn",
        "gelar": "Sp.OG",
        "kode": "O",
        "telp": "0215551004"
    },
    "5": {
        "nama": "Jantung",
        "gelar": "Sp.JP",
        "kode": "J",
        "telp": "0215551005"
    },
    "6": {
        "nama": "Saraf",
        "gelar": "Sp.S",
        "kode": "S",
        "telp": "0215551006"
    },
    "7": {
        "nama": "Umum",
        "gelar": "dr.",
        "kode": "U",
        "telp": "0215551007"
    },
    "8": {
        "nama": "Gigi",
        "gelar": "drg.",
        "kode": "G",
        "telp": "0215551008"
    },
    "9": {
        "nama": "Mata",
        "gelar": "Sp.M",
        "kode": "M",
        "telp": "0215551009"
    },
    "10": {
        "nama": "THT",
        "gelar": "Sp.THT",
        "kode": "T",
        "telp": "0215551010"
    }
}


# ============================================================
# FUNCTION PILIH POLI
# ============================================================

def pilih_poli():
    # Menampilkan pilihan poli
    print("\n--- PILIH POLI ---")

    for nomor, poli in poli_data.items():
        print(f"{nomor}. {poli['nama']}")

    pilihan = input("Pilih poli: ").strip()

    # Mengecek pilihan
    if pilihan not in poli_data:
        print("Input tidak valid.")
        return None

    return poli_data[pilihan]


# ============================================================
# FUNCTION PILIH STATUS
# ============================================================

def pilih_status():
    # Menampilkan pilihan status
    print("\n--- PILIH STATUS ---")
    print("1. Aktif")
    print("2. Tidak Aktif")

    pilihan = input("Pilih status: ").strip()

    if pilihan == "1":
        return "Aktif"

    elif pilihan == "2":
        return "Tidak Aktif"

    else:
        print("Input tidak valid.")
        return None


# ============================================================
# FUNCTION PILIH HARI
# ============================================================

def pilih_hari():
    # Menyimpan pilihan hari
    hari_data = {
        "1": "Senin",
        "2": "Selasa",
        "3": "Rabu",
        "4": "Kamis",
        "5": "Jumat",
        "6": "Sabtu",
        "7": "Minggu"
    }

    print("\n--- PILIH HARI ---")

    for nomor, hari in hari_data.items():
        print(f"{nomor}. {hari}")

    pilihan = input("Pilih hari: ").strip()

    if pilihan not in hari_data:
        print("Input tidak valid.")
        return None

    return hari_data[pilihan]


# ============================================================
# FUNCTION PILIH 5 HARI
# ============================================================

def pilih_5_hari():
    # Menyimpan 5 hari yang dipilih
    hari_terpilih = []

    print("\n--- PILIH 5 HARI KERJA ---")

    for i in range(5):

        print(f"\nPilihan hari ke-{i + 1}")

        hari = pilih_hari()

        if hari is None:
            return None

        # Hari tidak boleh sama
        if hari in hari_terpilih:
            print("Hari sudah dipilih.")
            return None

        hari_terpilih.append(hari)

    return hari_terpilih


# ============================================================
# FUNCTION PILIH JAM
# ============================================================

def pilih_jam():
    # Menampilkan pilihan jam
    print("\n--- PILIH JADWAL JAM ---")
    print("1. 08.00 - 14.00")
    print("2. 15.00 - 21.00")

    pilihan = input("Pilih jadwal jam: ").strip()

    if pilihan == "1":
        return "08.00 - 14.00"

    elif pilihan == "2":
        return "15.00 - 21.00"

    else:
        print("Input tidak valid.")
        return None


# ============================================================
# FUNCTION CEK ID
# ============================================================

def cek_id(id_dokter):
    # Mengubah ID menjadi huruf besar
    id_dokter = id_dokter.upper()

    # Mengecek ID pada seluruh data
    for dokter in data:

        if dokter["id"].upper() == id_dokter:
            return True

    return False


# ============================================================
# FUNCTION BUAT ID OTOMATIS
# ============================================================

def buat_id(poli):
    # Mengambil kode poli
    kode = poli["kode"]

    nomor = 1

    while True:

        # Membuat ID berdasarkan kode poli
        id_baru = "DR-" + kode + "-" + str(nomor).zfill(3)

        # Memastikan ID tidak duplikat
        if cek_id(id_baru) == False:
            return id_baru

        nomor += 1


# ============================================================
# FUNCTION PILIH RUANG
# ============================================================

def pilih_ruang(poli, jam, id_lama=None):
    # Mengambil kode poli
    kode = poli["kode"]

    # Membuat 3 ruang berdasarkan kode poli
    ruang_data = [
        kode + "-001",
        kode + "-002",
        kode + "-003"
    ]

    ruang_tersedia = []

    print("\n--- PILIH RUANG ---")

    for ruang in ruang_data:

        jumlah_dokter = 0
        bentrok = False

        for dokter in data:

            # Saat update, data lama tidak dihitung
            if id_lama is not None:

                if dokter["id"].upper() == id_lama.upper():
                    continue

            # Hanya dokter aktif
            if dokter["status"] == "Aktif":

                # Poli dan ruang harus sama
                if dokter["poli"] == poli["nama"] and dokter["ruang"] == ruang:

                    jumlah_dokter += 1

                    # Shift yang sama tidak boleh
                    if dokter["jam"] == jam:
                        bentrok = True

        # Ruang maksimal untuk 2 dokter
        if jumlah_dokter < 2 and bentrok == False:
            ruang_tersedia.append(ruang)

    # Jika tidak ada ruang
    if len(ruang_tersedia) == 0:

        print("Tidak ada ruang yang tersedia.")
        return None

    # Menampilkan ruang
    for i in range(len(ruang_tersedia)):
        print(f"{i + 1}. {ruang_tersedia[i]}")

    pilihan = input("Pilih ruang: ").strip()

    if not pilihan.isdigit():
        print("Input tidak valid.")
        return None

    pilihan = int(pilihan)

    if pilihan < 1 or pilihan > len(ruang_tersedia):
        print("Input tidak valid.")
        return None

    return ruang_tersedia[pilihan - 1]


# ============================================================
# FUNCTION TAMPILKAN TABEL
# ============================================================

def tampilkan_tabel(data_tampil):
    # Jika data kosong
    if len(data_tampil) == 0:

        print("\nData tidak ditemukan.")
        return

    print("\n" + "=" * 150)

    print(
        f"{'ID':<12}"
        f"{'Nama Dokter':<22}"
        f"{'Gelar':<10}"
        f"{'Poli':<18}"
        f"{'Telp Poli':<15}"
        f"{'Ruang':<10}"
        f"{'Status':<15}"
        f"{'Jadwal Hari':<35}"
        f"{'Jadwal Jam':<20}"
    )

    print("=" * 150)

    for dokter in data_tampil:

        # Mengubah list hari menjadi string
        if isinstance(dokter["hari"], list):
            hari = ", ".join(dokter["hari"])
        else:
            hari = dokter["hari"]

        print(
            f"{dokter['id']:<12}"
            f"{dokter['nama']:<22}"
            f"{dokter['gelar']:<10}"
            f"{dokter['poli']:<18}"
            f"{dokter['telp']:<15}"
            f"{dokter['ruang']:<10}"
            f"{dokter['status']:<15}"
            f"{hari:<35}"
            f"{dokter['jam']:<20}"
        )

    print("=" * 150)


# ============================================================
# FUNCTION PILIH KRITERIA PENCARIAN
# ============================================================

def pilih_kriteria():
    # Menampilkan pilihan pencarian
    print("\n--- PILIH KRITERIA PENCARIAN ---")
    print("1. Berdasarkan Nama")
    print("2. Berdasarkan Poli")
    print("3. Berdasarkan Status")
    print("4. Berdasarkan Jadwal Hari")
    print("5. Berdasarkan Jadwal Jam")

    pilihan = input("Pilih kriteria: ").strip()

    if pilihan not in ["1", "2", "3", "4", "5"]:

        print("Input tidak valid.")
        return None

    return pilihan


# ============================================================
# FUNCTION CARI DATA
# ============================================================

def cari_data():
    # Memilih kriteria pencarian
    kriteria = pilih_kriteria()

    if kriteria is None:
        return None

    hasil = []

    # --------------------------------------------------------
    # BERDASARKAN NAMA
    # --------------------------------------------------------

    if kriteria == "1":

        nama = input("Masukkan nama dokter: ").strip().lower()

        if nama == "":
            print("Input tidak valid.")
            return None

        for dokter in data:

            # Mencari nama secara sebagian
            if nama in dokter["nama"].lower():
                hasil.append(dokter)

    # --------------------------------------------------------
    # BERDASARKAN POLI
    # --------------------------------------------------------

    elif kriteria == "2":

        poli = pilih_poli()

        if poli is None:
            return None

        for dokter in data:

            if dokter["poli"] == poli["nama"]:
                hasil.append(dokter)

    # --------------------------------------------------------
    # BERDASARKAN STATUS
    # --------------------------------------------------------

    elif kriteria == "3":

        status = pilih_status()

        if status is None:
            return None

        for dokter in data:

            if dokter["status"] == status:
                hasil.append(dokter)

    # --------------------------------------------------------
    # BERDASARKAN HARI
    # --------------------------------------------------------

    elif kriteria == "4":

        hari = pilih_hari()

        if hari is None:
            return None

        for dokter in data:

            if isinstance(dokter["hari"], list):

                if hari in dokter["hari"]:
                    hasil.append(dokter)

    # --------------------------------------------------------
    # BERDASARKAN JAM
    # --------------------------------------------------------

    elif kriteria == "5":

        jam = pilih_jam()

        if jam is None:
            return None

        for dokter in data:

            if dokter["jam"] == jam:
                hasil.append(dokter)

    # Mengembalikan hasil pencarian
    return hasil


# ============================================================
# FUNCTION READ
# ============================================================

def read():

    print("\n--- CARI DAN TAMPILKAN DATA JADWAL DOKTER ---")
    print("1. Tampilkan Seluruh Data")
    print("2. Cari Data")

    pilihan = input("Pilih menu: ").strip()

    # --------------------------------------------------------
    # TAMPILKAN SELURUH DATA
    # --------------------------------------------------------

    if pilihan == "1":

        # Konfirmasi dilakukan SEBELUM data ditampilkan
        konfirmasi = input(
            "\nApakah anda yakin ingin menampilkan seluruh data? (y/n): "
        ).strip().lower()

        if konfirmasi == "y":

            # Baru menampilkan hasil setelah konfirmasi
            print("\n--- SELURUH DATA DOKTER ---")
            tampilkan_tabel(data)

            # Afirmasi
            print("\nData berhasil ditampilkan.")

        elif konfirmasi == "n":

            print("\nProses dibatalkan.")

        else:

            print("\nInput tidak valid.")

    # --------------------------------------------------------
    # CARI DATA
    # --------------------------------------------------------

    elif pilihan == "2":

        # Mencari data terlebih dahulu tanpa menampilkan hasil
        hasil = cari_data()

        if hasil is None:
            return

        # Konfirmasi dilakukan sebelum hasil ditampilkan
        konfirmasi = input(
            "\nApakah anda yakin ingin menampilkan hasil pencarian? (y/n): "
        ).strip().lower()

        if konfirmasi == "y":

            # Baru menampilkan hasil setelah konfirmasi
            print("\n--- HASIL PENCARIAN ---")
            tampilkan_tabel(hasil)

            # Afirmasi
            print("\nHasil pencarian berhasil ditampilkan.")

        elif konfirmasi == "n":

            print("\nProses pencarian dibatalkan.")

        else:

            print("\nInput tidak valid.")

    # Input menu tidak valid
    else:

        print("\nInput tidak valid.")


# ============================================================
# FUNCTION CREATE
# ============================================================

def create():

    print("\n--- TAMBAH DATA JADWAL DOKTER ---")

    # Input nama dokter
    nama = input("Masukkan nama dokter: ").strip().title()

    if nama == "":
        print("Input tidak valid.")
        return

    # Pilih poli
    poli = pilih_poli()

    if poli is None:
        return

    # Status otomatis Aktif
    status = "Aktif"

    # Pilih jam
    jam = pilih_jam()

    if jam is None:
        return

    # Pilih ruang
    ruang = pilih_ruang(poli, jam)

    if ruang is None:
        return

    # Pilih 5 hari
    hari = pilih_5_hari()

    if hari is None:
        return

    # Membuat ID otomatis
    id_baru = buat_id(poli)

    # Membuat data dokter
    dokter_baru = {
        "id": id_baru,
        "nama": nama,
        "gelar": poli["gelar"],
        "poli": poli["nama"],
        "telp": poli["telp"],
        "ruang": ruang,
        "status": status,
        "hari": hari,
        "jam": jam
    }

    # Menampilkan data yang akan ditambahkan
    print("\n--- DATA YANG AKAN DITAMBAHKAN ---")
    tampilkan_tabel([dokter_baru])

    # Konfirmasi
    konfirmasi = input(
        "\nApakah anda yakin ingin menambah data berikut? (y/n): "
    ).strip().lower()

    if konfirmasi == "y":

        # Menambahkan data
        data.append(dokter_baru)

        # Afirmasi
        print("\nData berhasil ditambahkan.")

        # Menampilkan data setelah eksekusi
        print("\n--- DATA SETELAH DITAMBAHKAN ---")
        tampilkan_tabel([dokter_baru])

    elif konfirmasi == "n":

        print("\nProses tambah data dibatalkan.")

    else:

        print("\nInput tidak valid.")


# ============================================================
# FUNCTION UPDATE
# ============================================================

def update():

    print("\n--- UBAH DATA JADWAL DOKTER ---")

    # Mencari data berdasarkan kriteria
    hasil = cari_data()

    if hasil is None:
        return

    # Jika data tidak ditemukan
    if len(hasil) == 0:

        print("\nData tidak ditemukan.")
        return

    # --------------------------------------------------------
    # MENAMPILKAN HASIL PENCARIAN
    # --------------------------------------------------------

    print("\n--- DATA HASIL PENCARIAN ---")
    tampilkan_tabel(hasil)

    # --------------------------------------------------------
    # KONFIRMASI HASIL PENCARIAN
    # --------------------------------------------------------

    konfirmasi = input(
        "\nApakah anda yakin ingin menggunakan data hasil pencarian ini? (y/n): "
    ).strip().lower()

    if konfirmasi == "n":

        print("\nProses ubah data dibatalkan.")
        return

    elif konfirmasi != "y":

        print("\nInput tidak valid.")
        return

    # --------------------------------------------------------
    # MEMASUKKAN ID BERDASARKAN DATA YANG DITAMPILKAN
    # --------------------------------------------------------

    id_dokter = input(
        "\nMasukkan No. ID dokter yang ingin diubah: "
    ).strip().upper()

    # Mencari ID pada hasil pencarian
    dokter_lama = None

    for dokter in hasil:

        # ID tidak terpengaruh huruf besar/kecil
        if dokter["id"].upper() == id_dokter:

            dokter_lama = dokter
            break

    # Jika ID tidak ditemukan
    if dokter_lama is None:

        print("\nID tidak ditemukan pada data hasil pencarian.")
        return

    # --------------------------------------------------------
    # MENAMPILKAN DATA LAMA
    # --------------------------------------------------------

    print("\n--- DATA LAMA ---")
    tampilkan_tabel([dokter_lama])

    # --------------------------------------------------------
    # INPUT DATA BARU
    # --------------------------------------------------------

    nama_baru = input(
        "\nMasukkan nama dokter baru: "
    ).strip().title()

    if nama_baru == "":
        print("Input tidak valid.")
        return

    # Pilih poli baru
    poli_baru = pilih_poli()

    if poli_baru is None:
        return

    # Pilih status baru
    status_baru = pilih_status()

    if status_baru is None:
        return

    # --------------------------------------------------------
    # JIKA TIDAK AKTIF
    # --------------------------------------------------------

    if status_baru == "Tidak Aktif":

        ruang_baru = "-"
        hari_baru = "Tidak ada jadwal"
        jam_baru = "Tidak ada jadwal"

    # --------------------------------------------------------
    # JIKA AKTIF
    # --------------------------------------------------------

    else:

        # Pilih jam baru
        jam_baru = pilih_jam()

        if jam_baru is None:
            return

        # Pilih ruang baru
        ruang_baru = pilih_ruang(
            poli_baru,
            jam_baru,
            dokter_lama["id"]
        )

        if ruang_baru is None:
            return

        # Pilih 5 hari baru
        hari_baru = pilih_5_hari()

        if hari_baru is None:
            return

    # --------------------------------------------------------
    # MEMBUAT DATA BARU
    # --------------------------------------------------------

    dokter_baru = {
        # ID tetap menggunakan ID lama
        "id": dokter_lama["id"],
        "nama": nama_baru,
        "gelar": poli_baru["gelar"],
        "poli": poli_baru["nama"],
        "telp": poli_baru["telp"],
        "ruang": ruang_baru,
        "status": status_baru,
        "hari": hari_baru,
        "jam": jam_baru
    }

    # --------------------------------------------------------
    # MENAMPILKAN DATA YANG AKAN DIUBAH
    # --------------------------------------------------------

    print("\n--- DATA YANG AKAN DIUBAH ---")
    tampilkan_tabel([dokter_baru])

    # Konfirmasi perubahan
    konfirmasi = input(
        "\nApakah anda yakin ingin mengubah data berikut? (y/n): "
    ).strip().lower()

    if konfirmasi == "y":

        # Mengubah data lama
        dokter_lama["nama"] = dokter_baru["nama"]
        dokter_lama["gelar"] = dokter_baru["gelar"]
        dokter_lama["poli"] = dokter_baru["poli"]
        dokter_lama["telp"] = dokter_baru["telp"]
        dokter_lama["ruang"] = dokter_baru["ruang"]
        dokter_lama["status"] = dokter_baru["status"]
        dokter_lama["hari"] = dokter_baru["hari"]
        dokter_lama["jam"] = dokter_baru["jam"]

        # Afirmasi
        print("\nData berhasil diubah.")

        # Menampilkan data setelah diubah
        print("\n--- DATA SETELAH DIUBAH ---")
        tampilkan_tabel([dokter_lama])

    elif konfirmasi == "n":

        print("\nProses ubah data dibatalkan.")

    else:

        print("\nInput tidak valid.")


# ============================================================
# FUNCTION DELETE
# ============================================================

def delete():

    print("\n--- HAPUS DATA JADWAL DOKTER ---")

    # Mencari data berdasarkan kriteria
    hasil = cari_data()

    if hasil is None:
        return

    # Jika data tidak ditemukan
    if len(hasil) == 0:

        print("\nData tidak ditemukan.")
        return

    # --------------------------------------------------------
    # MENAMPILKAN HASIL PENCARIAN
    # --------------------------------------------------------

    print("\n--- DATA HASIL PENCARIAN ---")
    tampilkan_tabel(hasil)

    # --------------------------------------------------------
    # KONFIRMASI HASIL PENCARIAN
    # --------------------------------------------------------

    konfirmasi = input(
        "\nApakah anda yakin ingin menggunakan data hasil pencarian ini? (y/n): "
    ).strip().lower()

    if konfirmasi == "n":

        print("\nProses hapus data dibatalkan.")
        return

    elif konfirmasi != "y":

        print("\nInput tidak valid.")
        return

    # --------------------------------------------------------
    # MEMASUKKAN ID BERDASARKAN DATA YANG DITAMPILKAN
    # --------------------------------------------------------

    id_dokter = input(
        "\nMasukkan No. ID dokter yang ingin dihapus: "
    ).strip().upper()

    # Mencari dokter berdasarkan ID
    dokter_hapus = None

    for dokter in hasil:

        # ID tidak terpengaruh huruf besar/kecil
        if dokter["id"].upper() == id_dokter:

            dokter_hapus = dokter
            break

    # Jika ID tidak ditemukan
    if dokter_hapus is None:

        print("\nID tidak ditemukan pada data hasil pencarian.")
        return

    # --------------------------------------------------------
    # MENAMPILKAN DATA YANG AKAN DIHAPUS
    # --------------------------------------------------------

    print("\n--- DATA YANG AKAN DIHAPUS ---")
    tampilkan_tabel([dokter_hapus])

    # Konfirmasi penghapusan
    konfirmasi = input(
        "\nApakah anda yakin ingin menghapus data berikut? (y/n): "
    ).strip().lower()

    if konfirmasi == "y":

        # Menyimpan data sebelum dihapus
        data_terhapus = dokter_hapus.copy()

        # Menghapus data
        data.remove(dokter_hapus)

        # Afirmasi
        print("\nData berhasil dihapus.")

        # Menampilkan data yang telah dihapus
        print("\n--- DATA YANG TELAH DIHAPUS ---")
        tampilkan_tabel([data_terhapus])

    elif konfirmasi == "n":

        print("\nProses hapus data dibatalkan.")

    else:

        print("\nInput tidak valid.")


# ============================================================
# FUNCTION MAIN
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 50)
        print("             RAFFY HOSPITAL")
        print("    PENCATATAN DATA JADWAL DOKTER")
        print("=" * 50)

        print("1. Cari dan Tampilkan Data Jadwal Dokter")
        print("2. Tambah Data Jadwal Dokter")
        print("3. Ubah Data Jadwal Dokter")
        print("4. Hapus Data Jadwal Dokter")
        print("5. Keluar Program")

        pilihan = input("Pilih menu: ").strip()

        # READ
        if pilihan == "1":
            read()

        # CREATE
        elif pilihan == "2":
            create()

        # UPDATE
        elif pilihan == "3":
            update()

        # DELETE
        elif pilihan == "4":
            delete()

        # EXIT
        elif pilihan == "5":

            print("\nTerima kasih telah menggunakan Raffy Hospital.")
            print("Pencatatan Data Jadwal Dokter")
            print("Semoga layanan kami membantu Anda.")

            break

        # Menu tidak valid
        else:

            print("\nInput tidak valid.")


# ============================================================
# MENJALANKAN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()