favorite_languages = {
    'Vela': 'Japanese',
    'Nayya': 'Korean',
    'Salsa': 'Indonesian',
    'Luna': 'English',
}
people_to_poll = ['Vela', 'Nayya', 'Salsa', 'Luna', 'Shinta']

for name in people_to_poll:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"{name.title()}, please take our favorite languages poll!")