[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# 💎 Etimo Diamonds 2 — AlphaBot Edition (IF211)

AlphaBot adalah bot strategi yang dikembangkan untuk berkompetisi dalam permainan Etimo Diamonds 2 – sebuah tantangan pemrograman berbasis papan di mana bot bersaing untuk mengumpulkan diamond sebanyak mungkin sebelum waktu habis.

🎓 Project ini dibuat sebagai bagian dari Tugas Besar mata kuliah IF211 – Strategi Algoritma pada Program Studi Teknik Informatika, Institut Teknologi Sumatera (ITERA).

📚 Referensi
-   [Spesifikasi Permainan](https://docs.google.com/document/d/13cbmMVXviyu8eKQ6heqgDzt4JNNMeAZO/edit)
-   [Panduan Awal Bermain Diamonds](https://docs.google.com/document/d/1L92Axb89yIkom0b24D350Z1QAr8rujvHof7-kXRAp7c/edit)

## Instalasi Dependens 🔨

1. Clone repositori ini dan pindah ke direktori root:
     ```
    git clone https://github.com/haziqam/tubes1-IF2110-bot-starter-pack.git
    cd ./tubes1-IF211-bot-starter-pack
     ```
    

2. Instal seluruh dependensi menggunakan pip:

    ```
    pip install -r requirements.txt
    ```

## 💻 Cara Menjalankan Bot

Menjalankan 1 Bot
### Menjalankan Beberapa Bot Sekaligus
#### Untuk Windows

    ```
    ./run-bots.bat
    ```

##### Untuk Linux / macOS

    ```
    ./run-bots.sh
    ```
## Note:
Pastikan Anda memberikan izin eksekusi pada file .sh terlebih dahulu:
    ```
   chmod +x run-bots.sh
    ```

#### ⚠️ Catatan Penting
-   Gunakan email dan nama yang unik untuk setiap bot saat menjalankan beberapa bot.
-   Email bisa sembarang selama formatnya valid (contoh: bot1@example.com).
-   Nama dan password tidak boleh mengandung spasi.

  ## 🤖 Tentang AlphaBot

AlphaBot menggunakan pendekatan strategi berbasis evaluasi posisi dan kepadatan diamond di sekitar papan. Bot akan mempertimbangkan jarak, skor diamond, serta posisi lawan untuk menentukan gerakan terbaik. Jika inventory penuh, bot secara otomatis akan kembali ke home base. Bot juga menghindari lawan jika memungkinkan dan dapat memanfaatkan fitur seperti teleporter dan red button.

## Credits

Repositori ini diadaptasi dari Etimo/diamonds2.

Sebagian kode telah dimodifikasi untuk menyesuaikan kebutuhan tugas mata kuliah IF211 Strategi Algoritma – Teknik Informatika ITERA.

©️ Hak cipta dan penghargaan sepenuhnya untuk Etimo.ub.com/Etimo)
