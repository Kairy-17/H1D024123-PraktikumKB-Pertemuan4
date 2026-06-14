# Pertemuan 4: Sistem Pakar Diagnosis Kerusakan Komputer

## 📝 Deskripsi Tugas
Tugas ini bertujuan untuk membangun sebuah program sistem pakar berbasis Python (Console) yang berfungsi untuk mendiagnosis jenis kerusakan pada perangkat keras maupun perangkat lunak komputer/laptop berdasarkan gejala-gejala fisik yang dimasukkan oleh pengguna.

## 🛠️ Kriteria & Fitur Program
Program ini dibangun dengan memenuhi standar kriteria praktikum sebagai berikut:
* **Knowledge Base (Basis Pengetahuan)**: Menyimpan informasi minimal 5 jenis kerusakan utama komputer, yaitu:
  1. RAM Rusak atau Kotor
  2. Power Supply Unit (PSU) Lemah
  3. Overheat pada Prosesor (CPU)
  4. VGA Bermasalah / Layar Artifak
  5. Hardisk atau SSD Corrupt
* **Mesin Inferensi Berbasis Kamus**: Aturan (*rules*) diagnosis disimpan menggunakan struktur data **Dictionary**, bukan sekadar menggunakan percabangan `if-else` berantai yang panjang.
* **Pattern Matching (Pencocokan Pola)**: Proses penarikan kesimpulan memanfaatkan fungsi subset himpunan (`set.issubset()`) untuk mencocokkan gejala inputan user dengan aturan secara dinamis.
* **Penanganan Kondisi Alternatif**: Program mampu mendeteksi dan menangani kondisi apabila kombinasi gejala yang dimasukkan oleh pengguna tidak cocok dengan jenis kerusakan apa pun di dalam database.
* **Output Dinamis**: Menampilkan nama kerusakan yang teridenteksi secara spesifik beserta rekomendasi solusi perbaikan singkatnya.

## 💻 Struktur Pengetahuan (Contoh Rule)
Sistem mengenali kerusakan melalui representasi gejala seperti:
* G01: Komputer sering restart sendiri
* G02: Muncul Blue Screen (BSOD)
* G03: Terdengar bunyi bip berulang saat dinyalakan

Jika inputan gejala memenuhi syarat aturan di dalam database, sistem akan langsung memberikan diagnosis yang tepat.

## 🚀 Cara Menjalankan Program

1. Buka terminal atau command prompt Anda.
2. Pastikan direktori terminal sudah mengarah ke folder tempat file script ini disimpan.
3. Jalankan perintah berikut:

```bash
python sistempakar.py
