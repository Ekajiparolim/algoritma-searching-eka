def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

def main():

    n = int(input("Masukkan jumlah buku: "))
    barang = []

    for _ in range(n):
        code = int(input("Masukkan kode buku: "))
        judul = input("Masukkan judul buku: ")
        barang.append((code, judul))

    barang.sort(key=lambda item: item[0])

    codes = [barang[0] for barang in barang]
    names = [barang[1] for barang in barang]

    x = int(input("Masukkan kode buku yang akan dicari: "))

    result = binary_search(codes, x)

    if result != -1:
        print(f"Kode buku ditemukan pada indeks {result} dengan judul buku: {names[result]}")
    else:
        print("Kode buku tidak ditemukan dalam daftar")

if __name__ == "__main__":
    main()