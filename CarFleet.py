target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]
sortPosition = sorted(position,reverse=True)
print(sortPosition)
fleets = []
count = 0
for num in position:
    result = (target-num)/speed[(position.index(num))]
    print(result)
    fleets.append(result)
    # print(position.index(num))




# result = (position.index(7))
# print(speed[result])
fleets= set(fleets)
print(fleets)
print(len(fleets))



cars = list(zip(position,speed))
print(cars)

cars.sort(reverse=True)
times = []
for pos, spd in cars:
    time = (target - pos) / spd
    times.append(time)
fleets = 0
prev_time = 0

for time in times:
    if time>prev_time:
        fleets+=1
        prev_time = time
return fleets