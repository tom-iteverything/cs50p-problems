# Define the main() funciton or application
def main():
    # Ask user for their name, 'strip' the whitespaces, capitalize it & split the name a part into two vars
    first, last = input("What is your name?: ").strip().title().split(" ")
    # Print the full name
    hello(first, last)

# Define the help() function
def hello(f, l):
    print(f"Hello, {f} {l}.")

main()