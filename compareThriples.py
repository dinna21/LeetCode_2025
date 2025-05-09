a = [5, 6, 7]
b = [3,6,10]
def compareTriplets(a, b):
    # Write your code here
    resulta = 0
    resultb = 0
    for i in range(3):
        if a[i] > b[i]:
            resulta+=1
        if a[i] < b[i]:
            resultb+=1
    return (resultb,resulta)

print(compareTriplets(a,b))