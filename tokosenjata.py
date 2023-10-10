import os
from prettytable import PrettyTable

senjata = PrettyTable()
senjata.header = False
senjata.border = False

senjata.field_names = ['id', 'nama_senjata', 'jenis_senjata', 'harga_senjata']
senjata.add_row([1, 'AK47', 'AR', 5000000])
senjata.add_row([2, 'AK74', 'AR', 7000000])
senjata.add_row([3, 'M16A4', 'AR', 15000000])
senjata.add_row([4, 'MP5', 'SMG', 8500000])

senjata_list = []

for row in senjata:
    senjata_list.append(list(row))

senjata_list = senjata.get_string().strip().split('\n')
senjata_list = [row.split() for row in senjata_list]

os.system('cls')

admin = ['superadmin', '1234']
pembeli = ['user', '1234']

data_akun = admin, pembeli
# ================================================================================

# Membaca Table
def baca_tabel():
    senjata = PrettyTable()
    senjata.field_names = ['id', 'nama_senjata', 'jenis_senjata', 'harga_senjata']
    for row in senjata_list:
        senjata.add_row(row)

    print(senjata)

# ================================================================================
# Menu Admin

# Menambahkan Senjata
def admin_tambah_senjata():
    id_senjata = int(senjata_list[-1][0])

    id_senjata_baru = id_senjata+1
    nama_senjata_baru = input('Masukkan Nama Senjata : ')
    jenis_senjata_baru = input('Masukkan Jenis Senjata : ')
    harga_senjata_baru = int(input('Masukkan Harga Senjata : '))

    senjata = PrettyTable()
    senjata.field_names = ['id', 'nama_senjata', 'jenis_senjata', 'harga_senjata']
    for row in senjata_list:
        senjata.add_row(row)

    senjata.add_row([id_senjata_baru ,nama_senjata_baru, jenis_senjata_baru, harga_senjata_baru])
    print('Data Berhasil Disimpan')

    print(senjata)

# Menghapus Senjata
def admin_hapus_senjata():
    hapus_senjata = int(input('Masukkan ID Senjata Yang Ingin Di Hapus : '))
    id_hapus = hapus_senjata-1
    senjata_list.pop(id_hapus)

    senjata = PrettyTable()
    senjata.field_names = ['id', 'nama_senjata', 'jenis_senjata', 'harga_senjata']
    for row in senjata_list:
        senjata.add_row(row)

    print(senjata)

# Mengedit Senjata
def admin_edit_senjata():
    edit_senjata = int(input('Masukkan ID Senjata Yang Ingin Di Edit : '))
    id_edit = edit_senjata-1

    id_senjata_edit = id_edit
    nama_senjata_edit = input('Masukkan Nama Senjata Baru : ')
    jenis_senjata_edit = input('Masukkan Jenis Senjata Baru : ')
    harga_senjata_edit = int(input('Masukkan Harga Senjata Baru : '))

    senjata_list[id_edit][0] = id_senjata_edit
    senjata_list[id_edit][1] = nama_senjata_edit
    senjata_list[id_edit][2] = jenis_senjata_edit
    senjata_list[id_edit][3] = harga_senjata_edit

    senjata = PrettyTable()
    senjata.field_names = ['id', 'nama_senjata', 'jenis_senjata', 'harga_senjata']
    for row in senjata_list:
        senjata.add_row(row)

    print(senjata)

    
# ================================================================================
# User

# Transaksi User
def transaksi_user():
    os.system('cls')

    senjata = PrettyTable()
    senjata.field_names = ['no', 'nama_senjata', 'jenis_senjata', 'harga_senjata']
    for row in senjata_list:
        senjata.add_row(row)

    print('======================= Katalog Kami =======================')
    print(senjata)
    print('=' * 60)

    no_senjata = int(input('Masukkan Nomor Senjata Yang Ingin Dibeli : '))
    pilihan_senjata = no_senjata-1

    jumlah = int(input(f'Anda Memilih : {senjata_list[pilihan_senjata][1]} seharga Rp. {senjata_list[pilihan_senjata][3]}. Masukkan Jumlah yang ingin dibeli : '))
    
    harga_senjata = int(senjata_list[pilihan_senjata][3])
    total_harga_senjata = harga_senjata * jumlah

    print('===================================')
    print(f'Senjata : {senjata_list[pilihan_senjata][1]}')
    print(f'Jumlah : {jumlah} Pucuk')
    print(f'Total Harga : Rp. {total_harga_senjata}')
    print('===================================')

    while True:
        konfirmasi = input('=========== Apakah Anda ingin Melakukan Transaksi? (Y/T) : ')
        if konfirmasi == 'Y' or konfirmasi == 'y':
            print('===================================')
            print(f'Senjata : {senjata_list[pilihan_senjata][1]}')
            print(f'Jumlah : {jumlah} Pucuk')
            print(f'Total Harga : Rp. {total_harga_senjata}')
            print('===================================')
            print('============= Terima Kasih Sudah Bertransaksi. =============')
            break
        elif konfirmasi == 'T' or konfirmasi == 't':
            print('============= Transaksi Anda Sudah Dibatalkan. =============')
            break
        else:
            print('==================== Inputan Anda Salah ====================')
        


# Menu User
def menu_user():
    print('=============== Selamat Datang Di Ammunation ===============')

    senjata = PrettyTable()
    senjata.field_names = ['no', 'nama_senjata', 'jenis_senjata', 'harga_senjata']
    for row in senjata_list:
        senjata.add_row(row)

    print('======================= Katalog Kami =======================')
    print(senjata)
    print('=' * 60)
    while True:
        konfirmasi = input('=========== Apakah Anda ingin Melakukan Transaksi? (Y/T) : ')
        if konfirmasi == 'Y' or konfirmasi == 'y':
            transaksi_user()
            break
        elif konfirmasi == 'T' or konfirmasi == 't':
            print('============= Transaksi Anda Sudah Dibatalkan. =============')
            break
        else:
            print('==================== Inputan Anda Salah ====================')
# ================================================================================



def admin_menu():
    print('=' * 60)
    print('Selamat datang Admin!!!!')
    baca_tabel()
    
    while True:
        print('=' * 60)
        print('1. Lihat Tabel Senjata')
        print('2. Tambah Senjata Baru')
        print('3. Edit Data Senjata')
        print('4. Hapus Senjata')
        print('5. Keluar')
        print('=' * 60)

        aksi = input('Apa yang ingin anda lakukan? : ')
        if aksi == '1':
            baca_tabel()
        elif aksi == '2':
            admin_tambah_senjata()
        elif aksi == '3':
            admin_edit_senjata()
        elif aksi == '4':
            admin_hapus_senjata()
        elif aksi == '5':
            print('Sampai Jumpa lagi :)')
            break


def user_menu():
    menu_user()


# Credential Login : 
#  Admin = superadmin | 1234
#  Admin = user | 1234


def login():
    print('Selamat Datang, Silahkan Login terlebih Dahulu!!!!')
    while True:
        nama_login = input('Username : ')
        password_login = input('Password : ')

        if nama_login == admin[0] and password_login == admin[1]:
            admin_menu()
            break
        elif nama_login == pembeli[0] and password_login == pembeli[1]:
            user_menu()
            break
        else:
            print('Maaf credential anda salah')
            print('Silahkan Login Ulang')
            print('=' * 60)


login()