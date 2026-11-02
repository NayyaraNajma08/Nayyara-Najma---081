animals = ["otter", "hamster", "lion", "cat"]
print("the first three items in the list are:")
print(animals[:3])

middle_index = len(animals)//2
print("\nThree items from the middle index and slice 3 items around it are:")
print(animals[middle_index - 1: middle_index + 2])

print("\nThe last three items in the list are:")
print(animals[-3:])