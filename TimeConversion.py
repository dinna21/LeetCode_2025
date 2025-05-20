s = '12:05:45PM'

if 'PM' in s:
    if s[:2] == '12':
        print(s[:8])
    else:
        print("PM is included")
        print(s[:2])
        front = (str(int(s[:2])+12))
        back = (s[2:8])
        print(front+back)
else:
    print("AM is included")
    if s[:2] == '12':
        front = '00'
        print(front+s[2:8])

