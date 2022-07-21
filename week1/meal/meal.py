# Main function
def main():
    timeValue = convert(input("What time is it?: ").strip())
    if timeValue >= 7.0 and timeValue <= 8.0: print("Breakfast time!")
    elif timeValue >= 12.0 and timeValue <= 13.0: print("Lunch time!")
    elif timeValue >= 18.0 and timeValue <= 19.0: print("Dinner time!")
    else: print()

# Function to convert time
def convert(time):
    return float(time.split(":")[0]) + float(time.split(":")[1])/60

# Run program
if __name__ == "__main__":
    main()