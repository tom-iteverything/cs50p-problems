# Calculate "Greeting"
def response(reply: str):
    if reply == "hello": print("$0!")
    elif reply.startswith("h"): print("$20!")
    else: print("$100!")
# Main function
def main():
    greeting = str(input("Greeting: ")).strip().lower()
    response(greeting)

# run program
main()