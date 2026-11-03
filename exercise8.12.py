def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("tuna")
make_sandwich("egg", "cheese", "lettuce")
make_sandwich("chicken", "tomato", "mayo", "ham", "turkey")