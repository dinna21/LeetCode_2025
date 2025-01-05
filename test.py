def find_pairs_with_sum_zero(numbers):
    seen = []  # To store numbers we've seen
    result = []   # To store pairs that add up to 0
    print("set is ",seen)
    
    for num in numbers:
        if -num in seen:  # Check if the negative of the current number exists in the set
            result.append((num, -num))  # Add the pair to the result
        seen.append(num)  # Add the current number to the set
        print("seen is ",seen)
        print("result is ",result)
    
    return result

# Example usage
numbers = [-3, 3, 4, 90]
pairs = find_pairs_with_sum_zero(numbers)
print("Pairs that add up to 0:", pairs)
