places = ["Switzerland", "Japan", "Swiss", "Korea", "Norway"]
print("original order:")
print(places)

#print the list in alphabetical order print("\nHere is the list in alphabetical order:")
print("\nAlphabetical order:")
print(sorted(places))

print("\nOriginal order:")
print(places)

print("\nReverse-alphabetical order:")
print(sorted(places, reverse=True))

print("\nOriginal order:")
print(places)

places.reverse()
print("\nReversed order:")
print(places)

places.reverse()
print("\nBack to original order:")
print(places)

places.sort()
print("\nSorted alphabetically:")
print(places)

places.sort(reverse=True)
print("\nSorted in reverse alphabetical order:")
print(places)