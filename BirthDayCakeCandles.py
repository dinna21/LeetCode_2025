candles = [4,5,1,3,6,2,1,3,4,5,6,6,6]
maxcandle = candles[0]
count = 0
for i in range(len(candles)):
    if maxcandle <= candles[i]:
        maxcandle = candles[i]
print(maxcandle)
print(candles.count(maxcandle))
