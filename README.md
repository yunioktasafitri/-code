# Tubes 1 Strategi Algoritma – AlphaBot

Bot ini dibuat untuk Tugas Besar 1 mata kuliah IF2211 Strategi Algoritma tahun 2024/2025.

## Penjelasan Singkat Algoritma Greedy yang Diimplementasikan

AlphaBot menggunakan algoritma **greedy berdasarkan density**, yaitu rasio antara nilai diamond dan jarak terdekat untuk mencapainya:

### Strategi utama:
- Memprioritaskan diamond dengan density tertinggi (red diamond lebih diprioritaskan dengan bobot 1.5×)
- Menghindari posisi bot musuh untuk menghindari tackle
- Menggunakan teleporter jika jalurnya lebih efisien daripada jalur langsung
- Kembali ke base jika:
  - Inventory penuh
  - Waktu hampir habis dan masih membawa diamond
- Pergi ke tombol merah jika diamond di peta habis
- Melakukan eksplorasi fallback jika tidak ada langkah lain

Strategi ini bertujuan untuk memaksimalkan jumlah poin yang dikumpulkan dalam waktu terbatas dengan tetap memperhitungkan risiko.

---

## Requirement & Instalasi

### 1. Python
- Python versi **3.9 atau lebih baru**
- Pastikan `pip` sudah tersedia di environment

### 2. Install dependensi
Jalankan perintah berikut:

```bash
pip install requests dacite colorama

Node.js (untuk game engine)

Langkah Menjalankan Program
A. Jalankan Game Engine
git clone https://github.com/yunioktasafitri/Tubes1_alphacode.git
cd tubes1-IF2211-game-engine
npm install
npm run build

Jalankan frontend visualisasi:
npm run start

B. Jalankan Bot
cd Tubes1_alpha-code
pip3 install requests dacite colorama
python src/main.py --name "AlphaBot" --email "alpha@bot.com" --password "123" --team "alpha-code"

Author
M. Zahran Dhiyaul Haq – 123140120

