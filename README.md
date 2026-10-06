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

   Bagian ini berisi data yang disiapkan sebagai dasar sebelum program GAMECLOUD dijalankan. Terdapat Dictionary akun yang menyimpan akun Admin dengan username admin, password admin123, dan role admin. Selanjutnya terdapat Tuple daftar_gamesewa yang berisi 7 game, yaitu GTA 7, Red Dead Redemption 5, Resident Evil: 17, Forza Horizon 9, EA SPORTS FC 29, NBA 2K29 Pro Edition, dan Assassin's Creed 9. Setelah itu terdapat Dictionary hargasewa yang menyimpan harga berdasarkan tiga pilihan durasi, yaitu key "1" dengan harga Rp10.000, key "2" dengan harga Rp60.000, dan key "3" dengan harga Rp180.000. Terakhir terdapat List datasewa = [] yang digunakan untuk menampung seluruh transaksi penyewaan yang dibuat selama program berjalan.

-Fungsi: Menyediakan data awal berupa akun, daftar game, harga sewa, dan tempat penyimpanan transaksi.

-Peran: Menjadi fondasi data yang digunakan oleh seluruh fitur GAMECLOUD.

---------------------------------------------

2. Input Validation dan Error Handling
  <img width="1582" height="1071" alt="Screenshot 2026-10-06 153121" src="https://github.com/user-attachments/assets/3ef99bb7-7889-4f0b-8934-0c4b03003819" />

   Bagian ini berisi tiga fungsi untuk mengatur input pengguna, yaitu input_nomor(), inputteks(), dan inputpassword(). Fungsi input_nomor(pesan, minimum, maksimum) digunakan untuk menerima input angka sesuai batas yang diberikan. Fungsi ini menggunakan while True agar pengguna dapat mencoba kembali ketika input salah, kemudian try digunakan untuk menjalankan proses konversi input menjadi integer. Jika angka berada di luar batas minimum dan maksimum, program menampilkan "Pilihan tidak tersedia!". Jika input bukan angka, ValueError ditangani dan program menampilkan "Input harus berupa angka!". Fungsi ini juga menangani KeyboardInterrupt dan EOFError dengan menampilkan "Input dibatalkan!" dan mengembalikan nilai 0. Selanjutnya inputteks(pesan) digunakan untuk input teks dan menggunakan .strip() untuk menghilangkan spasi di awal maupun akhir. Jika teks kosong, pengguna diminta memasukkan kembali data. Fungsi inputpassword(pesan) menggunakan pwinput.pwinput() agar password tidak ditampilkan secara langsung saat diketik dan juga menangani pembatalan input. Ketiga fungsi ini dibuat agar validasi input dapat digunakan berulang kali pada berbagai menu tanpa menulis proses validasi dari awal.

-Fungsi: Memvalidasi input angka, teks, dan password serta menangani kesalahan input.

-Peran: Menjaga program tetap berjalan ketika pengguna memberikan input yang salah dan menjadi penerapan Error Handling sebagai value-add.

---------------------------------------------

3. Fungsi Data
   
   <img width="1176" height="1149" alt="Screenshot 2026-10-06 155457" src="https://github.com/user-attachments/assets/267104b5-92ef-4e07-aece-7117d2c1f3f7" />

   <img width="1480" height="1352" alt="Screenshot 2026-10-06 155610" src="https://github.com/user-attachments/assets/c5392632-bce3-4b9b-91cd-12f4b728183f" />


    Bagian ini berisi beberapa fungsi untuk mendukung pengolahan data GAMECLOUD. buat_id() membuat ID transaksi secara acak menggunakan random.randint() dan mengecek agar ID tidak sama dengan data yang sudah ada. caridata() digunakan untuk mencari transaksi berdasarkan ID, sedangkan tampilkangame() menampilkan 7 game yang tersedia. tampilkandata() menampilkan data penyewaan menggunakan PrettyTable. Selanjutnya pilihgame() digunakan untuk memilih game, pilihdurasi() menentukan durasi sekaligus harga sewa, dan buat_datasewa(username) menggabungkan proses tersebut untuk membuat serta menyimpan transaksi baru ke datasewa.

-Fungsi: Mengatur pembuatan ID, pencarian dan penampilan data, pemilihan game dan durasi, serta pembuatan transaksi.

-Peran: Menjadi fungsi pendukung utama dalam proses penyewaan dan pengolahan data GAMECLOUD.

----------------------------------------------

4. Login dan Registrasi
   <img width="836" height="999" alt="Screenshot 2026-10-06 155621" src="https://github.com/user-attachments/assets/60f76d30-8080-4e26-aea5-c3c9f2db2f71" />

   Bagian ini berisi fungsi login() dan regis_user() yang mengatur akses pengguna ke dalam sistem. Fungsi login() menerima parameter role_login sehingga dapat digunakan untuk Login User maupun Login Admin. Prosesnya meliputi input username dan password, pengecekan username melalui akun.get(), pengecekan role akun, serta pemeriksaan password. Jika seluruh data sesuai, login berhasil dan username dikembalikan. Sementara itu, regis_user() digunakan untuk membuat akun User baru dengan memeriksa terlebih dahulu apakah username sudah digunakan, kemudian menyimpan username, password, dan role "user" ke dalam Dictionary akun.

-Fungsi: Mengatur proses login dan registrasi akun User.

-Peran: Menentukan identitas pengguna sekaligus membedakan hak akses User dan Admin.

----------------------------------------------

5. Fitur User
   <img width="1314" height="1295" alt="Screenshot 2026-10-06 160248" src="https://github.com/user-attachments/assets/a771f5b7-22f7-40d7-998b-bef84333d152" />

   <img width="1120" height="1135" alt="Screenshot 2026-10-06 160344" src="https://github.com/user-attachments/assets/7dfe2ddd-afb9-4d9d-a74f-731d937a9409" />

   Bagian ini berisi lihatpenyewaan_user() dan menu_user(). lihatpenyewaan_user() digunakan untuk menampilkan transaksi yang dimiliki User yang sedang login dengan mencocokkan username pada setiap data di datasewa. Sementara itu, menu_user() menggunakan while True dan menyediakan empat pilihan, yaitu Lihat Game, Sewa Game, Lihat Penyewaan Saya, dan Logout. Setiap pilihan akan memanggil fungsi yang sesuai, seperti tampilkangame(), buat_datasewa(username), dan lihatpenyewaan_user(username). Dengan username sebagai parameter, transaksi yang dibuat dapat langsung dikaitkan dengan User yang sedang login.

-Fungsi: Menyediakan fitur penyewaan dan pengelolaan informasi transaksi bagi User.

-Peran: Menjadi bagian sistem yang digunakan User untuk melihat game, melakukan penyewaan, melihat penyewaan sendiri, dan logout.

----------------------------------------------

6. CRUD Admin

   <img width="1629" height="833" alt="Screenshot 2026-10-06 160520" src="https://github.com/user-attachments/assets/424a09e9-168b-4343-8519-ca7eeed4390d" />

   Bagian ini berisi fungsi tambahdata_admin(), lihatdata_admin(), ubahdata_admin(), hapusdata_admin(), dan menucrud_admin(). tambahdata_admin() memungkinkan Admin membuat transaksi untuk User setelah username dan role User diperiksa. lihatdata_admin() menampilkan seluruh data penyewaan. ubahdata_admin() digunakan untuk mencari transaksi berdasarkan ID kemudian mengubah game, durasi, dan harga penyewaan. hapusdata_admin() mencari transaksi berdasarkan ID dan menghapusnya dari datasewa. Semua fungsi tersebut kemudian digabungkan melalui menucrud_admin() yang menyediakan pilihan Tambah, Lihat, Ubah, Hapus, dan Kembali.

-Fungsi: Menjalankan operasi Create, Read, Update, dan Delete pada data penyewaan.

-Peran: Memberikan Admin akses penuh untuk mengelola seluruh transaksi GAMECLOUD.

----------------------------------------------

7. Status Pembayaran Admin

   <img width="1473" height="1344" alt="Screenshot 2026-10-06 160541" src="https://github.com/user-attachments/assets/2b5e75f5-0ebe-43b7-8ee5-477ca8aa87a2" />

   Bagian ini berisi fungsi ubahstatus_pembayaran() yang digunakan Admin untuk mengatur status pembayaran suatu transaksi. Program terlebih dahulu memeriksa apakah terdapat data penyewaan. Jika data tersedia, seluruh transaksi ditampilkan dan Admin diminta memasukkan ID yang ingin diproses. ID tersebut dicari menggunakan caridata(). Setelah transaksi ditemukan, Admin diberikan pilihan Sudah Dibayar atau Belum Dibayar, kemudian nilai status pada Dictionary transaksi diperbarui sesuai pilihan. Setelah perubahan berhasil, data transaksi ditampilkan kembali agar hasil perubahan dapat dilihat.

-Fungsi: Mengubah status pembayaran berdasarkan ID transaksi.

-Peran: Mengelola informasi pembayaran yang nantinya digunakan dalam perhitungan pendapatan pada ringkasan.

----------------------------------------------

8. Ringkasan Admin

   <img width="1557" height="799" alt="Screenshot 2026-10-06 160605" src="https://github.com/user-attachments/assets/6307e515-a9c3-45c6-bb25-374317d2133e" />

   Bagian ini berisi fungsi ringkasan() yang digunakan untuk membuat rekap dari seluruh transaksi GAMECLOUD. Program menghitung jumlah seluruh penyewaan melalui len(datasewa), kemudian menggunakan variabel sudah_bayar, belum_bayar, dan pendapatan untuk menghitung jumlah transaksi berdasarkan status pembayaran serta total pendapatan. Setiap data diperiksa menggunakan for. Jika statusnya "Sudah Dibayar", jumlah pembayaran dan pendapatan akan bertambah sesuai harga transaksi, sedangkan transaksi lainnya dihitung sebagai belum dibayar. Setelah seluruh data selesai diperiksa, hasilnya ditampilkan menggunakan PrettyTable dengan informasi Total Penyewaan, Sudah Dibayar, Belum Dibayar, dan Pendapatan.

-Fungsi: Menghitung dan menampilkan rekap transaksi serta pendapatan GAMECLOUD.

-Peran: Membantu Admin memantau kondisi pembayaran dan jumlah pendapatan dari seluruh penyewaan.

----------------------------------------------

9. Menu Admin
    
<img width="1606" height="859" alt="Screenshot 2026-10-06 160620" src="https://github.com/user-attachments/assets/629870c7-4947-4947-b0c3-a5a94bd1a639" />

   Bagian ini berisi fungsi menu_admin(username) yang menjadi pusat navigasi bagi Admin setelah berhasil login. Menu dijalankan menggunakan while True sehingga Admin dapat menggunakan beberapa fitur dalam satu sesi. Terdapat empat pilihan, yaitu Kelola Data Penyewaan, Status Pembayaran, Ringkasan, dan Logout. Pilihan Kelola Data Penyewaan akan membuka menucrud_admin(), pilihan Status Pembayaran menjalankan ubahstatus_pembayaran(), sedangkan pilihan Ringkasan menjalankan ringkasan(). Jika memilih Logout, program menggunakan return untuk keluar dari menu Admin.

-Fungsi: Mengatur navigasi Admin menuju fitur-fitur pengelolaan GAMECLOUD.

-Peran: Menjadi pusat kontrol Admin untuk mengakses CRUD, status pembayaran, dan ringkasan.

----------------------------------------------

10. Program Utama
    
    <img width="1606" height="859" alt="Screenshot 2026-10-06 160620" src="https://github.com/user-attachments/assets/aba602ba-673a-4b3c-87d6-58e7c9014720" />

   Bagian ini berisi fungsi program() yang mengatur alur utama GAMECLOUD dari awal hingga program selesai. Program menggunakan while True untuk menampilkan menu utama secara berulang dengan empat pilihan, yaitu Login User, Login Admin, Registrasi User, dan Keluar. Login User akan menjalankan login("user") dan mengarahkan pengguna yang berhasil login ke menu_user(), sedangkan Login Admin menjalankan login("admin") dan mengarahkannya ke menu_admin(). Pilihan Registrasi menjalankan regis_user(), sementara pilihan Keluar menghentikan program menggunakan return. Pada bagian akhir, pemanggilan program() dibungkus dengan try-except untuk menangani KeyboardInterrupt dan EOFError sehingga program dapat dihentikan dengan lebih aman.

-Fungsi: Mengatur alur utama dari menu awal, login, registrasi, penggunaan fitur, hingga keluar dari program.

-Peran: Menjadi pengendali utama yang menghubungkan seluruh bagian GAMECLOUD menjadi satu sistem yang utuh.

----------------------------------------------

**OUTPUT : **


1. <img width="677" height="721" alt="Screenshot 2026-10-06 195344" src="https://github.com/user-attachments/assets/50102678-46f7-4cd9-93ae-219b40ca4bd0" />

Program dimulai dengan 4 menu utama, dimana seorang user wajib melakukan registrasi terlebih dahulu untuk login, kecuali admin.
Lalu user bisa login dan memasukkan username dan password yang sudah dibuat tadi.

----------------------------------------------


2. <img width="572" height="479" alt="Screenshot 2026-10-06 195424" src="https://github.com/user-attachments/assets/41de4de0-89f9-4f3c-9eb3-f767aebf0325" />

User bisa melihat daftar game apa saja yang disewakan dengan memilih menu 1.

----------------------------------------------


3. <img width="1015" height="1284" alt="Screenshot 2026-10-06 195445" src="https://github.com/user-attachments/assets/11728778-739e-41a0-97a4-fff184541545" />

User bisa memilih game yang ingin disewa dan memilih durasi penyewaaannya. User juga bisa melihat detail pesanannya.

----------------------------------------------


4. <img width="911" height="593" alt="Screenshot 2026-10-06 195544" src="https://github.com/user-attachments/assets/bdf76e56-d93c-4201-8213-818626046255" />

Login khusus yang diperuntukkan kepada admin untuk mengelola data penyewaan. Terdapat 4 Menu dan di menu 1 juga terdapat menu CRUD.

----------------------------------------------


5. <img width="1039" height="829" alt="Screenshot 2026-10-06 195632" src="https://github.com/user-attachments/assets/d42f6995-964a-430a-bba1-0e36d3fbf77a" />

Admin bisa menambahkan data sesuai dengan user yang ada.

----------------------------------------------

6. <img width="1039" height="829" alt="Screenshot 2026-10-06 195632" src="https://github.com/user-attachments/assets/396674ce-34dc-4f51-a081-20e67c183e16" />

Admin bisa melihat data apa saja yang sudeh terinput dengan memilih menu 2.

----------------------------------------------

7. <img width="1216" height="1219" alt="Screenshot 2026-10-06 195716" src="https://github.com/user-attachments/assets/f0cfc923-c074-4c77-b238-a57f5a9b2baa" />

Admin bisa mengupdate dan merubah data penyewa sesuai dengan ID meraka.

----------------------------------------------

8. <img width="1223" height="999" alt="Screenshot 2026-10-06 195740" src="https://github.com/user-attachments/assets/b82fbd64-ae37-41c7-bd79-b690a98514dd" />

Admin bisa menghapus data pengguna dengan memilih menu 4.

----------------------------------------------

9. <img width="1191" height="747" alt="Screenshot 2026-10-06 195813" src="https://github.com/user-attachments/assets/3bc58ea9-8b0b-4a5a-a38d-3656bea1d162" />

Admin bisa melakukan perubahan pada status pembayaran penyewa.

----------------------------------------------

10. <img width="1191" height="747" alt="Screenshot 2026-10-06 195813" src="https://github.com/user-attachments/assets/7b94e727-8261-468c-aacb-a4a47ecc9ce4" />

Admin bisa mengecek seluruh ringkasan total penyewaan.
