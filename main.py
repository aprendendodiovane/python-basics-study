# Working with lstrip, rstrip and strip
test = "   test   "

print(test.rstrip())
print(test.lstrip())
print(test.strip())

# Working with input, lower, title and concatenation
first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()

greeting = f"Hello {(first_name + " " + last_name).title()}!"

print(greeting)