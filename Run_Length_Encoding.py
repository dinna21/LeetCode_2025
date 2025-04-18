inputStr = "3322251"

# Dictionary to store character counts
char_count = {}

# Count occurrences of each character
for char in inputStr:
    char_count[char] = char_count.get(char, 0) + 1

# Print duplicate values
duplicates = {char: count for char, count in char_count.items() if count >= 1}
print(duplicates)


char_count = {'3': 2, '2': 3, '5': 1, '1': 1}

# Generate the output string by repeating each key its corresponding number of times
output_str = "".join(key * value for key, value in char_count.items())

print(output_str)  # Output: "3322251"




