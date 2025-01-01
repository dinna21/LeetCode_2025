s = "0P"
# s = "Was it a car or a cat I saw?"

reversed_striing = s[::-1]
filtered_striing = ''.join(char for char in s if char.isalpha() or char.isdigit())
print("filterd string is ", filtered_striing.lower())
rev_striing = ''.join(char for char in reversed_striing if char.isalpha() or char.isdigit())
print("reversed string is ", rev_striing.lower())
if rev_striing.lower() == filtered_striing.lower():
    print(True)
else:
    print(False)