# Sets playback as a string, inputted, and replaces the spaces with '...'
playback = str(input("Type a sentence: ")).strip().replace(" ","...")

# "Slow's down" the sentence with periods
print(f"{playback}")