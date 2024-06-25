#tentang inputan pasien
def input_nama_pasien():
    nama_pasien = []

    while True:
        nama = input("Masukkan nama pasien (atau ketik 'selesai' untuk mengakhiri): ")
        if nama.lower() == 'selesai':
            break
        nama_pasien.append(nama)

    return nama_pasien

def cari_nama_pasien(nama_pasien, nama_cari):

    for index, nama in enumerate(nama_pasien, start=1):
        if nama == nama_cari:
            return index
    return -1  

def tampilkan_urutan_nama(nama_pasien):
    print("\nDaftar nama pasien:")
    for index, nama in enumerate(nama_pasien, start=1):
        print(f"{index}. {nama}")

if __name__ == "__main__":
    daftar_nama_pasien = input_nama_pasien()

    tampilkan_urutan_nama(daftar_nama_pasien)

    nama_cari = input("\nMasukkan nama pasien yang ingin Anda cari: ")

    hasil_pencarian = cari_nama_pasien(daftar_nama_pasien, nama_cari)
    
    if hasil_pencarian != -1:
        print(f"\nNama '{nama_cari}' ditemukan pada posisi ke-{hasil_pencarian}.")
    else:
        print(f"\nNama '{nama_cari}' tidak ditemukan dalam daftar nama pasien.")
