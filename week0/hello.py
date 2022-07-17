# Ask user for their name, 'strip' the whitespaces, capitalize it & split the name a part into two vars
first, last = input("What is your name?: ").strip().title().split(" ")

# Print the full name
print(f"Hello, {first} {last}.")
