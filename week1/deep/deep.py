# create funciton to validate quesiton
def universeQuestion(q):
    if (q.isnumeric()):
        q = int(q)
        match q:
            case 42:
                return True
            case _:
                return False
    else:
        match (q.lower()):
            case "forty-two" | "forty two":
                return True
            case _:
                return False

# create main function
def main():
    answer = input("What is Answer to the Great Question of Life, the Universe and Everything?: ")
    if universeQuestion(answer): print(f"Yes.")
    else: print(f"No.")

# run program
main()