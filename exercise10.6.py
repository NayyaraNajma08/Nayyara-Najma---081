first = input("Angka pertama: ")
second = input("Angka kedua: ")

try:
    total = int(first) + int(second)
except ValueError:
    print("Maaf, kamu harus memasukkan angka, bukan teks.")
else:
    print(f"Hasil penjumlahan: {total}")