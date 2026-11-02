my_foods = ['cinnamon roll', 'chocolate', 'bagel', 'donut', 'croissant']
friend_foods = my_foods[:]
my_foods.append('croissant')
friend_foods.append('pancake')
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("My friend's favorite foods are:")
for food in friend_foods:
    print(food)