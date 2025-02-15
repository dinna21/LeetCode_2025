# prices = [7, 6, 4, 3, 1]
# prices = [10,1,5,6,7,1]
prices=[1]
profits = []
if len(prices) == 1:
    print(0)
else:
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] < prices[j]:
                profits.append(prices[j] - prices[i])
            else:
                profits.append(0)
    max_price = profits[0]
    for i in range(1, len(profits)):
        if profits[i] > max_price:
            max_price = profits[i]
    print(profits)
    print(max_price)
