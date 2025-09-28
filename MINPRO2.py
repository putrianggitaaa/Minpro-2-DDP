#MINPRO 2 DDP
#NAMA: PUTRI ANGGITA MELASARI
#NIM: 2509116010
#KELAS: SI A'25

#DICTIONERY BERISI DATA ANGGOTA DAN JABATAN
Nama = { 
    "Ketua" : "Muhammad Faris",
    "Wakil" : "Ananda Ion Jahfal",
    "Sekretaris" : "Nadya Kusuma Astuti",
    "Bendahara" : "Zessiva Isma Putri"
}

#DICTIONERY BERISI PASSWORD ROLE
users = {
    "admin" : "admin",
    "user" : "user"
}
#LIBRARI TABEL DAN PWINPUT
from prettytable import PrettyTable
import pwinput

#FUNCTION READ
def lihat_anggota():
    print("----------------------------------------")
    print("======Daftar Pengurus BEM FT 2025======")
    print("----------------------------------------")
    table = PrettyTable()
    table.field_names = ["No", "Jabatan", "Nama"]
    for i, (jabatan, nama)  in enumerate (Nama.items(), start=1):
        table.add_row([i, jabatan, nama])
    print(table)
    print()

#FUNCTION CREATE
def tambah_anggota():
        jabatan = (input("Masukkan jabatan: "))
        if jabatan in Nama:
            print ("Jabatan sudah diisi ya Abang/Mba. Silakan pilih menu 4 untuk memperbarui.")
            return
        nama = str(input("Masukkan nama anggota: "))
        Nama[jabatan] = nama
        print (f"Selamat! Abang/Mba berhasil menambahkan {nama} sebagai {jabatan} pada keanggotaan BEM FT 2025") 

#FUNCTION UPDATE
def update_anggota():
        jabatan = (input("Masukkan jabatan yang ingin di update: "))
        if jabatan not in Nama:
            print("Maaf ya Abang/Mba, jabatan tidak ditemukan")
            return
        nama_baru = (input("Masukkan nama anggota baru: "))
        Nama[jabatan] = nama_baru
        print (f"{jabatan} kini dipegang oleh {nama_baru}")

#FUNCTION DELETE
def hapus_anggota():
        jabatan = (input("Masukkan jabatan yang ingin dihapus: "))
        if jabatan not in Nama:
            print ("Maaf ya Abang/Mba, jabatan tidak terdaftar")
            return
        del Nama[jabatan]
        print(f"{jabatan} berhasil dihapus")

#FUNCTION LOGIN
def login():
    while True:
            print("----------------------------------------")
            print("Sistem Manajemen Keanggotaan BEM FT 2025")
            print("----------------------------------------")
            print("Silakan login terlebih dahulu! \n")
            print ("1. Admin ")
            print ("2. User \n") 
            try:
                pilihrole = int((input("Abang/Mba ingin login sebagai apa? (1/2)\n")))
            except ValueError:
                print("Abang/Mba pilih role menggunakan angka ya!\n")
            except KeyboardInterrupt:
                print("Abang/Mba pilih menu logout untuk keluar ya")
                continue

            if pilihrole == 1:   
                pwd = pwinput.pwinput("Masukkan password: ")
                if pwd == users["admin"]:   
                    print("Halo, Abang/Mba berhasil login sebagai admin! \n")
                    return "admin"
                else:
                    print("Password Abang/Mba salah nih, silakan ulangi proses login ya! \n")

            elif pilihrole == 2:
                pwd = pwinput.pwinput("Masukkan password: ")
                if pwd == users["user"]:
                    print ("Halo, Abang/Mba berhasil login sebagai user! \n")
                    return "user"
                else:
                    print("Password Abang/Mba salah nih, silakan ulangi proses login ya! \n")
            else:
                print ("Role hanya ada 2 ya Abang/Mba")

#FUNCTION UNTUK MENU ROLE ADMIN
def menu_admin():
    while True:
        print("-----------------------------------------------------------------")
        print ("===Selamat Datang di Sistem Manajemen Keanggotaan BEM FT 2025===")
        print("-----------------------------------------------------------------\n")
        print("1. Lihat Anggota")
        print("2. Tambah Anggota")
        print("3. Hapus Anggota")
        print("4. Update Anggota")
        print("5. Logout")
        try:
            pilih = int((input("Abang/Mba mau ngapain?: ")))
            if pilih == 1:
                lihat_anggota()
            elif pilih == 2:
                tambah_anggota()
            elif pilih == 3:
                hapus_anggota()
            elif pilih == 4:
                update_anggota()
            elif pilih == 5:
                print ("Abang/Mba telah logout")
                break
            else:
                print("Input dengan benar ya Abang/Mba!")
        except ValueError:
            print ("Abang/Mba pilih menu dengan angka ya!")
        except KeyboardInterrupt:
            print("Abang/Mba pilih menu logout untuk keluar ya")


#FUNCTION UNTUK MENU ROLE USER
def menu_user():
    while True:
        print("-----------------------------------------------------------------")
        print ("===Selamat Datang di Sistem Manajemen Keanggotaan BEM FT 2025===")
        print("-----------------------------------------------------------------\n")
        print("1. Lihat Anggota")
        print("2. Logout")
        try:
            pilih = int((input("Abang/Mba mau ngapain?: ")))

            if pilih== 1:
                lihat_anggota()
            elif pilih == 2:
                print("Abang/Mba telah logout")
                break
            else:
                print("Menu lainnya hanya bisa diakses oleh Admin ya!")
        except ValueError:
            print("Abang/Mba pilih menu dengan angka ya!")
        except KeyboardInterrupt:
            print("Abang/Mba pilih menu logout untuk keluar ya")

#FUNCTION MENU UTAMA
def main():
    role = login()
    if role == "admin":
        menu_admin()    
    else:
        menu_user()
    print ("Terima kasih Abang/Mba sudah menggunakan layanan kami!")
main()
