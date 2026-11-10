print("Kalkulator penjumlahan. Ketik 'q' untuk keluar.")

while True:
    first = input("\nAngka pertama: ")
    if first == 'q':
        break
    second = input("Angka kedua: ")
    if second == 'q':
        break

    try:
        total = int(first) + int(second)
    except ValueError:
        print("Maaf, kamu harus memasukkan angka, bukan teks.")
    else:
        print(f"Hasil penjumlahan: {total}")