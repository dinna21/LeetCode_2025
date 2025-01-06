def is_valid_pranthesis(s):
    stack = []  # Initialize an empty stack
    matching_brackets = {')': '(', '}': '{', ']': '['}  # Map closing brackets to opening brackets

    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char in '({[':
            stack.append(char)
        # If the character is a closing bracket
        elif char in ')]}':
            # Check if the stack is empty (no matching opening bracket)
            if not stack:
                return False
            # Pop the top of the stack and check if it matches the current closing bracket
            top = stack.pop()
            if matching_brackets[char] != top:
                return False

    # After processing all characters, the stack should be empty for a valid string
    return len(stack) == 0

# Test case
# s = "(){}}{"
s = "(){}"
print(is_valid_pranthesis(s))  # Expected output: False
