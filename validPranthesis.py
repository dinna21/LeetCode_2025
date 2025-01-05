s = "(){}}{"
def is_valid_pranthesis(s):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
            # print(stack)
        elif char in  ')]}':
            if not stack:
                return False
            top = stack.pop()
        # print(stack)
            if matching_brackets[char] != top:
                return False
            else:
                return True
    # print(stack)
    return len(stack) == 0
print(is_valid_pranthesis(s)) # Output: True
