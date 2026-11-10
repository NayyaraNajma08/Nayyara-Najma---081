from pathlib import Path

names = []
print("Ketik 'q' untuk berhenti.")
while True:
    name = input("Masukkan nama Anda: ")
    if name == 'q':
        break
    names.append(name)

contents = ""
for name in names:
    contents += f"{name}\n"

path = Path('guest_book.txt')
path.write_text(contents)