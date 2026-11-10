from pathlib import Path
import json

path = Path('user_info.json')

if path.exists():
    contents = path.read_text()
    user = json.loads(contents)
    print("Data yang saya ingat tentang kamu:")
    print(f"  Nama          : {user['name']}")
    print(f"  Umur          : {user['age']}")
    print(f"  Kota          : {user['city']}")
    print(f"  Warna favorit : {user['color']}")
else:
    user = {}
    user['name'] = input("Siapa namamu? ")
    user['age'] = input("Berapa umurmu? ")
    user['city'] = input("Kamu tinggal di kota mana? ")
    user['color'] = input("Apa warna favoritmu? ")

    contents = json.dumps(user)
    path.write_text(contents)
    print(f"Data tersimpan. Sampai jumpa lagi, {user['name']}!")