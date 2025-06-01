# AlphaBot – Tugas Besar 1 IF2211 Strategi Algoritma

AlphaBot adalah bot yang dikembangkan untuk permainan Diamonds pada Tugas Besar 1 mata kuliah IF2211 Strategi Algoritma tahun ajaran 2024/2025. Bot ini menggunakan pendekatan algoritma greedy berbasis density untuk mengumpulkan diamond sebanyak-banyaknya dan menghindari risiko dalam permainan.

## 🧠 Penjelasan Singkat Algoritma Greedy

Bot mengambil keputusan berdasarkan nilai density, yaitu rasio antara nilai diamond dengan jarak terdekat menuju diamond tersebut.
Strategi utama AlphaBot meliputi:AlphaBot menggunakan algoritma **greedy berdasarkan density**, yaitu rasio antara nilai diamond dan jarak terdekat untuk mencapainya:
- Memilih diamond dengan density tertinggi (red diamond memiliki bobot 1.5×).
- Menghindari bot lawan untuk menghindari tackle.
- Menggunakan teleporter jika lebih efisien.
- Kembali ke base jika inventory penuh atau waktu hampir habis.
- Menuju tombol merah jika tidak ada diamond tersisa.
- Melakukan eksplorasi acak jika tidak ada opsi optimal.
Strategi ini memastikan bot mendapatkan poin sebanyak mungkin dengan tetap mempertimbangkan efisiensi dan keamanan.

Strategi ini bertujuan untuk memaksimalkan jumlah poin yang dikumpulkan dalam waktu terbatas dengan tetap memperhitungkan risiko.

---

## ⚙️ Requirement & Instalasi

### 1. Python
- Python >= 3.x
- Pastikan pip sudah tersedia


### 2. Instalasi Dependensi
Jalankan perintah berikut di direktori bot:

```bash
pip install requests dacite colorama
```

### 3. Node.js
- Dibutuhkan untuk menjalankan game engine (frontend + backend)

## 🚀 Langkah Menjalankan Program
### A. Menjalankan Game Engine
```bash
git clone https://github.com/yunioktasafitri/Tubes1_alphacode.git
cd tubes1-IF2211-game-engine
npm install
npm run build
```
Untuk menjalankan frontend visualisasi:
```bash
npm run start
```
### B. Menjalankan Bot
```bash
cd Tubes1_alpha-code
pip install requests dacite colorama
python src/main.py --name "AlphaBot" --email "alpha@bot.com" --password "123" --team "alpha-code"
```

### 👤 Author
- Yuni Okta Safitri - 123140213
- M. Zahran Dhiyaul Haq – 123140120

