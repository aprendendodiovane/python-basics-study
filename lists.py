names = ["diovane", "joão", "arthur", "guilherme", "renan", "kauã"]

for name in names:
    message = f"Hello {name.title()}, how are you?!"
    print(message)

# Add an item to the list, always in the last position
names.append("bruno")

print(f"\n{names}\n")

# Add an item to the list, in the index informed
names.insert(1, "augusto")

print(f"\n{names}\n")

# Delete the name in the index from the list
del names[0]

print(f"\n{names}\n")

# Pop the name from the list, always the first index
popped_name = names.pop()

print(f"\n{names}\n")
print(f"\n{popped_name}\n")

# Pop the index informed from the list
new_popped_name = names.pop(3)

print(f"\n{names}\n")
print(f"\n{new_popped_name}\n")

print(f"\n{names}\n")

# Remove the name informed, not the index
names.remove("renan")

print(f"\n{names}\n")

cars_loved = ["lancer evolution", "nissan skyline", "toyota supra", "nissan 370z", "mazda rx7"]

print(f"\n{cars_loved}\n")

cars_loved.sort()

## Permanent sorting alphabetically
print(f"\n{cars_loved}\n")

# Permanent sorting, in reverse alphabetically
cars_loved.sort(reverse=True)

print(f"\n{cars_loved}\n")

# Reverse the list, not alphabetically, but by position
cars_loved.reverse()

print(f"\n{cars_loved}\n")

for car in cars_loved:
    message = f"I would like to own a {car.title()}!"
    print(message)

brands = ["louis vitton", "tommy hilfiger", "cartier", "hugo boss", "aramis", "brooksfield"]

print(f"\n{brands}\n")

# The function sorted does not change the list permanently
print(f"\n{sorted(brands)}\n")

# The function sorted does not change the list permanently but in reverse
print(f"\n{sorted(brands, reverse=True)}\n")

# Function len returns the size of the list
brands_size = len(brands)

print(f"\n{brands_size}\n")

magicians = ['alicia', 'david', 'otto']

for magician in magicians:
    print(f"\n{magician}\n")

# Range count a list, but we need to put list() to really create a list
for val in list(range(0, 10)):
    print(f"{val}")

print("\n")

# We can use a third parameter to skip values
for num in range(0, 10, 2):
    print(f"{num}")

squared_nums = []

for num in range(1, 11):
    squared_nums.append(num**2)
print(f"\n{squared_nums}\n")

list_of_numbers = list(range(1, 10000))

print(list_of_numbers)
print("\n")
print(min(list_of_numbers))
print("\n")
print(max(list_of_numbers))
print("\n")
print(sum(list_of_numbers))

# Creates the same thing as squared_nums
squares = [val**2 for val in range(1, 11)]

# Exercise 4-3
for num in range(1, 21):
    print(num)

# Exercise 4-4
million_nums = [num for num in range(1, 1000001)]

for num in million_nums:
    print(num)

# Exercise 4-5
print(min(million_nums))
print(max(million_nums))
print(sum(million_nums))

# Exercise 4-6
for num in range(1, 21, 2):
    print(num)

print("\n")

# Exercise 4-7
multiples_of_3 = [num*3 for num in range(1, 11)]

for num in multiples_of_3:
    print(num)

print("\n")

# Exercise 4-8 and 4-9
cubes = [num**3 for num in range(1, 11)]

for num in cubes:
    print(num)

print("\n")

numbers = [num*2 for num in range(1, 20)]

# Slices the list beginning from the second index until the 8 index
print(numbers[1:9])

# Slices the list from index 0 through the value informed after ':'
print(numbers[:6])

# Slices the list beginning from value informed before ':'
print(numbers[9:])
