s = "zxyzxyz"
set_str = set(s)
# print(set_str)

max_len = 0
seen = set()
# print(seen)
start = 0
for end in range(len(s)):
    # print(end)
    while s[end] in seen:
        seen.remove(s[start])
        start+=1
    seen.add(s[end])
    max_len = max(max_len,end -start+1)
print(max_len)

longest = 0
current = ""
for char in s :
    if char in current:
        index = current.index(char)
        current = current[index+1:]
    current+=char
    longest = max(longest,len(current))
print(longest)

Input: "zxyzxyz"
# We go through each character of the string one by one:

# 🔁 Step-by-step Execution:
# 1. char = 'z'
# 'z' not in current, so we add it:
# current = "z"

# Update longest: longest = max(0, 1) = 1

# 2. char = 'x'
# 'x' not in current, add it:
# current = "zx"

# Update longest: longest = max(1, 2) = 2

# 3. char = 'y'
# 'y' not in current, add it:
# current = "zxy"

# Update longest: longest = max(2, 3) = 3

# 4. char = 'z' ← Repeated!
# 'z' is already in "zxy" at index 0

# Remove part up to and including that 'z':
# current = "zxy"[1:] = "xy"

# Add 'z':
# current = "xyz"

# Update longest: longest = max(3, 3) = 3

# 5. char = 'x' ← Repeated!
# 'x' is in "xyz" at index 0

# Remove up to 'x':
# current = "yz"

# Add 'x':
# current = "yzx"

# Update longest: longest = max(3, 3) = 3

# 6. char = 'y' ← Repeated!
# 'y' is in "yzx" at index 0

# Remove up to 'y':
# current = "zx"

# Add 'y':
# current = "zxy"

# Update longest: longest = max(3, 3) = 3

# 7. char = 'z' ← Repeated!
# 'z' is in "zxy" at index 0

# Remove up to 'z':
# current = "xy"

# Add 'z':
# current = "xyz"

# Update longest: longest = max(3, 3) = 3

# ✅ Final Output:
# python
# Copy code
# return longest  # 3
# 🧠 So what’s happening?
# Every time a character repeats, we remove everything before and including its first appearance. This way, we always keep a clean substring with no duplicates.