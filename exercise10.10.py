from pathlib import Path

def count_the(filename):
    """Hitung berapa kali kata 'the' muncul di sebuah file."""
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.")
        return

    lowered = contents.lower()
    print(f"{filename}:")
    print(f"  'the'  -> {lowered.count('the')} kali")
    print(f"  'the ' -> {lowered.count('the ')} kali")

count_the('Exercise/alice.txt')