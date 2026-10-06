import random
import pwinput
from prettytable import PrettyTable

#1
akun = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    }
}

daftar_gamesewa = (
    "GTA 7",
    "Red Dead Redemption 5",
    "Resident Evil: 17",
    "Forza Horizon 9",
    "EA SPORTS FC 29",
    "NBA 2K29 Pro Edition",
    "Assassin's Creed 9"
)

hargasewa = {
    "1": 10000,
    "2": 60000,
    "3": 180000
}

datasewa = []

#2
def input_nomor(pesan, minimum, maksimum):
    while True:
        try:
            pilihan = int(input(pesan))
            if minimum <= pilihan <= maksimum:
                return pilihan
            print("Pilihan tidak tersedia!")
        except ValueError:
            print("Input harus berupa angka!")
        except (KeyboardInterrupt, EOFError):
            print("\nInput dibatalkan!")
            return 0

def inputteks(pesan):
    while True:
        try:
            teks = input(pesan).strip()
            if teks != "":
                return teks
            print("Input tidak boleh kosong!")
        except (KeyboardInterrupt, EOFError):
            print("\nInput dibatalkan!")
            return ""

def inputpassword(pesan):
    try:
        password = pwinput.pwinput(pesan)
        return password.strip()
    except (KeyboardInterrupt, EOFError):
        print("\nInput dibatalkan!")
        return ""

#3
def buat_id():
    while True:
        nomor = random.randint(1000, 9999)
        ada = False

        for data in datasewa:
            if data["id"] == nomor:
                ada = True
                break

        if ada == False:
            return nomor

def caridata(id_data):
    for data in datasewa:
        if data["id"] == id_data:
            return data
    return None

def tampilkangame():
    print("\n===== DAFTAR GAME =====")

    for i in range(len(daftar_gamesewa)):
        print(str(i + 1) + ". " + daftar_gamesewa[i])

def tampilkandata(data_list):
    if len(data_list) == 0:
        print("Belum ada data penyewaan!")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "ID", "Username", "Game", "Durasi", "Harga", "Pembayaran"
    ]

    for data in data_list:
        tabel.add_row([
            data["id"],
            data["username"],
            data["game"],
            data["durasi"],
            "Rp" + str(data["harga"]),
            data["status"]
        ])

    print(tabel)

def pilihgame():
    tampilkangame()

    pilihan = input_nomor(
        "Pilih game: ",
        1,
        len(daftar_gamesewa)
    )

    if pilihan == 0:
        return ""

    return daftar_gamesewa[pilihan - 1]

def pilihdurasi():
    print("\n1. 1 Hari - Rp.10.000")
    print("2. 1 Minggu - Rp.60.000")
    print("3, 1 Bulan - Rp.180.000")

    pilihan = input_nomor("Pilih durasi: ", 1, 3)

    if pilihan == 0:
        return "", 0
    
    if pilihan == 1:
        return "1 Hari", hargasewa["1"]
    
    elif pilihan == 2:
        return "1 Minggu", hargasewa["2"]
    
    else:
        return "1 Bulan", hargasewa["3"]

def buat_datasewa(username):
    game = pilihgame()

    if game == "":
        return False

    durasi, harga = pilihdurasi()
    if durasi == "":
        return False

    data_baru = {
        "id": buat_id(),
        "username": username,
        "game": game,
        "durasi": durasi,
        "harga": harga,
        "status": "Belum Dibayar"
    }

    datasewa.append(data_baru)

    print("\nData penyewaan berhasil ditambah!")
    tampilkandata([data_baru])

    return True

#4
def login(role_login):
    print("\n===== LOGIN " + role_login.upper() + "=====")

    username = inputteks("Username: ")
    if username == "":
        return ""

    password = inputpassword("Password: ")
    if password == "":
        return ""

    data_akun = akun.get(username)

    if data_akun is None:
        print("Username tidak ditemukan!")
        return ""

    if data_akun["role"] != role_login:
        print("Akun ini bukan akun " + role_login + ".")
        return ""

    if data_akun["password"] != password:
        print("Password salah!")
        return ""

    print("Login berhasil. Selamat datang, " + username + "!")
    return username

def regis_user():
    print("\n===== REGISTRASI USER =====")

    username = inputteks("Buat username: ")

    if username == "":
        return
    
    if username in akun:
        print("Username sudah digunakan!")
        return 

    password = inputpassword("Buat password: ")

    if password == "":
        return

    akun[username] = {
        "password": password,
        "role": "user"
    }

    print("Registrasi berhasil. Silahkan login sebagai user!")

#5
def lihatpenyewaan_user(username):
    data_user = []

    for data in datasewa:
        if data["username"] == username:
            data_user.append(data)

    print("\n===== PENYEWAAN SAYA =====")
    tampilkandata(data_user)

def menu_user(username):
    while True:
        print("\n===== MENU GAMECLOUD ======")
        print("1. Lihat Game")
        print("2. Sewa Game")
        print("3. Lihat Penyewaan Saya")
        print("4. Logout")

        pilihan = input_nomor("Pilih menu: ", 1, 4)

        if pilihan == 1:
            tampilkangame()

        elif pilihan == 2:
            buat_datasewa(username)

        elif pilihan == 3:
            lihatpenyewaan_user(username)

        elif pilihan == 4:
            print("Logout berhasil!")
            return

        elif pilihan == 0:
            return

def tambahdata_admin():
    print("\n===== TAMBAH DATA PENYEWAAN =====")

    username = inputteks("Username user: ")

    if username == "":
        return

    data_akun = akun.get(username)

    if data_akun is None or data_akun["role"] != "user":
        print("Username user tidak ditemukan!")
        return

    buat_datasewa(username)

def lihatdata_admin():
    print("\n===== SELURUH DATA PENYEWAAN =====")
    tampilkandata(datasewa)

def ubahdata_admin():
    print("\n===== UBAH DATA PENYEWAAN =====")

    if len(datasewa) == 0:
        print("Belum ada data penyewaan!")
        return

    tampilkandata(datasewa)

    id_data = input_nomor(
        "Masukkan ID yang ingin diubah: ",
        1000,
        9999
    )

    if id_data == 0:
        return

    data = caridata(id_data)

    if data is None:
        print("ID Penyewaan tidak ditemukan!")
        return

    print("\nData yang dipilih: ")
    tampilkandata([data])

    game = pilihgame()

    if game == "":
        return

    durasi, harga = pilihdurasi()

    if durasi == "":
        return

    data["game"] = game
    data["durasi"] = durasi
    data["harga"] = harga

    print("\nData penyewaan berhasil diubah!")
    tampilkandata([data])

def hapusdata_admin():
    print("\n===== HAPUS DATA PENYEWAAN =====")

    if len(datasewa) == 0:
        print("Belum ada data penyewaan!")
        return

    tampilkandata(datasewa)

    id_data = input_nomor(
        "Masukkan ID yang ingin dihapus: ",
        1000,
        9999
    )

    if id_data == 0:
        return

    data = caridata(id_data)

    if data is None:
        print("ID Penyewaan tidak ditemukan!")
        return

    datasewa.remove(data)

    print("Data penyewaan berhasil dihapus!")

#6
def menucrud_admin():
    while True:
        print("\n===== CRUD DATA PENYEWAAN =====")
        print("1. Tambah")
        print("2. Lihat")
        print("3. Ubah")
        print("4. Hapus")
        print("5. Kembali")

        pilihan = input_nomor("Pilih menu: ", 1, 5)

        if pilihan == 1:
            tambahdata_admin()

        elif pilihan == 2:
            lihatdata_admin()

        elif pilihan == 3:
            ubahdata_admin()

        elif pilihan == 4:
            hapusdata_admin()

        elif pilihan == 5 or pilihan == 0:
            return

#7
def ubahstatus_pembayaran():
    print("\n===== STATUS PEMBAYARAN =====")

    if len(datasewa) == 0:
        print("Belum ada data penyewaan!")
        return

    tampilkandata(datasewa)

    id_data = input_nomor(
        "Masukkan ID penyewaan: ",
        1000,
        9999
    )

    if id_data == 0:
        return

    data = caridata(id_data)

    if data is None:
        print("ID Penyewaan tidak ditemukan!")
        return

    print("\n1. Sudah Dibayar")
    print("2. Belum Dibayar")

    pilihan = input_nomor("Pilih status: ", 1, 2)

    if pilihan == 1:
        data["status"] = "Sudah Dibayar"

    elif pilihan == 2:
        data["status"] = "Belum Dibayar"

    else:
        return

    print("Status pembayaran berhasil diubah!")
    tampilkandata([data])

#8
def ringkasan():
    total = len(datasewa)
    sudah_bayar = 0
    belum_bayar = 0
    pendapatan = 0

    for data in datasewa:
        if data["status"] == "Sudah Dibayar":
            sudah_bayar += 1
            pendapatan += data["harga"]
        else:
            belum_bayar += 1

    print("\n===== RINGKASAN GAMECLOUD =====")

    tabel = PrettyTable()
    tabel.field_names = ["Keterangan", "Jumlah"]
    tabel.add_row(["Total Penyewaan", total])
    tabel.add_row(["Sudah Dibayar", sudah_bayar])
    tabel.add_row(["Belum Dibayar", belum_bayar])
    tabel.add_row(["Pendapatan", "Rp" + str(pendapatan)])

    print(tabel)

#9
def menu_admin(username):
    while True:
        print("\n===== MENU GAMECLOUD ADMIN =====")
        print("1. Kelola Data Penyewaan")
        print("2. Status Pembayaran")
        print("3. Ringkasan")
        print("4. Logout")

        pilihan = input_nomor("Pilih menu: ", 1, 4)

        if pilihan == 1:
            menucrud_admin()

        elif pilihan == 2:
            ubahstatus_pembayaran()

        elif pilihan == 3:
            ringkasan()
            
        elif pilihan == 4:
            print("Logout berhasil!")
            return
        
        elif pilihan == 0:
            return

#10
def program():
    while True:
        print("\n===== GAMECLOUD DIGITAL GAME RENTAL =====")
        print("1. Login User")
        print("2. Login Admin")
        print("3. Registrasi User")
        print("4. Keluar")

        pilihan = input_nomor("Pilih menu: ", 1, 4)

        if pilihan == 1:
            username = login("user")

            if username != "":
                menu_user(username)

        elif pilihan == 2:
            username = login("admin")

            if username != "":
                menu_admin(username)

        elif pilihan == 3:
            regis_user()

        elif pilihan == 4:
            print("Terima kasih telah menggunakan GAMECLOUD!")
            return

        elif pilihan == 0:
            return

try:
    program()

except KeyboardInterrupt:
    print("\n\nProgram Dihentikan.")

except EOFError:
    print("\n\nProgram Dihentikan.")