s = "xxxx"
print(len(set(s)))
def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
# Step-by-Step Explanation for s = "pwwkew":
# Iteration 1 (right = 0, s[0] = 'p'):

# Initial window: s[0:0] (empty) and char_set = {}.
# 'p' is not in char_set, so add 'p'.
# Window becomes: "p".
# current_length = 1
# max_length is updated to 1.
# Iteration 2 (right = 1, s[1] = 'w'):

# Current window: s[0:1] which is "p", char_set = {'p'}.
# 'w' is not in char_set, so add 'w'.
# Window becomes: "pw".
# current_length = 2
# max_length is updated to 2.
# Iteration 3 (right = 2, s[2] = 'w'):

# Current window: s[0:2] which is "pw", char_set = {'p', 'w'}.
# 'w' is already in char_set.
# Enter the while loop:
# Remove s[left] which is 'p' (at index 0), update left to 1.
# Check again: 'w' is still in the set (because now set = {'w'} and window is "w" from index 1).
# Remove s[left] which is 'w' (at index 1), update left to 2.
# Now, add 'w' from right = 2.
# Window becomes: "w".
# current_length = 1
# max_length remains 2.
# Iteration 4 (right = 3, s[3] = 'k'):

# Current window: s[2:3] which is "w", char_set = {'w'}.
# 'k' is not in char_set, so add 'k'.
# Window becomes: "wk".
# current_length = 2
# max_length remains 2.
# Iteration 5 (right = 4, s[4] = 'e'):

# Current window: s[2:4] which is "wk", char_set = {'w', 'k'}.
# 'e' is not in char_set, so add 'e'.
# Window becomes: "wke".
# current_length = 3
# max_length is updated to 3.
# Iteration 6 (right = 5, s[5] = 'w'):

# Current window: s[2:5] which is "wke", char_set = {'w', 'k', 'e'}.
# 'w' is already in char_set. Enter the while loop:
# Remove s[left] which is 'w' (at index 2), update left to 3.
# Now, add 'w' from right = 5.
# Window becomes: "kew" (from index 3 to 5).
# current_length = 3
# max_length remains 3.       
s = "pwwkew"
result = longest_substring(s)
print("Final result:", result)

    
    