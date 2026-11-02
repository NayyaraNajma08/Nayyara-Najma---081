favorite_numbers = {
    'yedam': [7, 5, 2],
    'vela': [13, 31],
    'salsa': [28, 3],
    'luna': [43, 56],
    'shinta': [8, 1, 64],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")