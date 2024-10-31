contacts = {}


def show_contacts():
    if contacts:
        print("\nDaftar Kontak:")
        for contact_id, info in contacts.items():
            print(f"ID: {contact_id}, Nama: {info['nama']}, Nomor Telepon: {info['nomor_telepon']}")
    else:
        print("\nKontak kosong.")


def add_contact():
    contact_id = input("\nMasukkan ID kontak: ")
    if contact_id in contacts:
        print("ID kontak sudah ada.")
        return

    nama = input("Masukkan nama: ")
    nomor_telepon = input("Masukkan nomor telepon: ")
    contacts[contact_id] = {'nama': nama, 'nomor_telepon': nomor_telepon}
    print("Kontak berhasil ditambahkan.")

def update_contact():
    contact_id = input("\nMasukkan ID kontak yang akan diubah: ")
    if contact_id not in contacts:
        print("ID kontak tidak ditemukan.")
        return

    nama = input("Masukkan nama baru: ")
    nomor_telepon = input("Masukkan nomor telepon baru: ")
    contacts[contact_id] = {'nama': nama, 'nomor_telepon': nomor_telepon}
    print("Kontak berhasil diubah.")


def delete_contact():
    contact_id = input("\nMasukkan ID kontak yang akan dihapus: ")
    if contact_id in contacts:
        del contacts[contact_id]
        print("Kontak berhasil dihapus.")
    else:
        print("ID kontak tidak ditemukan.")

def main():
    while True:
        print("\nMenu:")
        print("1. Tampilkan kontak")
        print("2. Tambah kontak")
        print("3. Ubah kontak")
        print("4. Hapus kontak")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            show_contacts()
        elif pilihan == '2':
            add_contact()
        elif pilihan == '3':
            update_contact()
        elif pilihan == '4':
            delete_contact()
        elif pilihan == '5':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
