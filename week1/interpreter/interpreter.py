# Main program asking Mathematical expression
def main():
    inputExpression = input("Expression: ")

    # Assign vars by space delimited
    x,y,z = int(inputExpression.split(" ")[0]), inputExpression.split(" ")[1], int(inputExpression.split(" ")[2])

    # Print expression
    answer(x,y,z)

# Define & print expression's answer
def answer(first,second,third):
    match second:
        case "+":
            print(f"{float(first+third):,.1f}")
        case "-":
            print(f"{float(first-third):,.1f}")
        case "*":
            print(f"{float(first*third):,.1f}")
        case "/":
            print(f"{float(first/third):,.1f}")

# Run program
main()