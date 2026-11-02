pet_1 = {'kind': 'cat', 'owner': 'nayya'}
pet_2 = {'kind': 'fish', 'owner': 'irfan'}
pet_3 = {'kind': 'bird', 'owner': 'syarif'}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner: {pet['owner'].title()}\n")