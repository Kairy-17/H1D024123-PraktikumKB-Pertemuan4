KNOWLEDGE_BASE = {
    "RAM Rusak/Kotor": {
        "gejala": ["PC menyala tapi layar blank", "Terdengar bunyi beep berulang", "Sering terjadi Blue Screen (BSOD)"],
        "solusi": "Cabut RAM, bersihkan pin emasnya dengan penghapus pensil secara perlahan, lalu pasang kembali di slot yang berbeda."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["PC sering mati mendadak saat main game", "Kipas casing berputar lemah", "PC tidak mau menyala sama sekali"],
        "solusi": "Periksa kabel power, atau coba ganti dengan PSU cadangan yang dayanya (Watt) mencukupi dan bersertifikat bagus."
    },
    "Overheat (Prosesor)": {
        "gejala": ["PC mati mendadak setelah beberapa menit menyala", "Kipas prosesor berisik/berputar sangat kencang", "Kinerja PC menjadi sangat lambat (throttling)"],
        "solusi": "Buka casing, bersihkan debu di heatsink, dan ganti thermal paste pada prosesor dengan yang baru."
    },
    "VGA/Artifak Bermasalah": {
        "gejala": ["Layar menampilkan garis-garis atau kotak warna-warni", "Driver grafis sering crash", "PC menyala tapi layar blank"],
        "solusi": "Pastikan kabel monitor terpasang erat ke port VGA. Jika menggunakan GPU eksternal, coba bersihkan pinnya atau update driver grafis."
    },
    "Hardisk/SSD Corrupt": {
        "gejala": ["Booting sangat lama atau stuck di logo", "Sering muncul pesan 'No Boot Device Found'", "Proses copy file sering error atau berhenti"],
        "solusi": "Lakukan pengecekan kesehatan storage menggunakan software seperti CrystalDiskInfo. Backup data penting dan bersiap ganti ke SSD baru."
    }
}

def main():
    print("=" * 60)
    print("   SISTEM PAKAR DIAGNOSIS KERUSAKAN KOMPUTER/LAPTOP   ")
    print("=" * 60)
    print("Silakan jawab pertanyaan berikut dengan (y/n) untuk mendiagnosis.\n")

    gejala_user = set()

    semua_gejala = set()
    for data in KNOWLEDGE_BASE.values():
        for gejala in data["gejala"]:
            semua_gejala.add(gejala)

    for i, gejala in enumerate(semua_gejala, 1):
        jawab = input(f"Apakah komputer Anda mengalami: {gejala}? (y/n): ").strip().lower()
        if jawab == 'y':
            gejala_user.add(gejala)

    print("\n" + "=" * 60)
    print("                    HASIL DIAGNOSIS                    ")
    print("=" * 60)

    kerusakan_ditemukan = False

    for nama_kerusakan, data in KNOWLEDGE_BASE.items():
        gejala_kerusakan = set(data["gejala"])
        
        if gejala_kerusakan.issubset(gejala_user):
            print(f"Jenis Kerusakan : {nama_kerusakan}")
            print(f"Solusi Singkat  : {data['solusi']}")
            print("-" * 60)
            kerusakan_ditemukan = True
            break  

    if not kerusakan_ditemukan:
        print("Hasil Diagnosis : Tidak Dapat Dikenali")
        print("Solusi Singkat  : Gejala yang Anda masukkan tidak cocok dengan database kami.")
        print("                  Cobalah untuk memeriksanya ke teknisi terdekat untuk pengecekan fisik.")
        print("-" * 60)

if __name__ == "__main__":
    main()