[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?style=flat)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?logo=github&color=%23F7DF1E)](https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python)
[![ISSN](https://img.shields.io/badge/ISSN-2686%E2%80%936099-blue.svg?logo=google-scholar&color=98FB98)](http://www.ejournal.upnjatim.ac.id/index.php/scan/article/view/2352)
![GitHub Star](https://img.shields.io/github/stars/devancakra/Bot-Inventaris-Tugas-Berbasis-Python.svg?color=FF69B4)
![GitHub Contributor](https://img.shields.io/github/contributors/devancakra/Bot-Inventaris-Tugas-Berbasis-Python.svg?color=FF8C00)
![GitHub last commit](https://img.shields.io/github/last-commit/devancakra/Bot-Inventaris-Tugas-Berbasis-Python)
![Python](https://img.shields.io/badge/-Python-blue.svg?style=flat&logo=python&logoColor=white)

# Bot-Telegram-Python-Inventaris-Tugas
<strong>Tugas Akhir ke-2 dalam Pemrograman API</strong><br>

Proyek ini sangat erat kaitannya dengan bot telegram, yang mana bot telegram sendiri memiliki peran penting dalam kegiatan belajar mengajar di kelas. Bot ini dapat melakukan inventarisasi tugas secara berkala. Bot ini dibangun dengan bantuan sebuah platform yang bernama ``` pythonanywhere ```. Pada proyek ini, pembuat program menggunakan ``` python versi 3.6 ``` karena dikenal memiliki kelebihan dalam sintaksis. Tujuan dari proyek ini adalah untuk membantu dosen atau guru dalam menginventarisir tugas-tugas siswanya dan mengantisipasi kesalahan yang mungkin terjadi yaitu lupa merekap, hal ini dikarenakan kesibukan aktivitas berkirim pesan dalam sebuah grup media sosial kelas, dalam hal ini telegram.

<br><br>

## Kebutuhan Proyek
| Bagian | Deskripsi |
| --- | --- |
| Fitur | Keyboard Balasan, Keyboard Sebaris, Pengendalian Masalah, Inventarisasi, Aktivitas Catatan Pengguna |
| Platform | Pythonanywhere |
| Pustaka | telebot, datetime |
| Kode | Python 3.6 |

<br><br>

## Kemampuan Bot
1. Terdapat pilihan menu yang dapat diakses dengan mengklik atau mengetik.<br><br>
   
2. Aplikasi ini juga dapat mendeteksi file atau dokumen yang masuk dan memberitahukan pengirimnya secara langsung.<br><br>
   
3. Kemampuan lain dari bot ini adalah dapat memberikan notifikasi kepada pemilik bot bahwa ada seseorang yang mengakses menu tertentu, sehingga pemilik bot dapat memantau pergerakan yang terjadi secara langsung.<br><br>
   
4. Bot ini dapat menyapa pengguna grup dan pengguna non-grup.<br><br>
   
5. Terdapat kontrol masalah dalam sistem, jika pesan tidak sesuai dengan perintah, maka akan dialihkan ke perintah ``` /help ```.

<br><br>

## Memulai
1. Unduh repositori ini dan ekstrak.<br><br>
   
2. Daftar ``` akun pythonanywhere ``` :

   <table><tr><td width="810">

   ```
   https://www.pythonanywhere.com/registration/register/beginner/
   ```

   </td></tr></table><br>
   
3. Masuk ``` akun pythonanywhere ```.<br><br>
   
4. Buat direktori baru pada ``` platform pythonanywhere ``` dengan mengklik ``` Files ``` yang ada di bagian atas -> Ketik di bagian ``` Directories ```: ``` KelasApi ``` -> Klik ``` New directory ```.<br><br>

5. Kemudian unggah ``` Bot-InventarisTugas.py ``` dengan mengklik tombol ``` Upload a file ```.<br><br>

6. Kembali ke halaman sebelumnya, yaitu di ``` /home/[pythonanywhere username] ``` -> Klik ``` Open Bash console here ```.<br><br>
  
7. Kemudian ketik ini di konsol secara bergantian:

   <table><tr><td width="810">

   ```python
   mkvirtualenv myvirtualenv --python=/usr/bin/python3
   ```   

   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/da359630-98c8-4742-a1d8-7a2f9beb282a">
   
   </td></tr></table><br>
   <table><tr><td width="810">
      
   ```python
   pip install pytelegrambotapi
   ```

   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/c452c0b8-38f6-4ca0-987d-01e28ef0c3be">

   </td></tr></table><br>
   <table><tr><td width="810">
      
   ```python
   pip install datetime
   ```

   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/e1ce9401-ac0d-4fff-8f93-8dbb89a893a9">
   
   </td></tr></table><br>
   <table><tr><td width="810">
      
   ```python
   cd KelasApi
   ```

   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/ba30f775-d385-4433-b8c5-a74b2086fc60">
   
   </td></tr></table><br>
   <table><tr><td width="810">

   ```bash
   python3 Bot-InventarisTugas.py
   ```

   <img width="810" src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/8391e6f8-de4b-4315-942a-4570385cc763">
   
   </td></tr></table><br>
   
8. Selamat menikmati [Selesai].

<br><br>

## Pengingat
• Perhatikan penulisan sintaks yang baik dan benar karena python peka terhadap huruf besar/kecil.

• Pastikan PC/Laptop Anda terhubung ke internet.

<br><br>

## Sorotan
<table>
<tr>
<th colspan="4">Bot Telegram</th>
</tr>
<tr>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/08217f59-1fc8-4721-a67c-4d604c4286e4" alt="TGbot-1"></td>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/9d5e906a-63a8-4913-97a3-1b86aabb9d0c" alt="TGbot-2"></td>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/9b684607-ca9f-4764-bf34-7ccd056fda0d" alt="TGbot-3"></td>
</tr>
<tr>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/cde5ec27-79ed-412e-9b4b-33d3062bc50b" alt="TGbot-4"></td>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/44b7d8f9-f3a2-42dc-a1b5-23ff54899062" alt="TGbot-5"></td>
<td width="280"><img src="https://github.com/devancakra/Bot-Inventaris-Tugas-Berbasis-Python/assets/54527592/ad0936cf-e162-42c0-a6d1-9a9ae192fbd4" alt="TGbot-6"></td>
</tr>
</table>

<br><br>

## Demonstrasi Aplikasi
Via Telegram: <a href="http://t.me/inventaristugas_bot">@inventaristugas_bot</a>

<br><br>

## Apresiasi
Jika anda merasa karya ini bermanfaat, dukunglah karya ini sebagai bentuk apresiasi kepada penulis dengan cara mengeklik tombol ``` ⭐Bintang ```.

<br><br>

## Penafian
Aplikasi ini dibuat dengan menyertakan sumber-sumber dari pihak ketiga. Pihak ketiga di sini adalah penyedia layanan, yang layanannya berupa pustaka, kerangka kerja, dan lain-lain. Saya ucapkan terima kasih banyak atas layanannya. Telah terbukti sangat membantu dan dapat diimplementasikan.

<br><br>

## LISENSI 
LISENSI MIT - Hak Cipta © 2020 - Devan Cakra Mudra Wijaya

Dengan ini diberikan izin tanpa biaya kepada siapa pun yang mendapatkan salinan perangkat lunak ini dan file dokumentasi terkait perangkat lunak untuk menggunakannya tanpa batasan, termasuk namun tidak terbatas pada hak untuk menggunakan, menyalin, memodifikasi, menggabungkan, mempublikasikan, mendistribusikan, mensublisensikan, dan/atau menjual salinan Perangkat Lunak ini, dan mengizinkan orang yang menerima Perangkat Lunak ini untuk dilengkapi dengan persyaratan berikut:

Pemberitahuan hak cipta di atas dan pemberitahuan izin ini harus menyertai semua salinan atau bagian penting dari Perangkat Lunak.

DALAM HAL APAPUN, PENULIS ATAU PEMEGANG HAK CIPTA DI SINI TETAP MEMILIKI HAK KEPEMILIKAN PENUH. PERANGKAT LUNAK INI DISEDIAKAN SEBAGAIMANA ADANYA, TANPA JAMINAN APAPUN, BAIK TERSURAT MAUPUN TERSIRAT, OLEH KARENA ITU JIKA TERJADI KERUSAKAN, KEHILANGAN, ATAU LAINNYA YANG TIMBUL DARI PENGGUNAAN ATAU URUSAN LAIN DALAM PERANGKAT LUNAK INI, PENULIS ATAU PEMEGANG HAK CIPTA TIDAK BERTANGGUNG JAWAB, KARENA PENGGUNAAN PERANGKAT LUNAK INI TIDAK DIPAKSAKAN SAMA SEKALI, SEHINGGA RISIKO ADALAH MILIK ANDA SENDIRI.
