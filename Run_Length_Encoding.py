inputStr = "3322251"

# Dictionary to store character counts
char_count = {}
duplicates = {}
# Count occurrences of each character
for char in inputStr:
    char_count[char] = char_count.get(char, 0) + 1

# Print duplicate values
print(char_count.items())
for char,count in char_count.items():
    if count >= 1:
        duplicates[char] = count
print(duplicates)

char_count = {'3': 2, '2': 3, '5': 1, '1': 1}

# Generate the output string by repeating each key its corresponding number of times
output_str = "".join(str(count)+char for char,count in duplicates.items())

print(output_str)  # Output: "3322251"



n = 3
result = "1"
for numbers in range(n-1):
    new_result = ""
    i = 0
    while i < len(result):
        count = 1
        while(i+1) < len(result) and result[i] == result[i+1]:
            i+=1
            count+=1
        new_result += str(count)+result[i]
        i+=1
    result = new_result
print(result)




