favorite_places = {
    'Nayya': ['Malang', 'Bali'],
    'Salsa': ['yogyakarta'],
    'Vela': ['Purwokerto', 'Bandung', 'Solo'],
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")