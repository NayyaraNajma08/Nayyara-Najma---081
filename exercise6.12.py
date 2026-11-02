person = {
    'first_name': 'Bang',
    'last_name': 'Yedam',
    'age': 24,
    'city': 'Seoul'
}
person_2={
    'first_name': 'Hira',
    'last_name': 'Dewi',
    'age': 18,
    'city': 'Surabaya',
}
person_3={
    'first_name': 'Yura',
    'last_name': 'Putri',
    'age': 18,
    'city': 'Bandung',
}
people = [person, person_2, person_3]
people[0]['hobby'] = 'singing'
people[1]['hobby'] = 'cooking'
people[2]['hobby'] = 'reading' 
for person_info in people:
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    print(full_name)
    print(f"\tAge: {person_info['age']}")
    print(f"\tCity: {person_info['city']}")
    print(f"\tHobby: {person_info['hobby']}\n")