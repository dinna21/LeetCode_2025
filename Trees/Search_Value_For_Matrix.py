matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
i=0
while i<=2:
# we can use for loop instead of while loop 
    # for row in matrix:
    # print(matrix[i])
    # print(binary_search(matrix[i],target=10))
    if binary_search(matrix[i],target=10) == True:
    # We can use  this instead of above line 
        # if binary_search(matrix[i],target=10):
        print(True)
        break
    i+=1
print(False)


