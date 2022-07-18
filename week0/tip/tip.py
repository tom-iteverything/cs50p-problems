# main function
def main():
    dollars = dollars_to_float(input("How much was the meal? ($##.##): "))
    percent = percent_to_float(input("What percentage would you like to tip? (##%): "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Convert to decimal
def dollars_to_float(d: str):
    # Remove leading '$'; return float version
    return float(d.removeprefix("$"))

# Convert to decimal precentage
def percent_to_float(p: str):
    # Remove ending '%'; return float version divided by 100
    return float(p.removesuffix("%"))/100

# run program
main()