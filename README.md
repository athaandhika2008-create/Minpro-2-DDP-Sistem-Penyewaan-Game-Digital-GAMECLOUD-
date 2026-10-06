<div align="center">
 Mini Project 2 Dasar Dasar Pemrograman.
</div>
--------------------------------------------------------------------------------------------------------------------------------------------------------------


## Sistem Penyewaan Game Digital (GameCloud)

**Nama: Muhammad Atha Andhika**

**Nim: 2609116065**

**Kelas: B**

**Prodi: Sistem Informasi**



--------------------------------------------------------------------------------------------------------------------------------------------------------------
**-1. Alur Diagram (FlowChart)**


***-Main Menu***

<img width="1211" height="1400" alt="Minpro3 (2)-Main drawio" src="https://github.com/user-attachments/assets/6d04ed99-f9b1-4d1e-8f71-53e8fab71a36" />

.

***-User Menu (Konektor A)***

<img width="850" height="1604" alt="Minpro3 (2)-Menu User drawio" src="https://github.com/user-attachments/assets/282f9b0a-a519-425c-b6ef-ad0d7c606b02" />

.

***-Admin Menu (Konektor B)***

<img width="1829" height="2543" alt="Minpro3 (2)-Menu Admin drawio" src="https://github.com/user-attachments/assets/84b2c1dd-64d3-4d2a-87e8-28d0d63ab040" />

============================================================================================

**-2. Penjelasan Program**

1. Data Awal
<img width="1601" height="823" alt="Screenshot 2026-10-06 153102" src="https://github.com/user-attachments/assets/b45fc956-28f3-45d6-8437-aeec5adbf0d8" />

Bagian ini menyimpan data utama yang dipakai oleh program GAMECLOUD. Data tersebut meliputi akun pengguna yang disusun dalam bentuk dictionary berisi nama pengguna, kata sandi, serta hak akses, daftar game yang dapat disewa dalam bentuk tuple, rincian biaya berdasarkan durasi sewa dalam dictionary, hingga daftar penyewaan bertipe list untuk menampung seluruh riwayat transaksi.

- Fungsi: Menyediakan data awal dan struktur penyimpanan yang dibutuhkan oleh program untuk menjalankan proses akun, daftar game, harga sewa, dan data penyewaan.

- Peran: Menjadi dasar penyimpanan data GAMECLOUD yang digunakan oleh fitur User maupun Admin selama program berjalan.

---------------------------------------------

2. Input Validation dan Error Handling
  <img width="1582" height="1071" alt="Screenshot 2026-10-06 153121" src="https://github.com/user-attachments/assets/3ef99bb7-7889-4f0b-8934-0c4b03003819" />

  Bagian ini memuat beberapa fungsi penanganan masukan seperti input_nomor(), inputteks(), dan inputpassword() untuk memproses serta memvalidasi masukan dari pengguna. Fungsi input_nomor() memastikan batas angka pada menu pilihan tetap sesuai, inputteks() mencegah adanya isian kosong, sedangkan inputpassword() membaca kata sandi menggunakan pustaka pwinput. Penerapan blok try-except di bagian ini membantu menangkap kesalahan seperti ketidaksesuaian tipe data saat angka diharapkan.
  
- Fungsi: Memvalidasi input pengguna dan menangani kesalahan agar input yang tidak sesuai tidak langsung menyebabkan program berhenti.

- Peran: Menjadi sistem pengamanan input dalam GAMECLOUD sehingga setiap pilihan menu dan data yang dimasukkan pengguna dapat diperiksa sebelum diproses.

---------------------------------------------

3. Fungsi Data
   
   <img width="1176" height="1149" alt="Screenshot 2026-10-06 155457" src="https://github.com/user-attachments/assets/267104b5-92ef-4e07-aece-7117d2c1f3f7" />

   <img width="1480" height="1352" alt="Screenshot 2026-10-06 155610" src="https://github.com/user-attachments/assets/c5392632-bce3-4b9b-91cd-12f4b728183f" />


Bagian ini memuat fungsi buat_id(), caridata(), tampilkangame(), tampilkandata(), pilihgame(), pilihdurasi(), dan buat_datasewa() untuk mengelola data game serta transaksi. Seluruh fungsi tersebut menangani pembuatan kode identitas, pencarian entri, penayangan katalog game, penayangan riwayat penyewaan, pemilihan game dan durasi, hingga pendaftaran transaksi baru ke dalam daftar datasewa.

- Fungsi: Menangani proses pengolahan data yang dibutuhkan oleh fitur penyewaan dan pengelolaan data.

- Peran: Menjadi kumpulan function utama yang digunakan kembali oleh User dan Admin sehingga proses pengolahan data tidak perlu ditulis berulang kali.

----------------------------------------------

4. Login dan Registrasi
   <img width="836" height="999" alt="Screenshot 2026-10-06 155621" src="https://github.com/user-attachments/assets/60f76d30-8080-4e26-aea5-c3c9f2db2f71" />

   Bagian ini memuat fungsi login() dan regis_user() untuk mengatur akses akun GAMECLOUD. Pengecekan pada login() memanfaatkan variabel role_login untuk membedakan alur masuk antara User dan Admin, dilanjutkan dengan pemeriksaan nama pengguna, hak akses, serta kata sandi. Di sisi lain, regis_user() menangani pembuatan akun User baru melalui verifikasi nama pengguna dan kata sandi sebelum menyimpannya ke dalam dictionary akun.
   
- Fungsi: Menangani proses login berdasarkan role serta proses registrasi akun User.

- Peran: Menjadi sistem autentikasi GAMECLOUD yang membedakan hak akses User dan Admin sehingga masing-masing role mendapatkan menu dan proses yang sesuai.

----------------------------------------------

5. Fitur User
   <img width="1314" height="1295" alt="Screenshot 2026-10-06 160248" src="https://github.com/user-attachments/assets/a771f5b7-22f7-40d7-998b-bef84333d152" />

   <img width="1120" height="1135" alt="Screenshot 2026-10-06 160344" src="https://github.com/user-attachments/assets/7dfe2ddd-afb9-4d9d-a74f-731d937a9409" />

Bagian ini memuat fungsi lihatpenyewaan_user() dan menu_user() yang mengatur alur kerja setelah User berhasil masuk. Pilihan yang tersedia meliputi Lihat Game, Sewa Game, Lihat Penyewaan Saya, serta Logout. Melalui menu ini, User dapat mengecek daftar game, melakukan transaksi penyewaan lewat buat_datasewa(), serta memantau data penyewaan yang terhubung dengan nama akun yang sedang aktif.

- Fungsi: Menyediakan fitur yang dapat digunakan User untuk melihat game, melakukan penyewaan, dan melihat data penyewaannya sendiri.

- Peran: Menjadi bagian program yang menangani aktivitas User serta menjadi sumber data penyewaan yang nantinya dapat diakses dan dikelola oleh Admin melalui datasewa.

----------------------------------------------

6. CRUD Admin

   <img width="1629" height="833" alt="Screenshot 2026-10-06 160520" src="https://github.com/user-attachments/assets/424a09e9-168b-4343-8519-ca7eeed4390d" />

----------------------------------------------

7. Status Pembayaran Admin

   <img width="1473" height="1344" alt="Screenshot 2026-10-06 160541" src="https://github.com/user-attachments/assets/2b5e75f5-0ebe-43b7-8ee5-477ca8aa87a2" />

----------------------------------------------

8. Ringkasan Admin

   <img width="1557" height="799" alt="Screenshot 2026-10-06 160605" src="https://github.com/user-attachments/assets/6307e515-a9c3-45c6-bb25-374317d2133e" />

----------------------------------------------

9. Menu Admin
    
<img width="1606" height="859" alt="Screenshot 2026-10-06 160620" src="https://github.com/user-attachments/assets/629870c7-4947-4947-b0c3-a5a94bd1a639" />

----------------------------------------------

10. Program Utama
    
    <img width="1606" height="859" alt="Screenshot 2026-10-06 160620" src="https://github.com/user-attachments/assets/aba602ba-673a-4b3c-87d6-58e7c9014720" />


