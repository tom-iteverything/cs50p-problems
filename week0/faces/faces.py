# Main function
def main():
    # Sets emoji as a string, inputted
    emoji = input().strip()
    # Shows interpretted text as emoji
    print(convert(emoji))

# Convert function
def convert(asciiEmoji: str):
    return asciiEmoji.replace(":)", "🙂").replace(":(", "🙁")

main()