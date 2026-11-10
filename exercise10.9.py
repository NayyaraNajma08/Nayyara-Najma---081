from pathlib import Path

filenames = ['exercise/cats.txt', 'exercise/dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"Isi {filename}:")
        print(contents)