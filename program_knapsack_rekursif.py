def knapsack(barang, target, hasil=[]):
    if target == 0:
        return hasil

    if target < 0 or len(barang) == 0:
        return None

    ambil = knapsack(
        barang[1:],
        target - barang[0],
        hasil + [barang[0]]
    )

    if ambil:
        return ambil

    return knapsack(barang[1:], target, hasil)


barang = [2, 5, 6, 9, 12, 14, 20]

target = int(input("Masukkan target berat: "))

hasil = knapsack(barang, target)

if hasil:
    print("Kombinasi ditemukan:", hasil)
else:
    print("Tidak ada kombinasi")
