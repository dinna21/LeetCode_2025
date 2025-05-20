def diagonalDifference(arr):
    num1 = 0
    num2 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                num1+=arr[i][j]
            if (i+j)==len(arr)-1:
                num2+=arr[i][j]
    return abs(num1 - num2)
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))